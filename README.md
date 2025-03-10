# HCC Extraction Project

An automated system for extracting HCC-relevant conditions from clinical progress notes using AI.

## Description

This project implements an AI-based solution that automates the extraction of medical conditions and their associated codes from clinical progress notes, determining which are relevant for HCC (Hierarchical Condition Category). Using Vertex AI Gemini 1.5 Flash and LangGraph, the system transforms a tedious and error-prone process into an efficient workflow, allowing healthcare professionals to focus more on patient care.

## System Architecture

The project follows a layered architecture that clearly separates:

1. **Condition extraction**: Identifies medical conditions and their codes from progress notes
2. **HCC relevance evaluation**: Determines which of the extracted conditions are relevant for HCC
3. **LangGraph orchestration**: Manages the workflow between different components

### Main components:

- `app/main.py`: Main entry point of the application
- `app/agent.py`: Defines the agent configuration
- `app/src/extraction/extractor.py`: Handles condition extraction from notes
- `app/src/evaluation/evaluator.py`: Evaluates the HCC relevance of extracted conditions
- `app/src/utils/`: Contains utilities for data handling, logging, and constants

## Prerequisites
- Poetry for development (optional)
- Docker and Docker Compose
- Google Cloud service account with access to Vertex AI
- Google Cloud credentials file (JSON)

## Configuration

### Google Cloud Credentials

To access Vertex AI Gemini 1.5 Flash, you need to configure a credentials file:

1. Create a service account in Google Cloud Console with access to Vertex AI
2. Generate and download a JSON key file for the service account
3. Place the credentials file in `app/credentials.json`

## Installation and Execution

### Using Docker (recommended)

1. Build and run the Docker container:

```bash
docker-compose up --build
```

This will automatically process all progress notes in `app/data/input/` and save the results in `app/data/output/`.

2. To access the processed results:

```bash
ls -la app/data/output/
```

### Manual Installation (development)

1. Set up the environment using Poetry:

```bash
# Install Poetry if not already installed
pip install poetry

# Install dependencies
poetry install
```

2. Run the application:

```bash
# Using Poetry
poetry run python app/main.py
```

## Usage

### Processing Progress Notes

1. Place clinical progress notes in text format in the `app/data/input/` directory
2. Run the application following the instructions above
3. Review the processed results in `app/data/output/`

### Input/Output Format

- **Input**: Text files with clinical progress notes
- **Output**: Files with extracted conditions, codes, and their HCC relevance

Example output:

```json
Patient Information:
	Name: ROOB, NATHANIAL
	Age: 84
	DOB: 06/17/1940
	Insurance #: 123456789

Medical Conditions:
	HCC Relevant:
	  - Hyperglycemia due to type 2 diabetes mellitus (Code: E11.65)
	  - Chronic obstructive lung disease (Code: J44.9)
	  - Chronic systolic heart failure (Code: I50.22)
	  - Chronic kidney disease stage 4 (Code: N18.4)
	  - Morbid obesity (Code: E66.01)
	HCC Not Relevant:
	  - Gastroesophageal reflux disease (Code: K21.9)
	  - Essential hypertension (Code: I10)

```

## Running the LangGraph Development Web App

To start the LangGraph development interface:

```bash
# Using Poetry
poetry run langgraph dev
```

This will start the web application where you can:

- Visualize the workflow graph
- Test different inputs
- Inspect the state at each step of the process
- Debug the behavior of nodes

## Running Tests

To run the unit tests:

```bash
# Using Poetry
poetry run pytest
```

## Project Structure

```
├── 📄 .gitignore                  # Files and directories ignored by Git
├── 📄 credentials.json            # Google Cloud credentials (do not include in repo)
├── 📁 data                 	   # Input, output, and reference data
│   ├── 📁 input            	   # Progress notes to process
│   ├── 📁 output          		   # Processed results
│   └── 📁 reference       	   	   # Reference data (HCC codes)
├── 📁 src                         # Main application directory
│   ├── 📄 agent.py                # AI agent and Vertex AI configuration
│   ├── 📄 main.py                 # Main entry point
|   ├── 📁 evaluation       	   # HCC relevance evaluation
│   ├── 📁 extraction       	   # Condition extraction
│   ├── 📁 langgraph        	   # LangGraph implementation
│   ├── 📁 models           	   # Models and data structures
│   └── 📁 utils            	   # Utilities and tools
├── 📁 tests                 	   # Unit tests
├── 📄 docker-compose.yaml         # Docker Compose configuration
├── 📄 dockerfile                  # Docker container definition
├── 📄 langgraph.json              # LangGraph configuration
├── 📄 poetry.lock                 # Dependency version lock
├── 📄 pyproject.toml              # Poetry and project configuration
```

## Dockerfile

The Dockerfile is configured to:

1. Build an environment with all necessary dependencies
2. Automatically process all notes in the input directory
3. Store the results in a mounted volume


## Methodology and Approach

### Condition Extraction

The solution specifically looks for the "assessment/plan" section in progress notes, where medical conditions are listed. We use Gemini 1.5 Flash to:

1. Identify and extract this specific section
2. Recognize medical conditions and their associated codes
3. Structure the information

### HCC Relevance Evaluation

The evaluation uses:

1. Reference database of HCC-relevant codes
2. Comparison logic to determine relevance
3. Calculation of confidence scores for each condition
