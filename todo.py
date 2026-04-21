tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added.")

def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"Deleted: {removed}")
    except:
        print("Invalid input.")

while True:
    print("\n1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")