from langgraph.graph import StateGraph,START,END
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import add_messages
import sqlite3

class ChatState(TypedDict):
    message: Annotated[list[BaseMessage],add_messages]
    
load_dotenv()
llm=ChatCohere(model="command-r-plus-08-2024")

def Chat_node(state:ChatState)->dict:   
    message=state["message"]
    response=llm.invoke(message)
    return {"message":[response]}


conn=sqlite3.connect(database="chatbot_db",check_same_thread=False)
checkpointer=SqliteSaver(conn=conn)

graph=StateGraph(ChatState)

graph.add_node("chat_node",Chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot=graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    all_thread=set()
    for checkpoint in checkpointer.list(None):
        all_thread.add(checkpoint.config["configurable"]["thread_id"])
    return list(all_thread)


#to check our database

# CONFIG={"configurable":{"thread_id": "thread_1"}}
# response=chatbot.invoke(
#                         {"message":[HumanMessage(content="whats my name?")]},
#                         config=CONFIG
#                     )

# print(response)