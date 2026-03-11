from typing import List 
from model import Task
from storage import load_tasks, save_tasks


class TaskService:
    
    def add_task(self, title:str)-> Task:
        tasks = load_tasks()
        task  = Task.create(title)
        tasks.append(task)
        save_tasks(tasks)
        return task
    
    def list_tasks(self) -> List[Task]:
        return load_tasks()
    
    def remove_task(self, task_id: str) -> bool:
        tasks = load_tasks()
        for task in tasks: 
            if task.id == task_id: 
                tasks.remove(task)
                save_tasks(tasks)
                return True
        return False
    
    def complete_task(self, task_id: str) -> bool:
        tasks = load_tasks()
        for task in tasks: 
            if task.id == task_id: 
                task.done = True
                save_tasks(tasks)
                return True
        return False