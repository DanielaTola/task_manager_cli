from typing import List, Optional
from model import Task
from storage import load_tasks, save_tasks
import re


class TaskService:
    
    def add_task(self, title:str)-> Task:
        tasks = load_tasks()
        if not title or not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("El título de la tarea no puede estar vacío.")
        elif len(title) > 100:
            raise ValueError("El título de la tarea no puede exceder los 100 caracteres.")
        elif title in [task.title for task in tasks]:
            raise ValueError("Ya existe una tarea con ese título.")
        elif not re.match("^[a-zA-Z0-9 ]+$", title):
            raise ValueError("El título de la tarea solo puede contener letras, números y espacios.")
        task  = Task.create(title)
        tasks.append(task)
        save_tasks(tasks)
        return task
    
    def list_tasks(self, done:Optional[bool] = None) -> List[Task]:
        tasks = load_tasks()
        if done is not None: 
            tasks = [t for t in tasks if t.done == done ]
        return tasks
    
    def remove_task(self, task_id: str) -> bool:
        try: 
            id_int = int(task_id)
            if id_int < 0:
                raise ValueError("El ID de la tarea debe ser un número entero positivo.")
        except ValueError:
            raise ValueError("El ID de la tarea debe ser un número entero.")
        tasks = load_tasks()
        for task in tasks: 
            if task.id == task_id: 
                tasks.remove(task)
                save_tasks(tasks)
                return True
            else:
                raise ValueError("Tarea no encontrada.")
        return False
    
    def complete_task(self, task_id: str) -> bool:
        try:
            id_int = int(task_id)
            if id_int < 0:
                raise ValueError("El ID de la tarea debe ser un número entero positivo.")
        except ValueError:
            raise ValueError("El ID de la tarea debe ser un número entero.")
        tasks = load_tasks()
        for task in tasks: 
            if task.id == task_id: 
                task.done = True
                save_tasks(tasks)
                return True
            else:
                raise ValueError("Tarea no encontrada.")
        return False