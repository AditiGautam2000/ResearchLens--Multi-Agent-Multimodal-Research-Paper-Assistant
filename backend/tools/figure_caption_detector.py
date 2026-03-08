import re


FIGURE_PATTERNS = [
    r"\bfig(?:ure)?\.?\s*(\d+)",          # Fig 2 / Fig.2 / Figure 2
    r"\bfig(?:ure)?\s*(\d+)[a-z]?",       # Fig 2a / Figure 3b
    r"\bfigure[-\s]*(\d+)",               # Figure-2
    r"\bfig\.\s*(\d+)",                   # Fig. 2
    r"\bfig\s*(\d+)",                     # Fig 2
]


def extract_figure_number(text: str):
    """
    Detect figure numbers from research paper captions.
    Returns the first detected figure number.
    """

    text = text.lower()

    for pattern in FIGURE_PATTERNS:
        match = re.search(pattern, text)

        if match:
            try:
                return int(match.group(1))
            except:
                pass

    return None