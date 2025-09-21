import os

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}\n")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print("Task added successfully.")

def mark_done(tasks, index, marked_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = marked_task
        print("Task marked as done successfully.")
    else:
        print("Invalid task index.")

def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task}' deleted successfully.")
    else:
        print("Invalid task index.")

def save_task(file_path, tasks):
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def load_tasks_from_file(file_path):
    tasks = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            tasks = file.read().splitlines()
    return tasks

def main():
    file_path = "todo_list.txt"
    tasks = load_tasks_from_file(file_path)
    while True:
        print("\n==== TO DO LIST ====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark as done")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the task to add: ")
            add_task(tasks, new_task)
        elif choice == "3":
            try:
                index = int(input("Enter the task index to mark: "))
                marked_task = input("Enter the task marked done: ")
                mark_done(tasks, index, marked_task)
            except ValueError:
                print("Invalid input. Please enter a number for the index.")
        elif choice == "4":
            try:
                index = int(input("Enter the task index to delete: "))
                delete_task(tasks, index)
            except ValueError:
                print("Invalid input. Please enter a number for the index.")
        elif choice == "5":
            save_task(file_path, tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
