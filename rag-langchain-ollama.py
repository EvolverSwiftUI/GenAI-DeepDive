# IMPORTS
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain.core_prompts import ChatPromptTemplate

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_chroma import Chroma

from dotenv import load_dotenv

load_dotenv()


# CONFIG
PDF_PATH = "./docs/myfile.pdf"
CHROMA_DIR = "./my_chroma_db"

# EMBED_MODEL = "granite-embedding:latest"
# LLM_MODEL = "llama3.2:3b"

EMBED_MODEL = "text-embedding-3-large"
LLM_MODEL = "gpt-5-nano"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


# LOAD PDF
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

print(f"Documents Loaded: {len(docs)}")
print(docs[0].page_content)
print(docs[0].metadata)


# CHUNK

# Vector DB with granite Embeddings

# LLM

# PROMPT

# FINAL RAG FUNCTION

# CHAT LOOP