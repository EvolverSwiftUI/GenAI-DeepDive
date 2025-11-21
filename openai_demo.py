
#!pip3 install openai

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
response = client.responses.create(
    model="gpt-5-nano",
    input="Write a poem on GenAI?"
)

print(response.output_text)