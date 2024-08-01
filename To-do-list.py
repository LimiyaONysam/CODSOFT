
class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def add_task(self):
        task = input("Enter a task: ")
        self.tasks.append(task)
        print("Task added!")

    def delete_task(self):
        self.display_tasks()
        task_number = int(input("Enter the task number to delete: ")) - 1
        if task_number < len(self.tasks):
            del self.tasks[task_number]
            print("Task deleted!")
        else:
            print("Invalid task number.")

    def mark_task_complete(self):
        self.display_tasks()
        task_number = int(input("Enter the task number to mark as complete: ")) - 1
        if task_number < len(self.tasks):
            task = self.tasks[task_number]
            self.tasks[task_number] = f"{task} (Completed)"
            print("Task marked as complete!")
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()
    while True:
        print("\n1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                todo.display_tasks()
            case "2":
                todo.add_task()
            case "3":
                todo.delete_task()
            case "4":
                todo.mark_task_complete()
            case "5":
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()



