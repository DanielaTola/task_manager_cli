from pathlib import Path
import sys 
import json

### === Rutas seguras === ###
APP_DIR = Path(__file__).resolve().parent         
PROJECT_ROOT = APP_DIR.parent                      
DATA_DIR = PROJECT_ROOT / "data"                   
FILE = DATA_DIR / "task.json"

def load_tasks(): 
    if not FILE.exists(): 
        return [] #retorna lo que haya en el archivo 
    with FILE.open("r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
    
def save_tasks(tasks): 
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def remove_tasks(task):
    tasks = load_tasks()
    for task_ in tasks: 
        if task_ == task: 
            tasks.remove(task_)
            save_tasks(tasks)
    
def update_task(task, new_task): 
    tasks = load_tasks()
    for i, task_ in enumerate(tasks): 
        if task_ == task:
            tasks[i] = new_task
            save_tasks(tasks)
        
tasks = load_tasks()   

"""
    argv: convierte la linea en la consola en un array por ejemplo. 
    python main.py add "pruebas de desarrollo" 
    se convierte en ["main.py", "add", "pruebas de desarrollo"]
    if len (sys.argv) > 1: 
"""
#print(sys.argv)
if len (sys.argv) > 1: 
    comando = sys.argv[1] 
    if comando == "add": 
        tarea = sys.argv[2]
        tasks.append(tarea)
        save_tasks(tasks)
        print (f"{tarea} tarea agregada.")
    elif comando == "remove": 
        task_remove = sys.argv[2]
        remove_tasks(task_remove)
        print (f"{task_remove} tarea eliminada.")
    elif comando == "update": 
        task_update = sys.argv[2]
        task_new = sys.argv[3]
        update_task(task_update,task_new)
        print (f"{task_update} tarea actualizada {task_new}.")
    elif comando == "list": 
        print ("Tus tareas: ")
        for t in tasks: 
            print(f"- {t} ")    
else:
    print("Se debe ingresar el comando de la siguiente manera: python main.py add <tarea>")   


