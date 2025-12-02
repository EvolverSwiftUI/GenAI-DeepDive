from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano")

response = llm.invoke("what is the capital of France?")

print(response.content)