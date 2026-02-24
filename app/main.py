from pathlib import Path
import sys 
import json


# # # === Rutas seguras ===
APP_DIR = Path(__file__).resolve().parent         
PROJECT_ROOT = APP_DIR.parent                      
DATA_DIR = PROJECT_ROOT / "data"                   
FILE = DATA_DIR / "task.json"

def load_tasks(): 
    if not FILE.exists: 
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
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with FILE.open("r", encoding="utf-8") as f: 
        load_tasks()

        
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
    elif comando == "list": 
        print ("Tus tareas: ")
        for t in tasks: 
            print(f"- {t} ")    
else:
    print("Se debe ingresar el comando de la siguiente manera: python main.py add <tarea>")   


