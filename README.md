# Document Intelligence Project

This project provides a pipeline for extracting relevant information from PDF documents based on a user-defined persona and task. It leverages advanced techniques for PDF outline extraction, semantic analysis, and hybrid relevance scoring to identify and refine key sections within documents.

## Project Structure

- `main.py`: Orchestrates the entire data processing pipeline.
- `enhanced_pdf_extractor.py`: Handles the extraction of structured outlines from PDF files.
- `semantic_analyzer.py`: Manages the loading of embedding models and performs semantic analysis on text.
- `relevance_scorer.py`: Combines lexical and semantic approaches to rank document sections based on relevance.
- `subsection_extractor.py`: Refines extracted sections by identifying the most relevant three-sentence windows.
- `input/`: Contains input PDF documents and the configuration JSON file.
- `output/`: Stores the processed output JSON file.
- `models/`: Directory for storing pre-trained sentence embedding models.
- `requirements.txt`: Lists all necessary Python dependencies.

## Setup

To set up the project, follow these steps:

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone https://github.com/Polymath-Saksh/Document_Intelligence.git
    cd Document_Intelligence
    ```

2.  **Install dependencies**:
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download the Sentence Transformer Model**:
    The project uses a pre-trained sentence embedding model (e.g., `granite-embedding-107m-multilingual`). This model needs to be placed in the `input/models/models/` directory. You can typically download this model from Hugging Face or similar sources and extract it there.

    The expected path for the model's main directory within the project is `input/models/models/granite-embedding-107m-multilingual/`.

## Usage

To run the document intelligence pipeline, execute the `main.py` script from the project root. You need to provide an input directory containing your PDF files and a configuration file, and an output directory where the results will be saved.

```bash
python main.py <input_directory> <output_directory>
```

**Example:**

```bash
python main.py input/ output/
```

### Input Configuration

The `input_directory` should contain a JSON file (e.g., `challenge1b_input.json`) that specifies the documents to be processed, along with a persona and a job-to-be-done. The structure of this JSON file should be as follows:

```json
{
    "documents": [
      {
        "filename": "document1.pdf"
      },
      {
        "filename": "document2.pdf"
      }
    ],
    "persona": {
      "role": "your_role"
    },
    "job_to_be_done": {
      "task": "your_task_description"
    }
}
```

-   `documents`: A list of dictionaries, each containing the `filename` of a PDF document to be processed. These PDFs should be located in the `input_directory`.
-   `persona.role`: A string describing the role of the user (e.g., "student", "researcher").
-   `job_to_be_done.task`: A string describing the specific task or query the system needs to address (e.g., "find relevant questions for programming languages exam").

### Output

The results will be saved in the specified `output_directory` as a JSON file (e.g., `challenge1b_output.json`). This file will contain metadata about the processing, extracted sections, and refined subsection analysis. 
