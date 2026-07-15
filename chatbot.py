from model import generate_response

SYSTEM_PROMPT = (
    "You are a medical assistant chatbot. Only answer questions related to "
    "health, symptoms, diseases, medicine, or wellness. "
    "If asked anything unrelated, refuse politely."
)

MEDICAL_KEYWORDS = [
    # general
    "pain", "ache", "hurt", "sick", "illness", "disease", "symptom", "symptoms",
    "health", "medical", "medicine", "treatment", "diagnosis", "doctor", "hospital",
    "clinic", "nurse", "surgery", "prescription", "tablet", "capsule", "dose",
    "injection", "vaccine", "therapy", "checkup", "test", "report", "recovery",
    # body parts
    "stomach", "abdomen", "head", "chest", "back", "throat", "ear", "eye", "nose",
    "tooth", "teeth", "gum", "skin", "joint", "bone", "muscle", "heart", "lung",
    "kidney", "liver", "brain", "spine", "leg", "arm", "hand", "foot", "neck",
    # common symptoms
    "fever", "cough", "cold", "flu", "headache", "migraine", "vomit", "vomiting",
    "nausea", "dizzy", "dizziness", "fatigue", "tired", "weakness", "swelling",
    "rash", "itch", "itchy", "bleeding", "wound", "cut", "burn", "bruise",
    "cramp", "cramps", "diarrhea", "constipation", "gas", "bloating", "acidity",
    "breathless", "breathing", "wheeze", "chills", "sweating", "numbness",
    "tingling", "burning sensation", "sore", "swollen", "infection", "inflammation",
    "allergy", "allergic", "sneeze", "sneezing", "congestion",
    # common diseases
    "diabetes", "sugar", "bp", "blood pressure", "hypertension", "asthma",
    "cancer", "tumor", "arthritis", "obesity", "thyroid", "anemia", "jaundice",
    "malaria", "dengue", "typhoid", "tuberculosis", "tb", "pneumonia",
    "bronchitis", "sinusitis", "migraine", "epilepsy", "stroke", "paralysis",
    "ulcer", "hernia", "piles", "cyst", "fracture", "sprain", "dislocation",
    "covid", "corona", "virus", "bacterial", "fungal", "std", "hiv",
    # wellness/diet
    "diet", "nutrition", "vitamin", "protein", "calorie", "exercise", "sleep",
    "mental health", "stress", "anxiety", "depression", "insomnia",
    "pregnancy", "pregnant", "period", "menstrual", "menstruation"
]

def get_response(user_message: str) -> str:
    if user_message.strip() == "":
        return "Please describe your symptoms."

    lower_msg = user_message.lower()
    is_medical = any(keyword in lower_msg for keyword in MEDICAL_KEYWORDS)

    if not is_medical:
        return "I can only help with medical and health-related questions."

    return generate_response(user_message, SYSTEM_PROMPT)