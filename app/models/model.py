from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task: 
    id: str
    title: str
    status: str
    priority:str
    tags: str
    description: str
    responsible: str
    create_at: datetime
    update_att: datetime