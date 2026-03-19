import sys
import argparse
from service import TaskService

service = TaskService()

def main():

    parser = argparse.ArgumentParser(description="Task CLI")
    subparsers = parser.add_subparsers(dest="command")

    add =subparsers.add_parser("add")
    add.add_argument("title", help="Titulo de la tarea")

    #subparsers.add_parser("list")

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument(
        "--done", 
        action="store_true", 
        help="Mostrar solo tareas completadas"
    )

    remove = subparsers.add_parser("remove")
    remove.add_argument("id", help="ID de la tarea a eliminar")

    complete = subparsers.add_parser("complete")
    complete.add_argument("id", help="ID de la tarea a completar")

    args = parser.parse_args()

    try:

        if args.command == "add":
            task = service.add_task(args.title)
            print(f"Tarea agregada: {task.id} - {task.title}")
        elif args.command == "list":
            tasks = service.list_tasks(done=args.done)
            if not tasks:
                print("No hay tareas.")
            else:
                print("Tus tareas:")
                for task in tasks:
                    status = "Done" if task.done else "Pending"
                    print(f"{status} - {task.id} - {task.title} ")
        elif args.command == "remove":
            if service.remove_task(args.id):
                print("Tarea eliminada.")
            else:
                print("Tarea no encontrada.")
        elif args.command == "complete":
            if service.complete_task(args.id):
                print("Tarea marcada como completada.")
            else:
                print("Tarea no encontrada.")
        else:
            parser.print_help()
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()