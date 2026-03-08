import re

def detect_figure_number(query: str):

    match = re.search(r"fig(?:ure)?\s*(\d+)", query.lower())

    if match:
        return int(match.group(1))

    return None