# Gemini API

This Python script interacts with Google's Generative AI API using the Gemini 1.5 Flash model to generate content based on a customizable prompt and parameters.

## Installation

```bash
git clone https://github.com/R-Tatara/gemini-api.git
cd gemini-api
pip install -r requirements.txt
```

## Usage
1. Replace the GOOGLE_API_KEY variable with your own API key from Google.

```Python
GOOGLE_API_KEY = "YOUR_API_KEY"
```

2. Edit the prompt variable to change the input question or request.

```Python
prompt = 'What is Google. Answer shortly.'
```

3. Run the script:

```Bash
python -m gemini_api
```