import json
import os

TASK_FILE = 'todo_tasks.json'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def view_tasks(tasks):
    if not tasks:
        print("\n No tasks found.\n")
        return
    print("\n Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Notdone"
        print(f"{i}. {task['title']} [{status}]")
    print()


def add_task(tasks):
    title = input("Enter the task: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print("Task added successfully!\n")
    else:
        print("Task cannot be empty!\n")


def complete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as completed: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["completed"] = True
            print("Task marked as completed!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number.\n")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Task '{removed['title']}' deleted.\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    tasks = load_tasks()
    while True:
        print(" TO-DO LIST MENU")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Thank you !")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
