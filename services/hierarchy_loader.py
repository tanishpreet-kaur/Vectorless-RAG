import json
from pathlib import Path
from langfuse import observe

path = Path("data/govt_law_chpt_10_structure.json")

@observe
def load_hierarchy(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)