import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Get token with error handling
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not token:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in .env file")

# Initialize client with correct parameters
client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=token
)

def get_response(user_input):
    try:
        # Format the prompt properly
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
        
        # Convert messages to proper format for text generation
        prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}\nAssistant:"
        
        response = client.text_generation(
            prompt,
            max_new_tokens=250,
            temperature=0.7,
            do_sample=True,
        )
        
        return response.strip()
        
    except Exception as e:
        return f"I'm having trouble connecting. Error: {str(e)}"