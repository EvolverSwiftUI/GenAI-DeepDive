from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

prompt = PromptTemplate.from_template("Tell me the key achivements of {name} in 4 bullet points.")

chain = prompt | model #LCEL ==> LangChain Expression Langugage

response = chain.invoke({"name" : "Nathuram Ghadse"})

print(response.content)