<div align="center">

# 🔗 LangGraph Complete Guide

### **Hands-on implementations of LangGraph concepts and workflows**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-green.svg)](https://langchain-ai.github.io/langgraph/)
[![LangChain](https://img.shields.io/badge/LangChain-Enabled-orange.svg)](https://langchain.com/)
[![Cohere](https://img.shields.io/badge/Cohere-LLM-purple.svg)](https://cohere.com/)

*Building graph-based LLM systems, one node at a time*

[📌 What This Covers](#-what-this-repository-covers) • [🧠 Key Concepts](#-key-concepts-practiced) • [📂 Repository Structure](#-repository-structure) • [🚀 Getting Started](#-getting-started)

---

</div>

## 📖 About

This repository contains **structured learning and practical implementations** of LangGraph, focusing on how to build **graph-based LLM systems**, manage state, route tools, and design non-trivial agent workflows.

### 🎯 **The Philosophy**

> **Learn by building, not just reading documentation.**

This is not a tutorial copy or boilerplate repo. Every example here is built from the ground up to understand LangGraph at a **system-design level** — how to think in graphs, control LLM execution, and build extensible agent systems.

---

## 📌 What This Repository Covers

<table>
<tr>
<td width="50%">

### 🏗️ **Core Fundamentals**
- LangGraph basics
- State management using `TypedDict`
- Message reducers (`add_messages`)
- Graph construction using `StateGraph`
- Node definitions and edges

</td>
<td width="50%">

### 🔄 **Workflow Patterns**
- Sequential workflows
- Parallel workflows
- Conditional workflows
- Iterative workflows
- Cyclic execution patterns

</td>
</tr>
<tr>
<td width="50%">

### 🛠️ **Tool Integration**
- Tool integration using `ToolNode`
- Conditional tool routing (`tools_condition`)
- Dynamic tool selection
- Tool-aware reasoning

</td>
<td width="50%">

### 💾 **Memory & Persistence**
- Checkpointing and memory
- In-memory persistence
- SQLite database integration
- Conversation state management

</td>
</tr>
<tr>
<td width="50%">

### ⚡ **Advanced Features**
- Streaming graph execution
- Backend–frontend integration
- Multi-turn conversations
- MCP (Model Context Protocol)

</td>
<td width="50%">

### 🎨 **Real-World Examples**
- Chatbots with memory
- Tool-calling agents
- Database-backed persistence
- LangSmith integration

</td>
</tr>
</table>

---

## 🧠 Key Concepts Practiced

### **Graphs Over Chains**
Designing LLM systems as **directed graphs** instead of linear flows. This enables:
- Dynamic branching based on LLM decisions
- Parallel execution of independent tasks
- Conditional logic and loops
- Better control over complex workflows

### **State-Driven Execution**
Explicit state schema controlling how data flows through nodes:
```python
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    context: str
    user_info: dict
```

### **Tool-Aware Reasoning**
Letting the model decide when tools are required:
- LLM evaluates if a tool is needed
- Graph routes to tool execution
- Results feed back to LLM for synthesis

### **Checkpointed Memory**
Persisting conversation state across executions:
- Thread-based conversations
- Resume interrupted workflows
- Multi-session memory

---

## 🏗️ Typical Graph Structure

Most examples follow this powerful pattern:

```
        START
          ↓
      LLM Node
          ↓
    (Conditional)
       ↙    ↘
  Tool Node  Direct Response
       ↘    ↙
         ↓
     END / Loop
```

### **What This Enables:**

| Feature | Benefit |
|---------|---------|
| **Dynamic Branching** | LLM decides the execution path |
| **Tool Execution** | Automatic tool invocation when needed |
| **Iterative Reasoning** | Loop back for multi-step problems |
| **Conditional Logic** | Different paths for different scenarios |

---

## 📂 Repository Structure

```
langgraph-complete-guide/
│
├── 1.Sequential_workflow/          # Learn sequential graph execution
├── 2.Parallel_workflow/            # Parallel node execution patterns
├── 3.Conditional_workflow/         # Conditional routing and branching
├── 4.Iterative_workflow/           # Loops and iterative reasoning
├── 6.Persistence/                  # In-memory checkpointing
├── 7.ChatBot/                      # Full chatbot implementation
├── 8.SQLite_Database/              # SQLite-backed persistence
├── 9.LangSmith/                    # LangSmith tracing integration
├── 10.Chatbot_tools/               # Chatbots with tool integration
├── 11.Chatbot_with_tools_SQLite/   # Complete chatbot + tools + DB
├── 12.MCP/                         # Model Context Protocol examples
│
├── requirements.txt
├── .env.example
└── README.md
```

Each folder contains **runnable examples** focusing on one concept at a time.

---

## 🗂️ Module Breakdown

### **1. Sequential Workflow** 📝
Learn the basics of LangGraph by building simple sequential flows.
- Define nodes and edges
- Create linear execution paths
- Understand state management

### **2. Parallel Workflow** ⚡
Execute multiple nodes in parallel for efficiency.
- Parallel node execution
- Fan-out and fan-in patterns
- Combining parallel results

### **3. Conditional Workflow** 🔀
Build intelligent routing based on conditions.
- Conditional edges
- Dynamic path selection
- If-else logic in graphs

### **4. Iterative Workflow** 🔄
Implement loops and recursive patterns.
- Loop until condition met
- Iterative problem solving
- Self-correction loops

### **6. Persistence** 💾
Add memory to your graphs with checkpointing.
- In-memory checkpointers
- Save and resume conversations
- Thread-based state management

### **7. ChatBot** 💬
Build a complete conversational agent.
- Multi-turn conversations
- Context maintenance
- Natural dialogue flow

### **8. SQLite Database** 🗄️
Persist conversation state in SQLite.
- Database schema design
- Save/load checkpoints
- Long-term memory storage

### **9. LangSmith** 🔍
Integrate LangSmith for observability.
- Trace graph execution
- Debug agent behavior
- Performance monitoring

### **10. Chatbot Tools** 🛠️
Add tool-calling capabilities to chatbots.
- Web search integration
- API calling
- Tool result synthesis

### **11. Chatbot with Tools + SQLite** 🚀
Complete production-ready chatbot.
- Tool integration
- Persistent memory
- Full conversation management

### **12. MCP (Model Context Protocol)** 🔌
Work with Model Context Protocol.
- MCP integration
- Context sharing
- Advanced communication patterns

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+**
- **Cohere API Key** ([Get one here](https://cohere.com/))
- Basic understanding of LangChain concepts

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Nabin68/Langgraph-complete-guide.git
cd Langgraph-complete-guide
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Key dependencies:**
```
langchain
langchain-cohere
langgraph
python-dotenv
sqlite3
```

### 3️⃣ Set Up Environment

Create a `.env` file in the project root:

```env
COHERE_API_KEY=your_cohere_api_key_here
LANGSMITH_API_KEY=your_langsmith_key_here  # Optional
```

### 4️⃣ Run Examples

Navigate to any folder and run the example:

```bash
cd 1.Sequential_workflow
python main.py
```

---

## 🎓 Learning Path

### **For Beginners:**
1. Start with `1.Sequential_workflow`
2. Move to `2.Parallel_workflow`
3. Understand `3.Conditional_workflow`
4. Practice `4.Iterative_workflow`

### **For Intermediate:**
1. Explore `6.Persistence`
2. Build `7.ChatBot`
3. Integrate `10.Chatbot_tools`

### **For Advanced:**
1. Study `8.SQLite_Database`
2. Implement `11.Chatbot_with_tools_SQLite`
3. Master `12.MCP`
4. Experiment with `9.LangSmith`

---

## ⚙️ Tech Stack

<div align="center">

| Technology | Purpose |
|------------|---------|
| **Python** | Core language |
| **LangGraph** | Graph-based orchestration |
| **LangChain** | LLM framework |
| **Cohere** | Language model provider |
| **SQLite** | Persistent storage |
| **LangSmith** | Observability & tracing |
| **Streamlit** | UI demonstrations |

</div>

---

## 🎯 Purpose of This Repository

This repository exists to:

✅ **Learn LangGraph at a system-design level**  
✅ **Understand agent workflows beyond simple chatbots**  
✅ **Practice production-relevant patterns**  
✅ **Serve as a reference for future projects**  

### **This is NOT:**
❌ A tutorial copy  
❌ A boilerplate repo  
❌ Just documentation reading  

### **This IS:**
✅ Practical, runnable code  
✅ Progressive learning path  
✅ Real-world patterns  
✅ Production-ready examples  

---

## 🔮 Roadmap & Future Additions

- [ ] **RAG workflows** using LangGraph
- [ ] **Multi-agent graph patterns**
- [ ] **Advanced MCP integrations**
- [ ] **Vector database integration**
- [ ] **Deployment examples** (Docker, Cloud)
- [ ] **Performance optimization** techniques
- [ ] **Error handling** best practices
- [ ] **Testing strategies** for graphs

---

## 💡 Key Takeaways

After working through this repository, you will understand:

### **1. How to Think in Graphs**
- Design workflows as nodes and edges
- Visualize execution flow
- Plan conditional paths

### **2. How to Control LLM Execution**
- Manage state explicitly
- Route based on conditions
- Handle tool calls gracefully

### **3. How to Build Extensible Systems**
- Modular node design
- Reusable graph patterns
- Scalable architecture

---

## 📚 Additional Resources

- **LangGraph Docs:** https://langchain-ai.github.io/langgraph/
- **LangChain Docs:** https://python.langchain.com/docs/
- **Cohere Platform:** https://cohere.com/
- **LangSmith:** https://smith.langchain.com/

---

## 👤 Author

**Nabin**

Focused on LangGraph, agent systems, and scalable AI workflows.

- GitHub: [@Nabin68](https://github.com/Nabin68)
- Repository: [Langgraph-complete-guide](https://github.com/Nabin68/Langgraph-complete-guide)

---

## ⚖️ License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/Nabin68/Langgraph-complete-guide/issues) if you want to contribute.

---

## ✅ Final Note

If you are learning LangGraph seriously, this repository demonstrates:

- ✅ **How to think in graphs** — Not just chains
- ✅ **How to control LLM execution** — Explicit state management
- ✅ **How to build extensible agent systems** — Production patterns

### **Start with the basics, progress to advanced patterns, and build real systems.**

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**Made with 🧠 by Nabin**

*Learning LangGraph one graph at a time*

</div>
