from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()


def create_react_agent(agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION):
    llm = ChatOpenAI(model='gpt-4', temperature=0)
    tools = load_tools(["serpapi"], llm=llm)
    agent = initialize_agent(tools, llm, agent=agent_type)
    return agent
