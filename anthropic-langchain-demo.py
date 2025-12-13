from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")
response = llm.invoke("What kind of applications I can develop using GenAI?")
print(response.content)

