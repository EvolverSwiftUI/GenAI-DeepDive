from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3:3.8b")

response = llm.invoke("My name is Siva.")
print(response.content)

respons2 = llm.invoke(" What is my name?")
print(response2.content)

