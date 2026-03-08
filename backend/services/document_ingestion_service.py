from backend.services.qdrant_service import QdrantService
from backend.tools.image_extractor import extract_images_from_pdf
from backend.services.mongo_service import figure_collection
from backend.tools.figure_caption_detector import extract_figure_number

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings


def process_document(file_path: str):

    print("Processing:", file_path)

    qdrant_service = QdrantService()
    collection_name = "your_agent"

    qdrant_service.create_collection(collection_name)

    # -------- LOAD PDF --------

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # -------- TEXT RAG --------

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    if len(chunks) > 0:

        embeddings_model = OllamaEmbeddings(model="nomic-embed-text")

        embeddings = embeddings_model.embed_documents(
            [chunk.page_content for chunk in chunks]
        )

        qdrant_service.insert_documents(
            collection_name,
            chunks,
            embeddings
        )

        print("Inserted text chunks:", len(chunks))

    else:
        print("No text found in document")

    # -------- IMAGE EXTRACTION --------

    images = extract_images_from_pdf(file_path, "uploads")

    print("Images extracted:", len(images))

    # -------- DETECT FIGURE CAPTIONS --------

    figure_map = {}

    for doc in documents:

        figure_number = extract_figure_number(doc.page_content)

        if figure_number is not None:

            page = doc.metadata.get("page", 0) + 1

            figure_map[page] = figure_number

    print("Detected figures:", figure_map)

    # -------- MAP FIGURES TO IMAGES --------

    stored_figures = set()

    for img in images:

        page = img["page"]

        if page in figure_map:

            figure_number = figure_map[page]

            # avoid duplicate figure storage
            if figure_number not in stored_figures:

                figure_collection.insert_one({
                    "figure": figure_number,
                    "page": page,
                    "image_path": img["path"]
                })

                stored_figures.add(figure_number)

                print(f"Stored Figure {figure_number} from page {page}")
        print("Image processing finished")