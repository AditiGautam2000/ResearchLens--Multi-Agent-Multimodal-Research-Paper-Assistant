from langgraph.graph import StateGraph, END

from backend.agents.agent_state import AgentState
from backend.agents.router_agent import router_agent
from backend.agents.retrieval_agent import retrieval_agent
from backend.agents.reasoning_agent import reasoning_agent
from backend.agents.critic_agent import critic_agent
from backend.agents.vision_agent import vision_agent


def build_graph():

    workflow = StateGraph(AgentState)

    # Nodes
    workflow.add_node("router", router_agent)
    workflow.add_node("retrieval", retrieval_agent)
    workflow.add_node("vision", vision_agent)
    workflow.add_node("reasoning", reasoning_agent)
    workflow.add_node("critic", critic_agent)

    # Entry
    workflow.set_entry_point("router")

    # CONDITIONAL ROUTING
    workflow.add_conditional_edges(
        "router",
        lambda state: state["route"],
        {
            "vision": "vision",
            "rag": "retrieval"
        }
    )

    # After retrieval → reasoning
    workflow.add_edge("retrieval", "reasoning")

    # After vision → reasoning
    workflow.add_edge("vision", "reasoning")

    # Final pipeline
    workflow.add_edge("reasoning", "critic")
    workflow.add_edge("critic", END)

    graph = workflow.compile()

    return graph