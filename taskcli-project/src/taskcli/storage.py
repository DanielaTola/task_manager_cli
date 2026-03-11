import json
from pathlib import Path
from typing import List
from model import Task

DATA_FILE = Path("data/tasks.json")

def load_tasks() -> List[Task]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []
        
def save_tasks(tasks: List[Task]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump([task.to_dict() for task in tasks], f, ensure_ascii=False, indent=2)