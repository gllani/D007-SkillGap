import os
import io
import spacy
import pdfplumber
import docx
import re
import ollama
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings

class ResumeParser:
    def __init__(self, resume_file):
        self.resume_file = resume_file
        self.text = self.extract_text()
        self.nlp = spacy.load('en_core_web_sm')
        self.doc = self.nlp(self.text)
        self.details = {
            'name': None,
            'email': None,
            'phone_number': None,
            'skills': [],
            'education': [],
            'experience': []
        }
        self.parse_details()

    def extract_text(self):
        ext = os.path.splitext(self.resume_file)[1].lower()
        text = ""
        if ext == ".pdf":
            with pdfplumber.open(self.resume_file) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
        elif ext in [".doc", ".docx"]:
            doc = docx.Document(self.resume_file)
            text = "\n".join([para.text for para in doc.paragraphs])
        elif ext == ".txt":
            with open(self.resume_file, "r", encoding="utf-8") as file:
                text = file.read()
        return text

    def parse_details(self):
        self.details['name'] = self.extract_name()
        self.details['email'] = self.extract_email()
        self.details['phone_number'] = self.extract_phone()
        self.details['skills'] = self.extract_skills()
        self.details['education'] = self.extract_education()
        self.details['experience'] = self.extract_experience()

    def extract_name(self):
        for ent in self.doc.ents:
            if ent.label_ == "PERSON":
                return ent.text
        return None

    def extract_email(self):
        match = re.search(r"[\w\.-]+@[\w\.-]+", self.text)
        return match.group(0) if match else None

    def extract_phone(self):
        match = re.search(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", self.text)
        return match.group(0) if match else None

    def extract_skills(self):
        tokens = [token.text.lower() for token in self.doc if not token.is_stop and not token.is_punct]
        return list(set(tokens))

    def extract_education(self):
        education_keywords = ["bachelor", "master", "phd", "degree", "university", "college"]
        return [sent.text for sent in self.doc.sents if any(word in sent.text.lower() for word in education_keywords)]

    def extract_experience(self):
        experience_keywords = ["experience", "worked", "internship", "employment", "company"]
        return [sent.text for sent in self.doc.sents if any(word in sent.text.lower() for word in experience_keywords)]

    def get_extracted_data(self):
        return self.details


MODEL = "llama2"
model = Ollama(model=MODEL)
embeddings = OllamaEmbeddings(model=MODEL)

def generate_roadmap_with_llama(skills, education, experience):
    # Convert skills, education, and experience into strings
    skills_str = ", ".join(skills)
    education_str = "; ".join(education)
    experience_str = "; ".join(experience)

    # Define the prompt that we'll send to Llama
    prompt = f"""
Based on the following skills: {', '.join(skills)}, education: {', '.join(education)}, and experience: {', '.join(experience)}, 
generate a personalized career pathway. 
1. Suggest a clear career progression considering the person’s current skillset and experiences.
2. For each step, outline what additional skills or knowledge they need to acquire to progress.
3. Recommend certifications, courses, or practical projects they can focus on at each stage.
4. Provide suggestions for potential career paths, either within the same field or branching out to related fields.
5. For each stage, include timeframes for how long it might take to progress to the next level.
"""



    # Generate response from the Llama model using model.invoke()
    response = model.invoke(prompt)

    # The response will be a string containing the roadmap text
    roadmap = response.strip()  # Remove any extra whitespace or newlines

    return roadmap


# Example Usage
if __name__ == "__main__":
    parser = ResumeParser("jpg2.pdf")  # Provide your resume file here
    extracted_data = parser.get_extracted_data()

    # Pass extracted data (skills, education, and experience) to the roadmap generator
    roadmap = generate_roadmap_with_llama(
        extracted_data['skills'], 
        extracted_data['education'], 
        extracted_data['experience']
    )

    # Output the generated roadmap
    print("Your Personalized Roadmap:")
    print(roadmap)
