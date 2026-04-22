SYSTEM_PROMPT = """You are MedBot, a friendly and caring AI health assistant.

Guidelines:
- Be warm, friendly, and easy to understand
- Keep responses short (2-3 sentences)
- NEVER give diagnosis - suggest possible causes only
- Recommend when to see a doctor
- Always include diet tips and lifestyle advice when relevant
- Always remind: "I'm not a doctor. Please consult a healthcare professional."

Emergency alerts - tell user to call 911 IMMEDIATELY if they mention:
- Chest pain + shortness of breath
- Difficulty breathing + sweating
- Sudden numbness or weakness
- Severe bleeding
- Confusion or loss of consciousness
- Coughing blood"""

EMERGENCY_KEYWORDS = ["chest pain", "difficulty breathing", "can't breathe", "shortness of breath", 
                      "severe bleeding", "unconscious", "numbness", "weakness", "coughing blood",
                      "suicide", "overdose", "stroke", "heart attack"]

QUICK_SYMPTOMS = {
    "🤕 Headache": "headache",
    "🤒 Fever": "fever",
    "🤧 Cough": "cough",
    "🤢 Nausea": "nausea",
    "💫 Dizziness": "dizziness",
    "😴 Fatigue": "fatigue",
    "🤕 Stomach Pain": "stomach pain",
    "💉 Chest Pain": "chest pain"
}

WIZARD_QUESTIONS = [
    {"key": "duration", "question": "How long have you had these symptoms?", "options": ["Just started", "Few hours", "1-3 days", "More than a week"]},
    {"key": "severity", "question": "How bad is the pain/discomfort?", "options": ["Mild", "Moderate", "Severe"]},
    {"key": "location", "question": "Where does it hurt?", "options": ["Head", "Chest", "Stomach", "Back", "Joints"]},
]
