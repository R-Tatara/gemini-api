#!/usr/bin/env python
import time
import google.generativeai as genai


def main():
    GOOGLE_API_KEY = "AIzaSyAMsd0qhUnq8wRp5zQU7OORJaHj_J3x3vY"
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = 'What is Google. Answer shortly.'

    res = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
            max_output_tokens=30,
            temperature=0.1,
        )
    )

    print(res.text)
    print(res.usage_metadata)

    # time.sleep(4)


if __name__ == "__main__":
    main()
