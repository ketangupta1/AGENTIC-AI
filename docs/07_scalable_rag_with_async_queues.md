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

### Asynchronous message enqueue with fastAPI
- create an fastAPI app, create server.py for routes and main.py.
- write a post API which will take user query in the request, and take the processor process_request.
- Then take the user_query in process_request and enqueue the process.
- you will get the job in return take that job and query the redis for the result.
- Run it: python3 -m 07_rag_queue.main

### FastAPI polling and dequeueing message from async queue
- create a new route job-status which will take job_id and send the result whatever processed.

### Running and scaling worker nodes for background processing
- In this we will know how to run processor function in the background.
- Open a new terminal and here we have to run worker. We have created worker file.
- command to run worker: rq worker
- I can run multiple worker as well, open new terminal and run command: rq worker.
- Now you can fire multiple query and your multiple worker will work.