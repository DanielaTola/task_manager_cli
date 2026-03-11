import sys
import argparse
from service import TaskService

service = TaskService()


def main():

    parser = argparse.ArgumentParser(description="Task CLI")
    subparsers = parser.add_subparsers(dest="command")

    add =subparsers.add_parser("add")
    add.add_argument("title", help="Title of the task")

    subparsers.add_parser("list")

    remove = subparsers.add_parser("remove")
    remove.add_argument("id", help="ID of the task to remove")

    complete = subparsers.add_parser("complete")
    complete.add_argument("id", help="ID of the task to complete")

    args = parser.parse_args()

    if args.command == "add":
        task = service.add_task(args.title)
        print(f"Tarea agregada: {task.id} - {task.title}")
    elif args.command == "list":
        tasks = service.list_tasks()
        if not tasks:
            print("No hay tareas.")
        else:
            print("Tus tareas:")
            for task in tasks:
                status = "✓" if task.done else "✗"
                print(f"{status} {task.id} - {task.title}")
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


if __name__ == "__main__":
    main()