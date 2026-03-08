def critic_agent(state):
    
    answer = state.get("answer", "")
    context = state.get("context", "")
    images = state.get("related_images", [])

    issues = []

    if not answer.strip():
        issues.append("Empty answer")

    if len(answer) < 50:
        issues.append("Answer too short")

    if "as an ai" in answer.lower():
        issues.append("Generic AI response")

    # hallucination check
    if "diagram" in answer.lower() and not images:
        issues.append("Mentions diagrams but none retrieved")

    if issues:
        print("Critic warnings:", issues)

    return state