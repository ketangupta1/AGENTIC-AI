## 🚀 Building agentic workflow with LangGraph

### Why LangGraph is gamechanger for AI agents
- LangGraph is a stateful, graph-based framework for building reliable, controllable AI agents.
- LangGraph is a framework that models AI agents as explicit state machines (graphs), enabling memory, branching, loops, and human-in-the-loop control.

### The Problem with Traditional Agents

Most traditional agent frameworks (e.g., LangChain agents or naive loops) rely on patterns like:
while True:
    thought → tool → observation → thought → tool
Issues:
    Infinite loops
    No clear control flow
    Hard to debug
    No guaranteed stopping
    State gets messy

### Setting up LangGraph- Installation and environment configuration
- pip install -U langgraph
- In langGraph you have nodes, nodes is nothing but a functions.
- e.g: Lets assume we have one function to take input from user, one function is to get the tool, one function to call OpenAI model, and other is to store something in the DB. So these 4functions are nothing but 4 nodes.
- We have to connect these nodes using edges, which defines a workflow.
- So what happens in langGraph once you build this type of langGraph we create a state.
- state is nothing but a piece of data.
- e.g: State is state={input: str, output: str}
- When you run your graph you give your state as input. graph.run(state)
- Now what happens this state goes to 1st node as an input call it as state 1.
- 1st node will process this input and it returns some output state i.e: state2.
- This state2 will goto node 2 and it returns state3.
- This state3 will goto node 3 for execution and returns output as state4.
- Now state4 will goto node 4 for execution and lets assume it doesn't changes the input state it will return output as it is.
- So state4 will be the final output for our graph. This is the how the langGraph works.
- We initially create the state we add all the data in this. Then all the nodes perform their task, they can read the state, they can modify the state and when the graph execution is done you get the final updates state back. 

### Defining state in langGraph