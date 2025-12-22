import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None: 
        raise RuntimeError("api key is not set or hasn't been loaded properly. Please check .env file.")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages
    )
    if response.usage_metadata == None: 
        raise RuntimeError("usage metadata returned as none, API request most likely failed.")
    
    tokens_sent = response.usage_metadata.prompt_token_count
    tokens_response = response.usage_metadata.candidates_token_count

    print(f"Prompt tokens: {tokens_sent}")
    print(f"Response tokens: {tokens_response}")

    print(f"{response.text}")



if __name__ == "__main__":
    main()
