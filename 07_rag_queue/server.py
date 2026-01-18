from fastapi import FastAPI, Query
from dotenv import load_dotenv
from .client.rq_client import queue
from .queues.worker import process_query

load_dotenv()

app = FastAPI()

@app.get('/')
def root():
    return {"status": "server is up and running"}


@app.post('/chat')
def chat(query: str=Query(..., description="The chat query of user")):
    job = queue.enqueue(process_query, query)

    return {"status": "queued", "JobId": job.id}


@app.get('/job-status')
def get_result(job_id: str=Query(..., description="Enter the Job Id to know the result")):
    job = queue.fetch_job(job_id=job_id)
    result =  job.return_value()
    return {"result": result}