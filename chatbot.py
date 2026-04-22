import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from prompts import SYSTEM_PROMPT, EMERGENCY_KEYWORDS

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def check_emergency(user_input):
    user_lower = user_input.lower()
    for keyword in EMERGENCY_KEYWORDS:
        if keyword in user_lower:
            return True
    return False

def get_response(user_input, context=""):
    if check_emergency(user_input):
        return """🚨 EMERGENCY ALERT!

Please call 911 or your local emergency number IMMEDIATELY!

Do NOT ignore these symptoms. If you're alone, call for help now.

While waiting for help:
- Stay calm and rest
- Don't drive yourself to the hospital
- If possible, have someone stay with you

I'm not a doctor. Please seek immediate medical attention!"""

    try:
        client = InferenceClient(
            model="HuggingFaceH4/zephyr-7b-beta",
            token=token,
            provider="featherless-ai"
        )
        
        response = client.chat.completions.create(
            model="HuggingFaceH4/zephyr-7b-beta",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input + "\n\n" + context}
            ],
            max_tokens=250,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Oops! Something went wrong. Please try again. ({str(e)})"
