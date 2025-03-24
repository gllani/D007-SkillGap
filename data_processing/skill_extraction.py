import spacy

def extract_skills_from_text(text: str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    return skills
