from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()
# Initialize the chatbot model
llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)

class State(TypedDict):
    # This will append message to the current list
    messages: Annotated[list, add_messages]

def chatBot(state: State):
    print("\n\nThis is my Chat Bot Node", state)
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}

def sampleNode(state: State):
    print("\n\nThis is my Sample Bot Node", state)
    return {"messages": ["Sample message appended"]}

graph_builder = StateGraph(State)


# ChatBot is the name we have given for this node and chatBot is the actual node
graph_builder.add_node("ChatBot", chatBot)
graph_builder.add_node("SampleNode", sampleNode)


# (START) -> chatbot -> samplenode -> (END) 
# START and END is two special type of edges provided by langgraph which tells us where to start and where to end.
graph_builder.add_edge(START, "ChatBot")
graph_builder.add_edge("ChatBot", "SampleNode")
graph_builder.add_edge("SampleNode", END)


# Now compile the graph you will get your graph in return
graph = graph_builder.compile()


# Now run the graph by invoking it, when you invoke the graph you need to pass the initial state.
# Here i am pasiing my initial state as {"messages": ["Hi my name is Ketan!"]} and we will get updated_state in the response.
updated_state = graph.invoke(State({"messages": ["Hi my name is Ketan!"]}))

print("\n\nupdate_state", updated_state)




# state = { messages: ["Hey there"] }
# node runs: chatbot(state: ["Hey There"]) -> ["Hi, This is a message from ChatBot Node"]
# state = { "messages": ["Hey there", "Hi, This is a message from ChatBot Node"]  }


'''
| Line                | Purpose                                 |
| ------------------- | --------------------------------------- |
| `TypedDict`         | Defines a structured state dictionary   |
| `Annotated`         | Adds metadata to a type                 |
| `add_messages`      | Appends messages instead of overwriting |
| `State`             | Defines the graph’s state schema        |
| `StateGraph(State)` | Creates a graph with that state         |

'''