from langgraph.graph import StateGraph,START,END
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import add_messages

class ChatState(TypedDict):
    message: Annotated[list[BaseMessage],add_messages]
    
    
load_dotenv()
llm=ChatCohere(model="command-r-plus-08-2024")


def Chat_node(state:ChatState)->dict:   
    message=state["message"]
    response=llm.invoke(message)
    return {"message":[response]}


checkpointer=MemorySaver()

graph=StateGraph(ChatState)

graph.add_node("chat_node",Chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot=graph.compile(checkpointer=checkpointer)


#for streaming we need this


# for message_chunk,metadata in chatbot.stream(
#     {"message":[HumanMessage(content="What is the recepi to make pasta?")]},
#     config={"configurable":{"thread_id":"thread_1"}},
#     stream_mode="messages"
# ):
#     if message_chunk.content:
#         print(message_chunk.content,end=" ",flush=True)    