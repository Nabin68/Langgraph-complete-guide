import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid 

#**************************************** Utility Functions ****************************************************
def generate_thread_id():
    thread_id=str(uuid.uuid4())  # Convert to string
    return thread_id

def reset_chat():
    thread_id=generate_thread_id()
    st.session_state["thread_id"]=thread_id
    add_thread(st.session_state["thread_id"])
    st.session_state["message_history"]=[]

def add_thread(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)

def load_conversation(thread_id):
    state = chatbot.get_state(config={"configurable":{"thread_id":thread_id}})
    # Check if state.values exists and has message (singular, not messages)
    if state.values and "message" in state.values:
        return state.values["message"]
    return []  # Return empty list if no messages exist

#****************************************** Session Setup ******************************************************
if "message_history" not in st.session_state:
    st.session_state["message_history"]=[]

if "thread_id" not in st.session_state:
    st.session_state["thread_id"]=generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"]=[]
    
add_thread(st.session_state["thread_id"])

#******************************************* Sidebar UI ********************************************************
st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()
    st.rerun()  # Force rerun to clear the UI

st.sidebar.header("My Conversations")
for thread_id in st.session_state["chat_threads"][::-1]:
    if st.sidebar.button(str(thread_id), key=f"thread_{thread_id}"):  # Add unique key
        st.session_state["thread_id"]=thread_id
        messages=load_conversation(thread_id)
        temp_messages=[]
        for msg in messages:
            if isinstance(msg,HumanMessage):
                role="user"
            else:
                role="assistant"
            temp_messages.append({"role":role,"content":msg.content})
        st.session_state["message_history"]=temp_messages
        st.rerun()  # Force rerun to display loaded messages

#******************************************** Main UI ***********************************************************
#loading the conversation history
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input=st.chat_input("Type here...")

if user_input:
    st.session_state["message_history"].append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.text(user_input)
    
    CONFIG={"configurable":{"thread_id": st.session_state["thread_id"]}}
    
    with st.chat_message("assistant"):
        ai_message=st.write_stream(
            message_chunk.content for message_chunk,metadata in chatbot.stream(
                {"message":[HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages"
            )
        )
    st.session_state["message_history"].append({"role":"assistant","content":ai_message})
    
    
    
#claude chat link if required:
# https://claude.ai/share/ed158992-69c9-4b16-97de-7ca89ece5868

# #detailed workflow

# """
# # **LangGraph Chatbot - Essential Notes**

# ---

# ## **1. Two Storage Systems**

# | Storage | What It Stores | Purpose |
# |---------|----------------|---------|
# | **Backend (MemorySaver)** | ALL messages for ALL threads | LLM context |
# | **Frontend (session_state)** | CURRENT thread messages only | UI display |

# **Key Point:** Backend stores everything; Frontend loads on-demand

# ---

# ## **2. Session State Structure**

# ```python
# st.session_state = {
#     "thread_id": "abc-123",           # Current active thread
#     "chat_threads": ["abc", "def"],   # All thread IDs
#     "message_history": [...]          # Current thread messages only
# }
# ```

# ---

# ## **3. Main Workflows**

# ### **Send Message Flow**
# ```
# User types → chatbot.stream(message, thread_id)
#           → Backend auto-saves to MemorySaver
#           → Frontend appends to session_state["message_history"]
# ```

# ### **New Chat Flow**
# ```
# Click "New Chat" → Generate new thread_id
#                  → Clear message_history
#                  → Add to chat_threads list
# ```

# ### **Switch Thread Flow**
# ```
# Click thread button → load_conversation(thread_id) from backend
#                     → Convert format (HumanMessage → dict)
#                     → Replace session_state["message_history"]
#                     → Update session_state["thread_id"]
#                     → st.rerun()
# ```

# ---

# ## **4. Key Functions**

# **`load_conversation(thread_id)`**
# - Fetches messages from backend
# - Returns list of messages for that thread

# **`reset_chat()`**
# - Creates new thread
# - Clears current messages

# **`add_thread(thread_id)`**
# - Adds thread to sidebar list

# ---

# ## **5. Config Parameter**

# ```python
# CONFIG = {"configurable": {"thread_id": "thread-001"}}
# ```
# **Purpose:** Tells backend which conversation to load/save

# ---

# ## **6. Important Points**

# ✅ **Backend auto-saves** - MemorySaver handles storage automatically  
# ✅ **session_state is temporary** - Only for current UI display  
# ✅ **Switch threads = load from backend** - Not stored in session_state  
# ✅ **One active thread** - session_state shows only current thread  
# ✅ **add_messages accumulates** - Conversation history builds up  

# ---

# ## **7. Common Confusion**

# ❌ **Wrong:** session_state stores all threads  
# ✅ **Correct:** session_state stores CURRENT thread only

# ❌ **Wrong:** Need to manually save to backend  
# ✅ **Correct:** Backend auto-saves with checkpointer

# ---

# **End** 📝
# """