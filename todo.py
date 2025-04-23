import argparse
import json
import os

DATA_FILE = "data.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        print("No tasks found.")
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
    print("Tasks saved to json.")

def export_tasks_to_csv():
    import csv
    with open("tasks.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Description", "Completed", "Tags"])
        for task in load_tasks():
            writer.writerow([task["description"], task["completed"], ", ".join(task.get("tags", []))])

def add_task(description, tags=None):
    tasks = load_tasks()
    task = {
        "description": description,
        "completed": False,
        "tags": tags if tags else []
    }
    tasks.append(task)
    print(f"Added task: {description} with tags: {task['tags']}")
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        tag_str = f" [tags: {', '.join(task['tags'])}]" if task.get("tags") else ""
        print(f"{i}. [{status}] {task['description']}{tag_str}")

def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        completed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Zadanie ukończone i usunięte: {completed_task['description']}")
    else:
        print("Nieprawidłowy numer zadania.")
        

def edit_task(index, new_description):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        old_description = tasks[index - 1]['description']
        tasks[index - 1]['description'] = new_description
        save_tasks(tasks)
        print(f"Zaktualizowano zadanie {index}: '{old_description}' -> '{new_description}'")
    else:
        print("Nieprawidłowy numer zadania.")

def filter_by_tag(tag):
    tasks = load_tasks()
    filtered = [task for task in tasks if tag in task.get("tags", [])]
    if not filtered:
        print(f"No tasks found with tag '{tag}'")
    else:
        for i, task in enumerate(filtered, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['description']} [tags: {', '.join(task['tags'])}]")

def main():
    parser = argparse.ArgumentParser(description="Simple Todo CLI with tags")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")
    add_parser.add_argument("--tags", nargs="*", help="Optional tags for the task")

    subparsers.add_parser("list", help="List all tasks")
    subparsers.add_parser("export", help="Export tasks to csv")

    complete_parser = subparsers.add_parser("done", help="Mark task as done")
    complete_parser.add_argument("index", type=int, help="Task number to mark as complete")
    
    edit_parser = subparsers.add_parser("edit", help="Edit an existing task")
    edit_parser.add_argument("index", type=int, help="Task number to edit")
    edit_parser.add_argument("new_description", help="New task description")

    filter_parser = subparsers.add_parser("filter", help="Filter tasks by tag")
    filter_parser.add_argument("tag", help="Tag to filter tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description, args.tags)
    elif args.command == "list":
        list_tasks()
    elif args.command == "export":
        export_tasks_to_csv()
    elif args.command == "done":
        complete_task(args.index)
        feature_tags
    elif args.command == "filter":
        filter_by_tag(args.tag)
    elif args.command == "edit":
        edit_task(args.index, args.new_description)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
