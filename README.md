# Coding Interview Practice

This repository contains code and resources for practicing coding interview questions, including:
- LeetCode problems
- Algorithm implementations
- Data structure examples
- Coding interview questions

## Setup

### Using Docker (Recommended)

A Dockerfile is provided for easy setup:

```bash
# Build the Docker image
docker build -t coding-interview .

# Run the container with volume mounting for persistent data
docker run -p 8888:8888 -v $(pwd):/app coding-interview
```

After running the container, access Jupyter Notebook by navigating to http://localhost:8888 in your browser. The access token will be displayed in the console output.

### Manual Setup

If you prefer not to use Docker, you can set up the environment manually:

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Jupyter Notebook
jupyter notebook
```

## Contents

- `algorithms/`: Implementation of common algorithms
- `interview_questions/`: Solutions to various interview questions
- `leet_code.py` and `neet_code.py`: Solutions to LeetCode problems
- `tests.py` and `tests.ipynb`: Test files and examples
