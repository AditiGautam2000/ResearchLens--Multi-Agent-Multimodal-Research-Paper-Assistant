"""from backend.tools.vector_search import search_documents, search_images


def retrieval_agent(state):

    query = state["query"]

    # -------- TEXT RETRIEVAL --------
    docs = search_documents(query)
    state["trace"].append(
    f"Retrieval agent fetched {len(docs)} chunks"
)

    # -------- IMAGE RETRIEVAL --------
    images = search_images(query)

    # -------- BUILD CONTEXT --------
    context = "\n\n".join(docs) if docs else ""

    # -------- UPDATE STATE --------
    state["documents"] = docs
    state["context"] = context
    state["images"] = images

    # -------- DEBUG OUTPUT --------
    print("Retrieved documents:", len(docs))
    print("Retrieved images:", len(images))

    return state


"""
from backend.tools.vector_search import search_documents


def retrieval_agent(state):

    query = state["query"]

    docs = search_documents(query)

    context = "\n\n".join(docs)

    state["documents"] = docs
    state["context"] = context

    print("Retrieved documents:", len(docs))

    return state

"""  
PDF
 ↓
extract text
extract images
 ↓
text embeddings → Qdrant
image embeddings → Qdrant
"""

"""
query
 ↓
text retrieval
image retrieval
 ↓
LLM reasoning
"""