# AI on FHIR – Backend NLP Service

This Python-based backend service accepts natural language healthcare queries (e.g., “Show me all diabetic patients over 50”) and simulates FHIR-compliant API requests by extracting relevant filters like age and medical condition using spaCy.

## Project Files

- `nlp_fhir_service.py` – Core script to parse natural language queries and generate FHIR-like output.
- `sample_queries.json` – Sample input/output showing extracted filters and simulated FHIR API requests.
- `requirements.txt` – Dependency list for running the project.
- `README.md` – This documentation file.

## How to Run

1. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install spacy
   python -m spacy download en_core_web_sm
   ```

3. **Run the service script:**
   ```bash
   python nlp_fhir_service.py
   ```

You’ll see parsed output and simulated FHIR requests for a set of sample queries printed in the terminal.

## Sample Query Example

**Input:**
```
Show me all diabetic patients over 50
```

**Parsed Entities:**
```json
{
  "age_gt": 50,
  "condition": "diabetes"
}
```

**Simulated FHIR Request:**
```json
{
  "resourceType": "Patient",
  "criteria": {
    "age_gt": 50,
    "condition": "diabetes"
  }
}
```

More examples are available in `sample_queries.json`.

## Requirements

- Python 3.8 or higher
- spaCy
- spaCy English model: `en_core_web_sm`

## Notes

- The system currently supports:
  - Age filters using keywords like "over", "older than", "above"
  - Conditions: diabetes, hypertension, asthma
- You can easily extend the system to support additional filters such as gender, medications, or lab observations.
