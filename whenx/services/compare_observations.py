from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


def compare_observations(observations: list):
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    prompt = f"""Compare the two answers and decide if a new report is necessary. Is a new report necessary? (Yes/No)
    Question, Answer, Date
{observations[0].instruction},{observations[0].content}, {observations[0].created_at}
{observations[1].instruction},{observations[1].content}, {observations[1].created_at}"""
    messages = [
        SystemMessage(
            content="You are a helpful assistant that helps people compare observations."
        ),
        HumanMessage(content=prompt),
    ]
    result = llm(messages)
    return result
