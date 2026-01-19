## 🚀 Checkpointing Workflows in LangGraph using MongoDB

### What is checkpointing
- So in previous module we have built chat app using LangGraph but when the program runs, its state is being lost. i.e: I am running it 1st time by giving question as "Hi My name is Ketan!" and we got in response from LLM as: "Hi Ketan how can i assist you today?". If i am running it 2nd time by asking question as "What's my name?" It will give answer as "I don't have context of your name".
- This means the state has been lost after program terminate 1st time, 2nd time it doesn't have the context of 1st time's state.
- we can solve this problem using checkpoint.
- Checkpointing in LangGraph means saving the graph’s state after each step (node execution) so it can be: resumed later, replayed, inspected/debugged, shared across sessions or users
- This is especially important for long-running, multi-step, or conversational graphs.

---

### Setting up mongodb with docker for LangGraph checkpoint storage
- Write the docker-compose file for mongodb image pull.
- Run the command: docker compose up -d

---

### Implementing Checkpointer in LangGraph workflow graphs
- pip install -U pymongo langgraph langgraph-checkpoint-mongodb