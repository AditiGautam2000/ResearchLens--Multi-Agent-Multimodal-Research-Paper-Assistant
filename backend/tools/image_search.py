from backend.services.mongo_service import figure_collection


def get_figure_by_number(number: int):

    result = figure_collection.find_one(
        {"figure": number}
    )

    if result:
        return result["image_path"]

    return None