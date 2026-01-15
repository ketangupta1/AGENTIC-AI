## 🚀 Scalable RAG with async queues and distributed workers

### Sync vs. async
- As we build RAG in previous lesson the limitation for that was we are doing synchronous call the user has to wait till their query is not processed successfully.
- So in this section we will build async process so that the jobs can run in background.

### Introduction to queues system design for async process
- We will use queue for background task.
- we will push the task to queue and there will be consumer/processor that will take the task one by one and executes and return the results.

### Python RQ setup distributed systems
- We will use python RQ here for the computation. This uses redis in the backend.
- Redis open source licence has been revoked so we will use valkey which is the dropin replacement for redis.
- We need vector DB as that is already running from previous lesson.
- Add the details of valkey in docker compose and run with (docker compose up -d).

### Setting up redis and valkey with docker
- Install RQ: pip install rq.
- cretae client folder all clients will be there.
- create queues folder where we will write the queue.
- create rq_client.py file and setup queue in that file.

### worker orchestration with python RQ
- create a worker.py file for writing worker function.
- Intantiate vector embedding, openai and vector_store client and make the connection.
- Create a process_query function and write all the logics for similarity search and sending query to the OpenAI.
- We will create a fastAPI route and that will take user_query in the request and then it will enqueue that message in the queue.
- Processor function that we built now will take the messsage from queue and process the query and store the data in the redis.
- After that we will create one more route that will fetch the result from the redis and show.

### FastAPI endpoints setup for chat queue
- Install fastapi standard. (python -m pip install fastapi uvicorn[standard])


### 🧩 Architecture Overview
**Indexing of PDF**

PDF → Text → Chunks → Embeddings → Vector Database (Qdrant)

**Retreival and user question answer**

User Question → Embedding → Vector Search → LLM → Answer

---

Steps to run qdrant DB in docker. create docker-compose.yml file and then run command: docker compose up. It will start running the qdrant vector db in docker. If you will close the terminal (clrl+c) it will stop the DB. SO run in detached mode: docker compose up -d

---
