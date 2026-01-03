import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions, call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None: 
        raise RuntimeError("api key is not set or hasn't been loaded properly. Please check .env file.")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose",action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    client = genai.Client(api_key=api_key)


    for _ in range(20): 
        if not generate_model_content(client, messages, args.verbose): 
            break
    else:
        print("LLM hasn't come to final conclusion within specified maximum iterations")
        exit(1)
    

def generate_model_content(client, messages, verbose):
    response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt),
        )
    if len(response.candidates) > 0: 
        for candidate in response.candidates: 
            messages.append(candidate.content)
    
    if response.usage_metadata == None: 
        raise RuntimeError("usage metadata returned as none, API request most likely failed.")
    
    tokens_sent = response.usage_metadata.prompt_token_count
    tokens_response = response.usage_metadata.candidates_token_count

    if verbose:
        print(f"Prompt tokens: {tokens_sent}")
        print(f"Response tokens: {tokens_response}")

    if response.function_calls == None: 
        print(f"{response.text}")
        return False
    list_func_results = []
    for obj in response.function_calls:
        function_call_result = call_function(obj, verbose)
        if len(function_call_result.parts) == 0: 
            raise Exception(f"Error content object parts list is empty")
        elif function_call_result.parts[0].function_response is None: 
            raise Exception(f"Error first item in list of parts is None")
        elif function_call_result.parts[0].function_response.response is None: 
            raise Exception(f"Error: response is None")
        else: 
            list_func_results.append(function_call_result.parts[0])
            if verbose: 
                print(f" -> {function_call_result.parts[0].function_response.response}")
    
    
    if len(list_func_results) > 0: 
        messages.append(types.Content(role="user", parts=list_func_results))
    
    return True

if __name__ == "__main__":
    main()
