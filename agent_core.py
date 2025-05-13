"""
Handles core logic for the autonomous AI agent:
- Defines custom tools (calculator, search, summarizer)
- Initializes the LangChain agent with tool access
- Exposes a function to run user tasks through the agent
"""

from langchain_community.llms import Ollama
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.prompts import PromptTemplate




# Tool Implementations
def calculator_tool(expression: str) -> str:
    """Performs basic arithmetic calculations.

    Args:
        expression (str): A math expression as a string (e.g., "23 * 4 + 8").

    Returns:
        str: The result of the evaluation, or an error message if invalid.
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Calculation error: {e}"

def search_tool(query: str) -> str:
    """Simulates a search tool that returns a placeholder result.

    Args:
        query (str): The search query provided by the user.

    Returns:
        str: A simulated string representing a search result.
    """
    return f"(Simulated search result for: '{query}')"

def summarize_tool(text: str) -> str:
    """Simulates summarizing a block of text.

    Args:
        text (str): The input text to summarize.

    Returns:
        str: A simulated summary containing a shortened version of the input.
    """
    return f"(Simulated summary of: '{text[:60]}...')"

# Tool Registry
tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Useful for solving math problems."
    ),
    Tool(
        name="Search",
        func=search_tool,
        description="Used to look up general information on a topic."
    ),
    Tool(
        name="Summarizer",
        func=summarize_tool,
        description="Helpful for condensing long text or content."
    ),
]


# Initialize the Agent
llm = Ollama(model="gemma")

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,

)

# Agent Executor
def run_agent(task: str) -> str:
    """Executes an autonomous task using the LangChain agent.

    Args:
        task (str): The natural language input describing the task or query.

    Returns:
        str: The output generated after reasoning and executing the appropriate tool 
             (e.g., calculator, summarizer, or search).
    """
    try:
        result = agent.invoke({"input": task})
        return result.get("output", "Agent did not return a final answer.")
    except Exception as e:
        return f"Agent error: {e}"
