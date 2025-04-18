import argparse
import json
import os

DATA_FILE = "data.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['description']}")

def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print(f"Completed task {index}")
    else:
        print("Invalid task number.")

def main():
    parser = argparse.ArgumentParser(description="Simple Todo CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    list_parser = subparsers.add_parser("list", help="List all tasks")

    complete_parser = subparsers.add_parser("done", help="Mark task as done")
    complete_parser.add_argument("index", type=int, help="Task number to mark as complete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        complete_task(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
