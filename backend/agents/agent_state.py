from typing import TypedDict, List


class AgentState(TypedDict):

    query: str
    history: list

    documents: list
    context: str

    answer: str

    image_explanation: str