import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types



def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate content using Gemini API")
    parser.add_argument("user_prompt", type=str, help="The prompt to generate content for")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Load environment variables from .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY is not set in environment variables.")
    
    # Initialize the Gemini API client
    client = genai.Client(api_key=api_key)  
    # Prepare the message content
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print("User prompt:", {args.user_prompt})

    generate_content(client, messages, args.verbose)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
    )
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()