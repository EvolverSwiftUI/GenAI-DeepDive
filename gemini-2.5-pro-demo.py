import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# genai.configure()

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content("What is the capital of India?")

print(response.text)