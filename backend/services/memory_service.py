from backend.services.mongo_service import chat_collection


def save_message(session_id, role, content):

    chat_collection.insert_one({
        "session_id": session_id,
        "role": role,
        "content": content
    })


def get_history(session_id):

    messages = chat_collection.find(
        {"session_id": session_id}
    )

    history = []

    for msg in messages:

        history.append(
            {
                "role": msg["role"],
                "content": msg["content"]
            }
        )

    return history