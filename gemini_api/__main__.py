#!/usr/bin/env python
from google import genai
from google.genai import types


api_key = "YOUR_API_KEY"

def send_gemini(prompt_text):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt_text,
        config=types.GenerateContentConfig(
            system_instruction="You are a professional.",
            max_output_tokens=10
        )
    )
    print(response.text)


def send_gemini_with_search(prompt_text):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt_text,
        config=types.GenerateContentConfig(
            system_instruction="You are a professional.",
            max_output_tokens=200,
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                )
            ]
        )
    )
    print(response.text)


def get_text_embedding(prompt_text):
    client = genai.Client(api_key=api_key)

    response = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents=prompt_text,
    )
    print(response.embeddings)


def main():
    send_gemini("Hello.")
    send_gemini_with_search("Summarize this: https://ai.google.dev/gemini-api/docs?hl=ja")
    get_text_embedding("What is the meaning of life?")


if __name__ == "__main__":
    main()

