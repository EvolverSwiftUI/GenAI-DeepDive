# NSR-GEN-AI: Generative AI Applied Practice

A comprehensive collection of generative AI demos and applications exploring multiple LLM platforms, frameworks, and deployment strategies.

## 📋 Project Overview

This project demonstrates practical implementations of generative AI using various platforms including OpenAI, Google Gemini, HuggingFace, Ollama, AWS, and Azure. It includes backend services, chatbot implementations, prompt templating, vector embeddings for semantic search, and web UI demos using Streamlit.

## 🛠️ Technology Stack

### Core Dependencies
- **LLM Platforms**: 
  - OpenAI (GPT models)
  - Google Generative AI (Gemini)
  - HuggingFace (Transformers)
  - Ollama (Local LLMs)

- **Frameworks**:
  - LangChain (LLM orchestration and prompting)
  - Streamlit (Web UI framework)
  - LangSmith (LLM monitoring and debugging)

- **ML Libraries**:
  - PyTorch (Deep learning)
  - Transformers (Pre-trained models)

- **Utilities**:
  - python-dotenv (Environment configuration)

## 📁 Project Structure

### Core Files

| File | Purpose |
|------|---------|
| `backend.py` | Backend service for finding professional achievements using LLMs |
| `ui.py` | UI component definitions |
| `requirements.txt` | Python dependencies |

### Chatbot Implementations

| File | Purpose |
|------|---------|
| `chatbot-v1-prompt-template.py` | Basic chatbot with prompt templates |
| `chatbot-v2-chat-template.py` | Enhanced chatbot with chat templates |
| `prompt_template.py` | Reusable prompt template utilities |

### LLM Platform Demos

| File | Purpose |
|------|---------|
| `openai_demo.py` | OpenAI API demonstrations |
| `openai-langchain-demo.py` | OpenAI with LangChain framework |
| `openai-langchain-prompt-template.py` | OpenAI with advanced prompt templating |
| `gemini-2.5-pro-demo.py` | Google Gemini 2.5 Pro API usage |
| `gemini-2.5-pro-demo.ipynb` | Jupyter notebook for Gemini demos |
| `gemini-2.5-pro-langchain-demo.py` | Gemini with LangChain integration |
| `huggingface_demo.py` | HuggingFace model demonstrations |
| `huggingface_local_demo.py` | Local HuggingFace model inference |
| `ollama-llama3.2-demo.py` | Local Ollama with Llama 3.2 model |

### Cloud Platform Integrations

| File | Purpose |
|------|---------|
| `aws-demo.py` | AWS AI/ML services demonstrations |
| `azure-demo.py` | Azure OpenAI API demonstrations |
| `azure-langchain-demo.py` | Azure OpenAI with LangChain integration |

### Vector Embeddings & Semantic Search

| File | Purpose |
|------|---------|
| `1_embedding_openai_query.py` | Generate embeddings using OpenAI API |
| `2_embedding_openai_docs.py` | Create embeddings for document processing |
| `3_embedding_ollama_query.py` | Local embeddings using Ollama |
| `4_embedding_similarity_search.py` | Semantic similarity search implementation |

### Utilities & Learning

| File | Purpose |
|------|---------|
| `python-syntax-quick-demo.py` | Quick Python syntax examples and best practices |
| `langchain_with_memory.py` | LangChain chat example with memory enabled |
| `langchain_without_memory.py` | LangChain chat example without memory |
| `rag-langchain-ollama.py` | Retrieval-Augmented Generation (RAG) example using LangChain + Ollama |

### Web UI

| File | Purpose |
|------|---------|
| `streamlit-demo-001.py` | Streamlit web application demo |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip or conda for package management
- API keys for OpenAI and Google Generative AI (if using cloud services)
- Ollama installed locally (for local LLM demos)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/EvolverSwiftUI/GenAI-DeepDive.git
   cd GenAI-DeepDive
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root with your API keys:
   ```bash
   OPENAI_API_KEY=your_openai_key_here
   GOOGLE_API_KEY=your_google_key_here
   ```

## 📚 Usage Examples

### Running the Streamlit Web App
```bash
streamlit run streamlit-demo-001.py
```

### OpenAI Demo
```bash
python openai_demo.py
```

### Google Gemini Demo
```bash
python gemini-2.5-pro-demo.py
```

### Local HuggingFace Model
```bash
python huggingface_local_demo.py
```

### Ollama Local LLM
```bash
python ollama-llama3.2-demo.py
```

### AWS AI/ML Services
```bash
python aws-demo.py
```

### Azure OpenAI
```bash
python azure-demo.py
```

### Azure OpenAI with LangChain
```bash
python azure-langchain-demo.py
```

### Python Syntax Quick Reference
```bash
python python-syntax-quick-demo.py
```

### Embedding Demos

**OpenAI Embeddings**
```bash
python 1_embedding_openai_query.py
python 2_embedding_openai_docs.py
```

**Ollama Local Embeddings**
```bash
python 3_embedding_ollama_query.py
```

**Semantic Similarity Search**
```bash
python 4_embedding_similarity_search.py
```

### LangChain & RAG Demos

```bash
python langchain_with_memory.py
python langchain_without_memory.py
python rag-langchain-ollama.py
```

### About `rag-langchain-ollama.py`

This script demonstrates a Retrieval-Augmented Generation (RAG) workflow using LangChain components and Ollama models.

- **Purpose**: Ingest a PDF, split it into chunks, create vector embeddings, store them in a Chroma vector DB, retrieve the most relevant chunks for a user query, and generate an answer using an Ollama LLM constrained to the retrieved context.
- **Config (edit in file)**:
   - `PDF_PATH` — path to the input PDF (default: `./docs/myfile.pdf`)
   - `CHROMA_DIR` — Chroma DB directory (default: `./my_chroma_db`)
   - `EMBED_MODEL` — embedding model (default: `granite-embedding:latest`)
   - `LLM_MODEL` — LLM model for generation (default: `llama3.2:3b`)
   - `CHUNK_SIZE`, `CHUNK_OVERLAP` — control text chunking behavior
- **How it works (high-level)**:
   1. Load the PDF using `PyPDFLoader` and split into chunks with `RecursiveCharacterTextSplitter`.
   2. Create embeddings with `OllamaEmbeddings` and add them to a `Chroma` collection.
   3. For each user question, retrieve top-k chunks from Chroma, build a prompt that includes only the retrieved context, and call `ChatOllama` to generate the final answer.
- **Run**:
   1. Ensure Ollama is running and the required models are installed locally (or switch to OpenAI embeddings/LLM by editing the script).
   2. Place your PDF at `PDF_PATH` or update the constant.
   3. Run:
       ```bash
       python rag-langchain-ollama.py
       ```
   4. Ask questions at the prompt and type `exit` to quit.
- **Notes & tips**:
   - Persist embeddings to avoid re-indexing on every run (check `Chroma` persistence options).
   - Reduce `k` or truncate context if you hit token limits with the LLM.
   - If switching to cloud embeddings (OpenAI), enable `load_dotenv()` and set API keys in `.env`.

### Backend Service Example
```python
from backend import find_achievements

# Find achievements for a person
result = find_achievements(
    model_name="gpt-4o-mini",
    person_name="Steve Jobs",
    person_role="CEO of Apple"
)
print(result)
```

## 🔑 Key Features

### 1. **Multi-Platform LLM Support**
   - Seamless integration with OpenAI, Google Gemini, HuggingFace, Ollama, AWS, and Azure
   - Platform-agnostic chat interface

### 2. **Vector Embeddings & Semantic Search**
   - OpenAI and Ollama embedding support
   - Semantic similarity search implementations
   - Document embedding and retrieval

### 3. **Cloud Platform Integrations**
   - AWS AI/ML services demonstrations
   - Azure OpenAI API support
   - Easy switching between cloud providers

### 4. **LangChain Integration & RAG**
   - Prompt templating and management
   - LLM chain orchestration (LCEL - LangChain Expression Language)
   - Structured output formatting
   - Memory-enabled and stateless chat examples (`langchain_with_memory.py`, `langchain_without_memory.py`)
   - Retrieval-Augmented Generation example using LangChain + Ollama (`rag-langchain-ollama.py`)

### 5. **Multiple Chatbot Versions**
   - v1: Basic prompt template implementation
   - v2: Advanced chat template with conversation history

### 6. **Local and Cloud Inference**
   - Cloud-based: OpenAI, Google Gemini, AWS, Azure
   - Local: HuggingFace, Ollama (supports running models locally)

### 7. **Web UI**
   - Streamlit-based interactive web application
   - Real-time chat interface

## 🔒 Security Considerations

- **API Keys**: Store sensitive credentials in `.env` file (included in `.gitignore`)
- **Never commit** API keys or sensitive information to version control
- Use environment variables for all configuration

## 📖 Learning Path

1. Start with `openai_demo.py` for basic API usage
2. Explore `openai-langchain-demo.py` for LangChain patterns
3. Try `gemini-2.5-pro-demo.ipynb` for Jupyter-based learning
4. Move to `streamlit-demo-001.py` for web UI development
5. Experiment with local models using `huggingface_local_demo.py` and `ollama-llama3.2-demo.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug reports and feature suggestions.

## 📝 License

This project is part of the GenAI-DeepDive repository by EvolverSwiftUI.

## 🔗 Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Google Generative AI Documentation](https://ai.google.dev)
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai)
- [AWS AI/ML Services](https://aws.amazon.com/machine-learning)
- [LangChain Documentation](https://python.langchain.com)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers)
- [Ollama](https://ollama.ai)
- [Streamlit Documentation](https://docs.streamlit.io)

## ❓ FAQ

**Q: Do I need all API keys to run the project?**
A: No, you can run specific demos based on which services you want to use. Use local models (HuggingFace, Ollama) if you don't have API keys.

**Q: Can I run models locally?**
A: Yes! Use `huggingface_local_demo.py` or `ollama-llama3.2-demo.py` for local inference without API keys.

**Q: How do I add a new LLM platform?**
A: Follow the pattern in existing demo files and create a new file under the appropriate category. Update `backend.py` if needed for new model support.

**Q: What's the difference between chatbot v1 and v2?**
A: v1 uses basic prompt templates, while v2 implements more advanced chat templates with better conversation management.

---

**Last Updated**: December 13, 2025  
**Repository**: [GenAI-DeepDive](https://github.com/EvolverSwiftUI/GenAI-DeepDive)
