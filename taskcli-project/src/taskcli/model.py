from dataclasses import dataclass
import uuid 

@dataclass
class Task: 
    id: str
    title: str
    done: bool = False

    def __init__(self, id, title, done=False):
        self.id = id
        self.title = title
        self.done = done

    @staticmethod
    def create (title: str): 
        return Task(
            id=str(uuid.uuid4()), 
            title=title.strip(), 
            done=False
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done
        }
    
    @classmethod
    def from_dict(cls,data: dict) -> "Task":
        return cls(
            id=data.get("id", str(uuid.uuid4())), 
            title=str(data.get("title", "")).strip(), 
            done=data.get("done", False)
        )