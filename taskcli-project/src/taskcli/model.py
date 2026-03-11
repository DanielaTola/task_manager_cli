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
    
    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            title=data["title"],
            done=data.get("done", False)
        )