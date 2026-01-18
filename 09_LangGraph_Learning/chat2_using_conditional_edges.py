from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Optional, Literal
from openai import OpenAI
from langgraph.graph import StateGraph, START, END

load_dotenv()

openai_client = OpenAI()

class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]

def chatbot(state: State):
    print("Chatbot Node", state)
    response = openai_client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "user", "content": state.get("user_query")}
        ]
    )

    state["llm_output"] = response.choices[0].message.content
    return state

def evaluate_response(state: State) -> Literal["chatbot_gemini", "end_node"]:
    print("evaluate_response Node", state)
    if False:
        return "end_node"
    return "chatbot_gemini"

def chatbot_gemini(state: State):
    print("chatbot_gemini Node", state)
    response = openai_client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "user", "content": state.get("user_query")}
        ]
    )

    state["llm_output"] = response.choices[0].message.content
    return state

def end_node(state: State):
    print("end_node Node", state)
    return state

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)
graph_builder.add_node("end_node", end_node)


graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)

graph_builder.add_edge("chatbot_gemini", "end_node")
graph_builder.add_edge("end_node", END)

graph = graph_builder.compile()

final_state = graph.invoke(State({"user_query": "Hey what is 2+2?"}))
print(final_state)
