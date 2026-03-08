from backend.tools.figure_caption_detector import extract_figure_number


def router_agent(state):

    query = state["query"].lower()

    # detect figure number like "Figure 2", "Fig 3"
    figure_number = extract_figure_number(query)

    if figure_number is not None:
        print(f"Routing to VISION agent (Figure {figure_number})")
        return {"route": "vision"}

    # detect diagram style queries
    if any(word in query for word in ["figure", "fig", "diagram", "image", "chart", "graph"]):
        print("Routing to VISION agent")
        return {"route": "vision"}

    print("Routing to TEXT RAG")
    return {"route": "rag"}