import streamlit as st
import sqlite3

# Create a database
conn = sqlite3.connect('todo1.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, description TEXT, due_date TEXT, status TEXT)''')

# Function to add a task
def add_task(description, due_date):
    c.execute("INSERT INTO tasks (description, due_date, status) VALUES (?, ?, ?)",
              (description, due_date, 'pending'))
    conn.commit()

# Function to update a task
def update_task(id, status):
    c.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, id))
    conn.commit()

# Function to delete a task
def delete_task(id):
    c.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()

# Streamlit UI
st.title('To-Do List Manager')

# Add a task
description = st.text_input('Task Description')
due_date = st.date_input('Due Date')
if st.button('Add Task'):
    add_task(description, due_date)

# Section for viewing tasks
view_option = st.selectbox('View Tasks', ['Show all', 'Show completed', 'Show pending'])

# Display tasks based on the selected view option
if view_option == 'Show all':
    st.write('All Tasks:')
    tasks = c.execute('SELECT * FROM tasks').fetchall()
elif view_option == 'Show completed':
    st.write('Completed Tasks:')
    tasks = c.execute('SELECT * FROM tasks WHERE status = "completed"').fetchall()
elif view_option == 'Show pending':
    st.write('Pending Tasks:')
    tasks = c.execute('SELECT * FROM tasks WHERE status = "pending"').fetchall()

for task in tasks:
    st.write(f'Task Number: {task[0]}, Description: {task[1]}, Due Date: {task[2]}')
    if view_option == 'Show completed' and st.checkbox(f'Mark as Pending', key=f'mark_pending_{task[0]}'):
        update_task(task[0], 'pending')
    elif view_option == 'Show pending' and st.checkbox(f'Mark as Completed', key=f'mark_completed_{task[0]}'):
        update_task(task[0], 'completed')
    elif st.checkbox(f'Delete', key=f'delete_{task[0]}'):
        delete_task(task[0])
