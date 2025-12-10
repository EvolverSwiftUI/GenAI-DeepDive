from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimension=32)  # default dimension is 3072

result = embeddings.embed_query("Delhi is the capital of India.")

print(str(result))  # Print the embedding result

