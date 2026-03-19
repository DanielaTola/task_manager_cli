from __future__ import annotations
import json
import os
from pathlib import Path
from typing import List
from taskcli.model import Task


def _data_file() -> Path: 
    override = os.getenv("TASKCLI_DATA_PATH")
    if override: 
        return Path(override)
    
    project_root = Path(__file__).resolve().parents[2]
    return project_root / "data"/ "tasks.json"

def load_tasks() -> List[Task]:
    path = _data_file()
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []
        
def save_tasks(tasks: List[Task]) -> None:
    path  = _data_file()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump([task.to_dict() for task in tasks], f, ensure_ascii=False, indent=2)