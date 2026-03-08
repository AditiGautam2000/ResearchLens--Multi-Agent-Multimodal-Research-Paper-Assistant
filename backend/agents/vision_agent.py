from backend.services.mongo_service import figure_collection
from backend.services.vision_service import analyze_figure
import re


def extract_figure_number(query: str):
    match = re.search(r"figure\s*(\d+)|fig\.?\s*(\d+)", query.lower())
    if match:
        return int(match.group(1) or match.group(2))
    return None


def vision_agent(state):

    query = state["query"]
    figure_number = extract_figure_number(query)

    figure = figure_collection.find_one({"figure": figure_number})

    if not figure:
        state["vision_answer"] = "Figure not found in the document."
        return state

    image_path = figure["image_path"]

    print("Calling Ollama Moondream")

    description = analyze_figure(image_path, query)

    # cache
    figure_collection.update_one(
        {"_id": figure["_id"]},
        {"$set": {"description": description}}
    )

    state["vision_answer"] = description

    return state


    #If paper contains embedded images model will work fine with with latex images (NOT)X.
    #Modify later- Solution 1 — Render Page and Crop Figure Area