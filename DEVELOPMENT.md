# Development Setup with GitHub Copilot

## Prerequisites
- Python 3.8+ (tested with 3.12.3)
- Docker (for containerized execution)
- VS Code with GitHub Copilot extension (recommended)

## GitHub Copilot Setup

### 1. Install Required Extensions
The repository includes VS Code extension recommendations. Open the project in VS Code and install the recommended extensions:
- GitHub Copilot
- GitHub Copilot Chat
- Python extension pack
- Docker extension

### 2. VS Code Configuration
The `.vscode/settings.json` file is pre-configured for optimal Copilot integration with:
- Python-specific Copilot settings
- Inline suggestions enabled
- Advanced Copilot features configured
- Code formatting and linting setup

### 3. Copilot Context
The `.github/copilot-instructions.md` file provides comprehensive context about:
- Project architecture and design patterns
- Key modules and their responsibilities
- Code conventions and development guidelines
- Common operations and extension patterns

## Local Development Environment

### Option 1: Virtual Environment (Recommended for Development)
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python main.py input output
```

### Option 2: Docker Environment (Production-like)
```bash
# Build the Docker image
docker build --platform linux/amd64 -t document-intelligence:dev .

# Run with mounted volumes
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  document-intelligence:dev
```

## Development Workflow with Copilot

### 1. Code Completion
- Copilot will provide intelligent suggestions based on:
  - Project context from `.github/copilot-instructions.md`
  - Existing code patterns in the repository
  - Python and ML/AI best practices

### 2. Code Generation
- Use Copilot Chat for generating new functions
- Example prompts:
  - "Create a function to validate PDF input format"
  - "Add error handling for embedding model loading"
  - "Generate unit tests for the relevance scoring logic"

### 3. Documentation
- Copilot can help generate docstrings following the project's style
- Ask for explanations of complex algorithms
- Generate comments for multi-step processes

### 4. Debugging
- Use VS Code's integrated debugger with launch configurations
- Copilot can suggest debugging strategies and help analyze stack traces
- The debug configurations are pre-configured for the main pipeline components

## Project Structure for Copilot Context

```
document-intelligence/
├── .github/
│   └── copilot-instructions.md    # Copilot context and guidelines
├── .vscode/
│   ├── settings.json              # VS Code and Copilot settings
│   ├── extensions.json            # Recommended extensions
│   └── launch.json                # Debug configurations
├── models/                        # Local ML models
├── r1a/                          # PDF extraction components
├── main.py                       # Main pipeline orchestrator
├── semantic_analyzer.py          # Embedding and semantic analysis
├── relevance_scorer.py           # Hybrid ranking algorithm
├── subsection_extractor.py       # Text refinement logic
├── requirements.txt              # Python dependencies
└── Dockerfile                    # Container configuration
```

## Tips for Effective Copilot Usage

### 1. Context-Aware Prompts
- Reference specific modules: "In relevance_scorer.py, add a function to..."
- Mention the project domain: "For PDF document analysis, create..."
- Use existing patterns: "Following the threading pattern in main.py..."

### 2. Code Comments
- Add comments describing your intent before writing code
- Copilot uses comments as context for suggestions
- Example: `# Calculate cosine similarity between section embeddings and user intent`

### 3. Function Signatures
- Start with clear function names and type hints
- Copilot will suggest implementations based on the signature
- Example: `def calculate_hybrid_score(semantic_score: float, bm25_score: float) -> float:`

### 4. Testing Integration
- Use Copilot to generate test cases
- Ask for edge case scenarios
- Generate mock data for PDF processing tests

## Performance Considerations

### Memory Usage
- The Granite embedding model requires ~400MB RAM
- Multiprocessing creates separate Python processes
- Monitor memory usage with large PDF collections

### CPU Optimization
- PyTorch is configured for CPU-only execution
- Thread pools optimize I/O-bound operations
- Process pools handle CPU-intensive PDF parsing

### Model Loading
- Models are cached after first load
- Consider warm-up strategies for production deployments
- Use local model storage for offline execution

## Troubleshooting Common Issues

### Model Download Issues
- Ensure models are available in the `models/` directory
- Check internet connectivity for first-time model downloads
- Verify sentence-transformers compatibility

### PDF Processing Errors
- Handle corrupted or password-protected PDFs gracefully
- Use PyMuPDF error handling patterns
- Log processing failures for debugging

### Memory Errors
- Reduce batch sizes for embedding operations
- Monitor multiprocessing memory usage
- Consider processing PDFs sequentially for large collections

This development setup ensures GitHub Copilot has comprehensive context about the document intelligence system, enabling more accurate and helpful code suggestions throughout the development process.