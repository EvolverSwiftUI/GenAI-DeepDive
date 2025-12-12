# IMPORTS
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings

# from langchain_openai import ChatOpenAI
# from langchain_openai import OpenAIEmbeddings

from langchain_core.prompts import ChatPromptTemplate

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_chroma import Chroma

from dotenv import load_dotenv

# load_dotenv()


# CONFIG
PDF_PATH = "./docs/myfile.pdf"
CHROMA_DIR = "./my_chroma_db"

EMBED_MODEL = "granite-embedding:latest"
LLM_MODEL = "llama3.2:3b"

# EMBED_MODEL = "text-embedding-3-large"
# LLM_MODEL = "gpt-5-nano"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


# LOAD PDF
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

print(f"Documents Loaded: {len(docs)}")
print(docs[0].page_content)
print(docs[0].metadata)


# CHUNK
splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)
chunks = splitter.split_documents(docs)
print(f"Chunks Created: {len(chunks)}")
print(chunks[0])


# Vector DB with granite Embeddings
embeddings = OllamaEmbeddings(model=EMBED_MODEL)
# embeddings = OpenAIEmbeddings(model=EMBED_MODEL)

vector_db = Chroma(
    collection_name="pdf_collection",
    embedding_function=embeddings,
    persist_directory=CHROMA_DIR
)

vector_db.add_documents(chunks)


# LLM
llm = ChatOllama(model=LLM_MODEL)
# llm = ChatOpenAI(model=LLM_MODEL)


# PROMPT
prompt = ChatPromptTemplate.from_template(
    '''
    Use only the cotext below to answer the question.

    Context:
    {context}

    Question:
    {question}
    '''
)

# FINAL RAG FUNCTION (manual RAG)
def rag(question):
    #1 retrieve top chunks from vector DB
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(question)

    #2 combine retrieved chunks
    context = "\n\n".join([doc.page_content for doc in docs])

    #3 create the final prompt
    final_prompt = prompt.invoke({"context": context, "question": question})

    #4 send to llm for final answer
    response = llm.invoke(final_prompt)

    return response.content


# CHAT LOOP

while True:
    user_question = input("You: ")
    if user_question.lower() == 'exit':
        break

    answer = rag(user_question)
    print(f"Answer: {answer}\n")