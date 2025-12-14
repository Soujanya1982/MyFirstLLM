import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

def get_response(prompt: str) -> str:
    if not API_KEY:
        # Mock response if no key yet
        return f"[MOCK] You asked: '{prompt}'. Add OPENAI_API_KEY in .env to call a real model."
    # Real call placeholder: Replace with actual OpenAI client usage when ready.
    # For example, once configured, you'd use the OpenAI Python client to create a response.
    return "[Placeholder] Real LLM call would happen here once the client is set up."

if __name__ == "__main__":
    print(get_response("Say hello in one sentence."))
