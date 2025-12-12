from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# 1. Model
model = ChatOllama(model="phi3:3.8b")

# 2. Prompt
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

# 3. Memory store
history_store = {}

def get_session_history(session_id: str):
    if session_id not in history_store:
        history_store[session_id] = InMemoryChatMessageHistory()
    return history_store[session_id]

# 4. Runnable chain
runnable = prompt | model

chain = RunnableWithMessageHistory(
    runnable=runnable,
    get_session_history=get_session_history,  # MUST BE THIS NAME EXACTLY
    input_messages_key="input",
    history_messages_key="history",
)

# 5. Test
response1 = chain.invoke(
    {"input": "My name is Siva."},
    config={"session_id": "sess1"}
)
print("Response 1:", response1.content)

response2 = chain.invoke(
    {"input": "What is my name?"},
    config={"session_id": "sess1"}
)
print("Response 2:", response2.content)
