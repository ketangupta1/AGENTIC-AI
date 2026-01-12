## 🚀 Building chat with pdf project using RAG

### 🧩 Architecture Overview
**Indexing of PDF**
PDF → Text → Chunks → Embeddings → Vector Database (Qdrant)

**Retreival and user question answer**
User Question → Embedding → Vector Search → LLM → Answer

---

Steps to run qdrant DB in docker. create docker-compose.yml file and then run command: docker compose up. It will start running the qdrant vector db in docker. If you will close the terminal (clrl+c) it will stop the DB. SO run in detached mode: docker compose up -d

---
