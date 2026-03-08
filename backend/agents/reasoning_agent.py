from backend.services.llm_service import generate_response


def reasoning_agent(state):

    query = state["query"]

    # -----------------------------
    # VISION RESULT (VISION-ON-DEMAND)
    # -----------------------------
    if "vision_answer" in state and state["vision_answer"]:

        state["answer"] = state["vision_answer"]
        return state

    # -----------------------------
    # TEXT RAG REASONING
    # -----------------------------
    context = state.get("context", "")
    vision_context = state.get("vision_context", "")

    # convert list context to string
    if isinstance(context, list):
        context = "\n\n".join(context)

    full_context = context + "\n\n" + vision_context

    prompt = f"""
You are an expert AI assistant specialized in analyzing research papers.

Your task is to answer the user's question using ONLY the information from the document context.

DOCUMENT CONTEXT
----------------
{context}

USER QUESTION
-------------
{query}

INSTRUCTIONS
-------------
1. Use ONLY the provided document context.
2. If multiple sections are relevant, combine them logically.
3. Provide a clear, structured explanation.
4. If the document does not contain enough information, respond with:
   "The document does not contain enough information to answer this."

ANSWER
-------------
"""

    answer = generate_response(prompt)

    state["answer"] = answer

    return state