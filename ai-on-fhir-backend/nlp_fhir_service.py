import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def parse_query(text):
    doc = nlp(text)
    entities = {
        "age_gt": None,
        "condition": None
    }

    # Extract age
    for token in doc:
        if token.like_num and token.head.text.lower() in ["over", "older", "above", "than"]:
            try:
                entities["age_gt"] = int(token.text)
            except ValueError:
                continue

    # Extract condition
    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.lower()
        if "diabet" in chunk_text:
            entities["condition"] = "diabetes"
        elif "hypertens" in chunk_text:
            entities["condition"] = "hypertension"
        elif "asthma" in chunk_text:
            entities["condition"] = "asthma"

    return entities

def simulate_fhir_request(parsed_entities):
    return {
        "resourceType": "Patient",
        "criteria": parsed_entities
    }

# Run sample queries
if __name__ == "__main__":
    sample_queries = [
        "Show me all diabetic patients over 50",
        "List patients with hypertension above 60",
        "Find asthma patients older than 40",
        "Patients over 65 with diabetes",
        "Hypertensive patients older than 55"
    ]

    for query in sample_queries:
        print(f"\nQuery: {query}")
        parsed = parse_query(query)
        fhir_request = simulate_fhir_request(parsed)
        print("Parsed Entities:", parsed)
        print("FHIR Request:", fhir_request)
