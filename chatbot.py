import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from prompts import SYSTEM_PROMPT

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def get_response(user_input):
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
                {"role": "user", "content": user_input}
            ],
            max_tokens=200,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Oops! Something went wrong. Please try again. ({str(e)})"
