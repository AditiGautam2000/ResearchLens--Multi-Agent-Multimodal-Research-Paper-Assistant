import streamlit as st
import requests
import uuid

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

BACKEND_URL = "http://127.0.0.1:8000"

# Page config
st.set_page_config(
    page_title="AI Research Lab",
    layout="wide"
)

st.title("📚 Multi-Agent AI Research Assistant")


# -------------------------------
# Upload Section
# -------------------------------

st.sidebar.header("Upload Research Paper")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    response = requests.post(
        f"{BACKEND_URL}/upload",
        files=files
    )

    if response.status_code == 200:
        st.sidebar.success("Document uploaded successfully")
    else:
        st.sidebar.error("Upload failed")


# -------------------------------
# Chat Query Section
# -------------------------------

st.header("Ask Questions About Papers")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask about the paper")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = requests.post(
        f"{BACKEND_URL}/query",
        json={"query": user_input,
               "session_id": st.session_state.session_id}
    )

    # -------- Backend safety fix --------
    if response.status_code == 200:
        result = response.json()
    else:
        st.error("Backend error")
        st.write(response.text)
        st.stop()
    # ------------------------------------

    answer = result.get("answer")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    # store images if present
    images = result.get("related_images", [])

    if images:
        st.session_state.messages.append(
            {"role": "assistant", "content": "Relevant diagrams:"}
        )
        for img in images:
            st.session_state.messages.append(
                {"role": "assistant", "content": img}
            )


# Display chat history
for msg in st.session_state.messages:

    # -------- NoneType safety fix --------
    if (
        msg["role"] == "assistant"
        and isinstance(msg["content"], str)
        and msg["content"].endswith(".png")
    ):
        st.image(msg["content"])
    else:
        st.chat_message(msg["role"]).write(msg["content"])
    # ------------------------------------


#run front-end - streamlit run frontend/streamlit_app.py --server.port 8005
# run qdrant- docker run -p 6333:6333 qdrant/qdrant
# run  backend- uvicorn backend.main:app --reload
# run vallkey- docker run -p 6379:6379 valkey/valkey
# run mongo -docker run -p 27017:27017 mongo