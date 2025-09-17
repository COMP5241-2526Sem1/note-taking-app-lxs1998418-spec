# import libraries
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv() # Loads environment variables from .env
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

# A function to call an LLM model and return the response
def call_llm_model(model, messages, temperature=1.0, top_p=1.0):
    client = OpenAI(base_url=endpoint,api_key=token)
    response = client.chat.completions.create(
    messages=messages,
    temperature=temperature, top_p=top_p, model=model)
    return response.choices[0].message.content

# A function to translate to target language
def translate_text(text, target_language):
    messages = [
        {"role": "user", "content": f"Translate the following text to {target_language}: {text}"}
    ]
    response = call_llm_model(model, messages)
    return response

# Run the main function if this script is executed
if __name__ == "__main__":
    sample_text = "Hello, how are you?"
    target_language = "Spanish"
    translated_text = translate_text(sample_text, target_language)
    print(f"Original text: {sample_text}")
    print(f"Translated text: {translated_text}")