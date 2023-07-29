import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv

# python-dotenv
__ = load_dotenv(find_dotenv())  # read local .env file

# openai-key

openai.api_key = os.environ['OPENAI_API_KEY']


def get_completion(prompt, model="gpt-3.5-turbo"):
    msgs = [{
        "role": "user",
        "content": prompt
    }]
    res = openai.ChatCompletion.create(
        model=model,
        messages=msgs,
        temperature=0,
    )
    return res.choices[0].message["content"]
