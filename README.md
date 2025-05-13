# Autonomous Task Execution Agent

This project implements an Autonomous AI Agent that performs reasoning-driven task execution using LangChain and the Ollama `gemma` model. Users can enter natural language tasks through a Streamlit interface, and the agent selects appropriate tools (Calculator, Search, Summarizer) to generate intelligent responses.

## Table of Contents

- [Installing Libraries](#1-installing-libraries)  
- [Agent Tools and Architecture](#2-agent-tools-and-architecture)  
- [Streamlit UI and Task Flow](#3-streamlit-ui-and-task-flow)  
- [Video Demostration](#4-video-demonstration)
- [Conclusion](#5-conclusion)

## 1. Installing Libraries

Before running the application, make sure all Python dependencies are installed and the local model is available.

### Step 1: Install Python dependencies

Use the following command to install all required packages:

```bash
pip install -r requirements.txt
```

### Step 2: Set up Ollama and the Gemma model

Ensure that Ollama is installed on your machine. Then, pull and run the gemma model locally:

```bash
ollama pull gemma
ollama run gemma    
```

This will start the model server on your local machine and make it accessible for LangChain to use during task execution.

## 2. Agent Tools and Architecture

The backend of this application is powered by LangChain's ZeroShotAgent, which connects to the locally running gemma model via Ollama. The agent is provided with access to a custom toolset that allows it to reason and act based on the given prompt.

### Tools Integrated

| Tool        | Description                                                       |
|-------------|-------------------------------------------------------------------|
| Calculator  | Evaluates arithmetic and mathematical expressions using Python's eval().               |
| Search      | Returns simulated search results for general knowledge queries.                      |
| Summarizer  | Provides shortened summaries of long input texts (simulation-based).              |

These tools are implemented as LangChain-compatible functions and registered with the agent during initialization.

## 3. Streamlit UI and Task Flow

The front end is built using Streamlit and provides a minimal and functional interface for task submission and result viewing.

### Task Execution Flow

1. **Input Field**: Users enter their desired task or query in a text box.
2. **Trigger Agent**: Upon submission, the text is passed to the LangChain agent.
3. **Tool Selection**: Based on the task, the agent chooses the most relevant tool (Calculator, Search, or Summarizer).
4. **Execution**: The selected tool processes the task and returns the result.
5. **Display Output**: Streamlit displays the agent’s response in a readable format.

This setup allows users to perform a wide range of operations—from calculations to content summarization—via a single unified interface.

## 4. Video Demonstration
A walkthrough video showing local model startup and real-time response

https://github.com/user-attachments/assets/e020307f-619a-4f12-a53a-b876dc4a11eb



## 5. Conclusion

This project demonstrates how to combine a local LLM with LangChain’s reasoning agent and a lightweight UI like Streamlit to perform autonomous task execution. It highlights the ability to:

 - Integrate tool-based reasoning workflows

 - Run everything locally without external APIs

 - Provide a seamless user experience
