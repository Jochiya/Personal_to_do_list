# Personal_to_do_list
This is a personal To-do List created for easy usage of a person to manage his/her daily tasks


The code is implemented in two ways such that:

1st one: 
         This Python script implements a simple To-Do List Manager using several design patterns such as the Builder pattern for creating tasks, the Memento pattern for tracking task history, and a basic CLI interface. Users can add, mark tasks as completed, delete tasks, and view tasks based on their status.
         Named as personal_to_do_list1.py

**Key components**:

         Task class: Represents a task with a description, completion status, and an optional due date. Tasks can be marked as completed.
         TaskHistory class: Acts as a caretaker for the Memento pattern. It stores the history of tasks using mementos.
         TaskMemento class: Represents a memento capturing the state of a task. Used to track task history.
         TaskList class: Manages a list of tasks and provides methods to add, mark as completed, delete, and view tasks based on their status.
         CLI Interface: The main function allows users to interact with the To-Do List Manager via a command-line interface. Users can add tasks, mark them as completed, delete tasks, and view tasks based on status. The script employs a while loop to continuously offer these options until the user decides to exit.
         This script offers a basic yet flexible To-Do List Manager that can be run in a command-line environment. Users can easily add, manage, and view their tasks.
         


2nd one:
         Named as personal_to_do_list2.py
         This is a Python application for a To-Do List Manager created using Streamlit and SQLite. It allows users to add, update, and delete tasks, and view tasks based on their status (completed or pending). Here are the key components of the application:
         - **Database Creation**: The script establishes a connection to an SQLite database and creates a table named 'tasks' to store task-related information, including a task's description, due date, and status.
         - **Add Task Function**: There is a function to add tasks to the database. Users can input a task description and due date, and the task is inserted with a 'pending' status by default.
         - **Update Task Function**: Another function enables users to update the status of a task. They can mark a task as 'completed' or 'pending'.
         - **Delete Task Function**: Users can also delete tasks from the database using a dedicated function.
         - **Streamlit UI**: The Streamlit-based user interface allows users to interact with the To-Do List Manager. It includes the following elements:
                    - A title indicating it's a To-Do List Manager.
                    - Input fields for adding a task description and due date, along with a button to add the task to the list.
                    - A dropdown to select the view option: 'Show all', 'Show completed', or 'Show pending'.
                    - A list of tasks based on the selected view option, with checkboxes to mark them as completed or pending and an option to delete them.

This application can be a handy tool for managing tasks and can be hosted or shared via GitHub or any other platform that supports Python applications. Users can easily add, update, and delete tasks to keep track of their to-do lists.
        
        In order to run this use the command Streamlit run personal_to_do_list2.py
