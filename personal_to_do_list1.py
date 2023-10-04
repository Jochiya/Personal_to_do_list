import datetime
import copy

# Task class using the Builder pattern
class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.completed = False
        self.due_date = due_date

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        due_date_str = f", Due: {self.due_date}" if self.due_date else ""
        return f"{self.description} - {status}{due_date_str}"

# Caretaker class for Memento pattern
class TaskHistory:
    def __init__(self):
        self.history = []

    def add_memento(self, task_memento):
        self.history.append(task_memento)

    def get_memento(self, index):
        return self.history[index]

# Memento class for Task state
class TaskMemento:
    def __init__(self, task):
        self.task = copy.deepcopy(task)

# TaskList class to manage tasks
class TaskList:
    def __init__(self):
        self.tasks = []
        self.history = TaskHistory()

    def add_task(self, task):
        self.tasks.append(task)
        self.history.add_memento(TaskMemento(task))

    def mark_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                self.history.add_memento(TaskMemento(task))
                return True
        return False

    def delete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                return True
        return False

    def view_tasks(self, filter_option="all"):
        if filter_option == "completed":
            filtered_tasks = [task for task in self.tasks if task.completed]
        elif filter_option == "pending":
            filtered_tasks = [task for task in self.tasks if not task.completed]
        else:
            filtered_tasks = self.tasks

        for task in filtered_tasks:
            print(task)

# Main function
if __name__ == "__main__":
    todo_list = TaskList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Completed")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date_str = input("Enter due date (YYYY-MM-DD, optional): ")
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None

            task = Task(description, due_date)
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            description = input("Enter task description to mark as completed: ")
            if todo_list.mark_completed(description):
                print("Task marked as completed!")
            else:
                print("Task not found!")

        elif choice == "3":
            description = input("Enter task description to delete: ")
            if todo_list.delete_task(description):
                print("Task deleted successfully!")
            else:
                print("Task not found!")

        elif choice == "4":
            filter_option = input("View all, completed, or pending tasks? (all/completed/pending): ")
            todo_list.view_tasks(filter_option)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")
