class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"description": task, "completed": False})

    def list_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['description']} - {status}")

    def mark_task_completed(self, task_description):
        for task in self.tasks:
            if task["description"] == task_description:
                task["completed"] = True
                break

    def clear_tasks(self):
        self.tasks = []

if __name__ == "__main__":
    todo_manager = ToDoListManager()
    while True:
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear all tasks")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            task = input("Enter task description: ")
            todo_manager.add_task(task)
        elif choice == "2":
            todo_manager.list_tasks()
        elif choice == "3":
            task_description = input("Enter task description to mark as completed: ")
            todo_manager.mark_task_completed(task_description)
        elif choice == "4":
            todo_manager.clear_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please select a valid option.")
