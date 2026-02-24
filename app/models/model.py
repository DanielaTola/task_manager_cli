from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task: 
    id: str
    title: str
    status: str
    priority:str
    create_at: datetime