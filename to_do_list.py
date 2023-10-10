tasks = []

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({"title": title, "description": description})
    print("Task added!")

def view_tasks():
    for i, task in enumerate(tasks):
        print(f"{i + 1}. Title: {task['title']}, Description: {task['description']}")

def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number")

def save_tasks_to_file():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"Title: {task['title']}, Description: {task['description']}\n")
    print("Tasks saved to tasks.txt")

while True:
    print("\nMenu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        save_tasks_to_file()
        break
    else:
        print("Invalid choice. Please enter a valid option.")