from langchain.utilities import SerpAPIWrapper
from langchain.agents import Tool
from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.experimental import AutoGPT
from langchain.chat_models import ChatOpenAI


class Response:
    def __init__(self, text):
        self.text = text

    def set_text(self, text):
        self.text = text


def setup_tools(response):
    search = SerpAPIWrapper()

    tools = [
        Tool(
            name="search",
            func=search.run,
            description="useful for when you need to answer questions about current events. You should ask targeted questions",
        ),
        Tool(
            name="return",
            func=response.set_text,
            description="useful to return the answer to the question you asked and finish the task",
        ),
    ]
    return tools


def setup_memory():
    # Define your embedding model
    embeddings_model = OpenAIEmbeddings()
    # Initialize the vectorstore as empty
    import faiss

    embedding_size = 1536
    index = faiss.IndexFlatL2(embedding_size)
    vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})
    return vectorstore


def setup_autogpt(response):
    tools = setup_tools(response)
    vectorstore = setup_memory()
    agent = AutoGPT.from_llm_and_tools(
        ai_name="Tom",
        ai_role="Assistant",
        tools=tools,
        llm=ChatOpenAI(temperature=0),
        memory=vectorstore.as_retriever(),
    )
    # Set verbose to be true
    agent.chain.verbose = True
    return agent


class Agent():

    def __init__(self):
        self.response = Response("")
        self.autogpt = setup_autogpt(self.response)

    def run(self, instruction):
        self.autogpt.run([instruction])
        return self.response.text


def create_autogpt():
    return Agent()
