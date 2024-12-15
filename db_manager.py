# db_manager.py
import sqlite3

# Función para inicializar la base de datos
def initialize_db():
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        status TEXT NOT NULL
                    )''')
    connection.commit()
    connection.close()

# Función para agregar una tarea
def add_task(description):
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (description, status) VALUES (?, ?)", (description, 'pendiente'))
    connection.commit()
    connection.close()

# Función para obtener todas las tareas
def get_tasks():
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    connection.close()
    return tasks

# Función para marcar una tarea como completada
def complete_task(task_id):
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", ('completada', task_id))
    connection.commit()
    connection.close()

# Función para eliminar una tarea
def delete_task(task_id):
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()
