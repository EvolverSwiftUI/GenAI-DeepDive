from langchain_aws import ChatBedrockConverse
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv  

load_dotenv()

# initialize the AWS Bedrock LLM
llm = ChatBedrockConverse(
    model_id="openai.gpt-oss-120b-1:0",
    region_name="ap-south-1",
)

prompt = PromptTemplate.from_template(
    "What is the capital of {country}?"
)   

chain = prompt | llm  # LCEL

response = chain.invoke({'country': 'France'})

print(response.content)
