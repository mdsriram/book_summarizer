import os
import openai
from dotenv import load_dotenv
import src.prompts
from src.pdf_generator import create_pdf

#load the environment variable from .env file
load_dotenv()

#access the key
api_key = os.getenv('MYAPI_KEY')
if not api_key:
    raise ValueError("API key not found. Please set it in the .env file.")

openai.api_key = api_key

#prompts
system_message = src.prompts.system_message
prompt = src.prompts.generate_prompt(book='The Enchanted Realm', title='The Journey of Discovery')

#helper function
def generate_content():
    completion = openai.ChatCompletion.create(
        model ="gpt-4",
        messages = [
            {"role":"system","content":system_message},
            {"role":"user","content":prompt}
        ],
        temperature =0.7,
        max_tokens = 2000
    )
    return completion.choices[0].message['content']

#Generate content
content = generate_content()

#create pdf
create_pdf(content)