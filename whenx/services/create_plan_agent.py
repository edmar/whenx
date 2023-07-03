from langchain.chat_models import ChatOpenAI
from langchain.experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain import SerpAPIWrapper
from langchain.agents.tools import Tool


def create_plan_agent():
    search = SerpAPIWrapper()
    tools = [
        Tool(
            name="Search",
            func=search.results,
            description="useful for when you need to answer questions about current events"
        )
    ]
    model = ChatOpenAI(temperature=0)
    planner = load_chat_planner(model)
    executor = load_agent_executor(model, tools, verbose=True)
    agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)
    return agent
