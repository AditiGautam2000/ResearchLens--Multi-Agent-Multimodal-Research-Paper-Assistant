"""from fastapi import APIRouter
from pydantic import BaseModel

from backend.agents.retrieval_agent import retrieval_agent

router = APIRouter()


class QueryRequest(BaseModel):
    query: str


@router.post("/query")
async def query_documents(request: QueryRequest):

    state = {
        "query": request.query
    }

    result = retrieval_agent(state)

    return {
        "query": request.query,
        "retrieved_chunks": result["documents"]
    }"""







"""from fastapi import APIRouter
from pydantic import BaseModel

from backend.agents.graph_builder import build_graph
from langchain_core.runnables import Runnable

graph: Runnable = build_graph()

router = APIRouter()

# Initialize graph once
graph = build_graph()


class QueryRequest(BaseModel):
    query: str


@router.post("/query")
async def query_documents(request: QueryRequest):


    state = {
    "query": request.query,
    "documents": [],
    "context": "",
    "images": [],
    "image_descriptions": [],
    "answer": ""
}

    result = graph.invoke(state)

    return {
        "query": request.query,
        "answer": result["answer"],
        "retrieved_chunks": result["documents"]
    }"""



from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.memory_service import save_message, get_history
from backend.agents.graph_builder import build_graph

router = APIRouter()

graph = build_graph()


class QueryRequest(BaseModel):
    query: str
    session_id: str


@router.post("/query")
async def query_documents(request: QueryRequest):

    history = get_history(request.session_id)

    state = {
    "query": request.query,
    "history": history,
    "documents": [],
    "context": "",
    "answer": ""
}

    result = graph.invoke(state) #type: ignore

    answer = result["answer"]

    save_message(request.session_id, "user", request.query)
    save_message(request.session_id, "assistant", answer)

    return {"answer": result["answer"]}