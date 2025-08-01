from typing import Dict, List, Tuple
from collections import Counter
import re
import numpy as np
import pandas as pd  # type: ignore[import]
import pymupdf  # type: ignore[import]

# Assuming r1a.utils is available in the execution environment
from r1a.utils import extract_spans


# 1. CROSS-PAGE FONT ANALYSIS - Unchanged
def analyze_fonts_globally(df: pd.DataFrame) -> Dict:
    """Analyze font patterns across the entire document for better consistency."""
    unique_sizes = sorted(df['size'].unique(), reverse=True)
    if not unique_sizes:
        return {'size_clusters': {}, 'font_frequency': {}, 'total_spans': len(df)}

    clusters = []
    current_cluster = [unique_sizes[0]]

    for i in range(1, len(unique_sizes)):
        if (current_cluster[0] - unique_sizes[i]) / current_cluster[0] < 0.1:
            current_cluster.append(unique_sizes[i])
        else:
            clusters.append(current_cluster)
            current_cluster = [unique_sizes[i]]
    clusters.append(current_cluster)

    size_clusters = {size: rank for rank, cluster in enumerate(
        clusters, 1) for size in cluster}
    font_patterns = Counter(df['font'].values)

    return {
        'size_clusters': size_clusters,
        'font_frequency': dict(font_patterns),
        'total_spans': len(df)
    }

# 2. OPTIMIZED POSITION FEATURE EXTRACTION - Unchanged
def extract_position_features(df: pd.DataFrame) -> pd.DataFrame:
    """Extract position-based features from bounding boxes using vectorized operations."""
    df_enhanced = df.copy()
    bboxes = df_enhanced['bbox'].tolist()
    df_enhanced['x0'] = [b[0] for b in bboxes]
    df_enhanced['y0'] = [b[1] for b in bboxes]
    df_enhanced['x1'] = [b[2] for b in bboxes]
    df_enhanced['y1'] = [b[3] for b in bboxes]
    df_enhanced['height'] = df_enhanced['y1'] - df_enhanced['y0']
    df_enhanced['left_margin'] = df_enhanced['x0']

    page_heights = df_enhanced.groupby('page')['y1'].max()
    df_enhanced['page_height'] = df_enhanced['page'].map(page_heights)

    page_groups = df_enhanced.groupby('page')
    page_min_margin = page_groups['left_margin'].transform('min')
    page_max_margin = page_groups['left_margin'].transform('max')
    df_enhanced['left_margin_norm'] = (df_enhanced['left_margin'] - page_min_margin) / \
        (page_max_margin - page_min_margin + 1e-6)
    return df_enhanced

# 3. VECTORIZED LINGUISTIC & CONTEXT FEATURES - Unchanged
def apply_features(df: pd.DataFrame) -> pd.DataFrame:
    """Vectorized creation of linguistic and context features."""
    text_stripped = df['text'].str.strip()
    df['has_section_pattern'] = text_stripped.str.match(r'^\d+\.?\d*', na=False)
    df['word_count'] = df['text'].str.split().str.len().fillna(0)
    heading_keywords = {'introduction', 'conclusion', 'abstract', 'summary',
                        'background', 'methodology', 'results', 'discussion', 'chapter', 'section', 'references'}
    df['has_heading_keyword'] = df['text'].str.lower().str.split().apply(
        lambda words: any(word.strip(".,:") in heading_keywords for word in words) if isinstance(
            words, list) else False
    )

    df_sorted = df.sort_values(['page', 'y0']).reset_index()
    df_sorted['prev_y1'] = df_sorted.groupby('page')['y1'].shift(1)
    vertical_gap = df_sorted['y0'] - df_sorted['prev_y1']
    df_sorted['large_gap_before'] = vertical_gap > df_sorted['height'] * 1.5
    df_sorted.loc[df_sorted.groupby('page').head(
        1).index, 'large_gap_before'] = True
    return df_sorted.set_index('index').sort_index()

# 4. HEADING/TITLE MERGING LOGIC - Unchanged
def merge_candidates(candidates_df: pd.DataFrame, is_title: bool = False) -> List[Dict]:
    """Merges consecutive text spans that form a single heading or title."""
    if candidates_df.empty:
        return []

    merged = []
    candidates_df = candidates_df.sort_values(['page', 'y0'])

    buffer = []
    for _, row in candidates_df.iterrows():
        text = row['text'].strip()
        if not text:
            continue

        if not buffer:
            buffer.append(row)
            continue

        prev_row = buffer[-1]
        vertical_gap = row['y0'] - prev_row['y1']

        merge_threshold = row['height'] * 0.75 if is_title else row['height'] * 0.5
        if row['page'] == prev_row['page'] and vertical_gap < merge_threshold:
            buffer.append(row)
        else:
            full_text = ' '.join([b['text'].strip() for b in buffer])
            num_digits = sum(c.isdigit() for c in full_text)
            num_alpha = sum(c.isalpha() for c in full_text)
            is_mostly_numeric = num_digits > num_alpha and num_alpha < 5

            if not (is_mostly_numeric and not buffer[0].get('has_section_pattern', False)):
                merged.append({
                    'text': full_text, 'page': int(buffer[0]['page']),
                    'level': buffer[0]['level'], 'confidence': buffer[0]['confidence'],
                    'y0': buffer[0]['y0'], 'page_height': buffer[0]['page_height']
                })
            buffer = [row]

    if buffer:
        full_text = ' '.join([b['text'].strip() for b in buffer])
        num_digits = sum(c.isdigit() for c in full_text)
        num_alpha = sum(c.isalpha() for c in full_text)
        is_mostly_numeric = num_digits > num_alpha and num_alpha < 5
        if not (is_mostly_numeric and not buffer[0].get('has_section_pattern', False)):
            merged.append({
                'text': full_text, 'page': int(buffer[0]['page']),
                'level': buffer[0]['level'], 'confidence': buffer[0]['confidence'],
                'y0': buffer[0]['y0'], 'page_height': buffer[0]['page_height']
            })

    return merged

# 5. ADVANCED TITLE SCORING - Unchanged
def score_title_candidate(candidate: Dict) -> float:
    """Calculates a score based on content and position to identify the true title."""
    text = candidate['text'].lower()
    word_count = len(text.split())

    affiliation_keywords = ['university', 'department', 'institute',
                            'school', 'college', 'laboratory', 'center', 'china', 'usa', 'germany', 'australia']
    if any(keyword in text for keyword in affiliation_keywords):
        return -100.0

    if text.count(',') > 3 and word_count > 5:
        return -50.0

    score = candidate['confidence']

    if 5 <= word_count <= 25:
        score += 2.0
    elif word_count < 4 or word_count > 30:
        score -= 1.0

    relative_y = candidate['y0'] / candidate.get('page_height', 792)
    if 0.1 < relative_y < 0.5:
        score += 2.0

    return score

# 6. MAIN PROCESSING FUNCTION (REWRITTEN FOR ACCURACY)
def process_pdf_enhanced(pdf_path: str) -> Dict:
    """Processes a PDF using advanced heuristics for high accuracy."""
    doc = pymupdf.open(pdf_path)
    # Use the provided utility to extract spans
    df = extract_spans(doc)

    if df.empty:
        return {'title': '', 'outline': []}

    font_analysis = analyze_fonts_globally(df)
    df = extract_position_features(df)
    df = apply_features(df)

    # Vectorized Scoring
    scores_df = pd.DataFrame(index=df.index)
    scores_df['title'] = 0
    scores_df['h1'] = 0
    scores_df['h2'] = 0
    scores_df['h3'] = 0

    df['size_cluster'] = df['size'].map(
        font_analysis.get('size_clusters', {})).fillna(999)
    
    # --- MODIFICATION 1: More flexible H1 scoring ---
    # Allow size_cluster 1 on page 1 to be a potential H1 as a fallback for title.
    # Give 'title' a higher score (5) to ensure it's preferred if it passes its own checks.
    scores_df['title'] += ((df['size_cluster'] == 1) & (df['page'] == 1)) * 5
    scores_df['h1'] += ((df['size_cluster'] == 1) * 4) + ((df['size_cluster'] == 2) * 3)
    scores_df['h2'] += ((df['size_cluster'] == 2) * 2) + \
        ((df['size_cluster'] == 3) * 3)
    scores_df['h3'] += (df['size_cluster'] == 3) * 2

    scores_df['title'] += df['is_bold'] * 2 + df['large_gap_before'] * 2
    scores_df['h1'] += df['is_bold'] * 2 + df['large_gap_before'] * 2
    scores_df['h2'] += df['is_bold'] * 1 + df['large_gap_before'] * 1
    scores_df['h1'] += (df['has_heading_keyword']) * 2
    scores_df['h2'] += (df['has_heading_keyword']) * 1

    df['level'] = scores_df.idxmax(axis=1)
    total_scores = scores_df.sum(axis=1)
    df['confidence'] = scores_df.max(axis=1) / total_scores.replace(0, 1)

    # Filter candidates
    candidates = df[(df['confidence'] > 0.30) & (df['level'] != 'none')].copy()

    # --- Advanced Title Extraction ---
    title_candidates = candidates[(
        candidates['level'] == 'title') & (candidates['page'] == 1)]
    merged_titles = merge_candidates(title_candidates, is_title=True)

    final_title = ""
    if merged_titles:
        scored_titles = [(cand, score_title_candidate(cand))
                         for cand in merged_titles]
        if scored_titles:
            best_title_candidate = max(scored_titles, key=lambda item: item[1])
            if best_title_candidate[1] > 0:
                final_title = best_title_candidate[0]['text']

    # --- Outline Extraction ---
    outline_candidates = candidates[candidates['level'] != 'title']
    merged_outline = merge_candidates(outline_candidates)

    outline = [
        {'level': item['level'].upper(),
         'text': item['text'], 'page': item['page']}
        for item in merged_outline
    ]

    # --- MODIFICATION 2: ROBUST TITLE FALLBACK ---
    # If no title was found, promote the first H1/H2 from page 1.
    if not final_title and outline:
        # Find the first heading from page 1 in the generated outline.
        # The outline is already sorted by page and vertical position.
        page1_headings = [h for h in outline if h['page'] == 1]
        if page1_headings:
            title_from_outline = page1_headings[0]
            final_title = title_from_outline['text']
            # Remove the promoted heading from the outline to avoid duplication
            outline.remove(title_from_outline)

    return {'title': final_title, 'outline': outline}