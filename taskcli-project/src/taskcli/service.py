from typing import List 
from model import Task
from storage import load_tasks, save_tasks


class TaskService:
    
    def add_task(self, title:str)-> Task:
        tasks = load_tasks()
        if not title.strip():
            raise ValueError("El título de la tarea no puede estar vacío.")
        elif len(title) > 100:
            raise ValueError("El título de la tarea no puede exceder los 100 caracteres.")
        elif title in [task.title for task in tasks]:
            raise ValueError("Ya existe una tarea con ese título.")
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