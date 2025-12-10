from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimension=32)  # default dimension is 3072

documents=[
    "Virat kohli is a great cricketer.",
    "Sachin Tendulkar is a legendary batsman.",
    "Messi is a world-renowned footballer.",
]

query= "tell me about Sachin Tendulkar"

doc_embedding = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

similarity_score = cosine_similarity([query_embedding],doc_embedding)

print("Query:",query)
print("Similarity Score:",similarity_score)
print("Most Similar Document:",documents[similarity_score.argmax()])
print("Most Similar Document Score:",similarity_score.max())

#----------------------------------------------------------------------------------------------------------------------

print("--------------------------------------------------")

similarity_score = euclidean_distances([query_embedding], doc_embedding)
# Note: Lower values = more similar (opposite of cosine)
print("Most Similar Document:", documents[similarity_score.argmin()])
