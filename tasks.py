import json

TASKS_FILE = "tasks.json"


def load_tasks(filename=TASKS_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                return []
            data = json.loads(content)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks, filename=TASKS_FILE):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not done"
        print(f"{i}. {task['title']} - {status}")


def mark_task_done(tasks):
    if not tasks:
        print("No tasks available.")
        return

    list_tasks(tasks)
    choice = input("Enter task number to mark as done: ")

    if not choice.isdigit():
        print("Invalid number.")
        return

    number = int(choice)

    if number < 1 or number > len(tasks):
        print("Task number out of range.")
        return

    tasks[number - 1]["done"] = True
    save_tasks(tasks)
    print("Task marked as done.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add new task")
        print("2. View all tasks")
        print("3. Mark task as done")
        print("4. Save tasks")
        print("5. Load tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved.")
        elif choice == "5":
            tasks = load_tasks()
            print("Tasks loaded.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
