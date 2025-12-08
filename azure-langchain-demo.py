from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# initialize the Azure OpenAI LLM
llm = AzureChatOpenAI(
    deployment_name="gpt-5-nano",
    model="gpt-5-nano",
)

prompt = PromptTemplate.from_template(
    "What is the capital of {country}?"
)

chain = prompt | llm  # LCEL

response = chain.invoke({'country': 'France'})

print(response.content)


