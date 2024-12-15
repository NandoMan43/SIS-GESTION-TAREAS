import tkinter as tk
from db_manager import initialize_db, add_task, get_tasks, complete_task, delete_task

def add_task_gui():
    def submit_task():
        description = task_entry.get()
        if description:
            add_task(description)
            task_entry.delete(0, tk.END)
            refresh_task_list()

    add_window = tk.Toplevel()
    add_window.title("Agregar Tarea")
    tk.Label(add_window, text="Descripción:").pack()
    task_entry = tk.Entry(add_window)
    task_entry.pack()
    tk.Button(add_window, text="Agregar", command=submit_task).pack()

def refresh_task_list():
    for widget in task_frame.winfo_children():
        widget.destroy()
    tasks = get_tasks()
    for task in tasks:
        task_label = tk.Label(task_frame, text=f"{task[0]}: {task[1]} - {task[2]}")
        task_label.pack()
        tk.Button(task_frame, text="Completado", command=lambda t=task[0]: complete_task_gui(t)).pack()
        tk.Button(task_frame, text="Eliminar", command=lambda t=task[0]: delete_task_gui(t)).pack()

def complete_task_gui(task_id):
    complete_task(task_id)
    refresh_task_list()

def delete_task_gui(task_id):
    delete_task(task_id)
    refresh_task_list()

# Inicialización de la GUI
initialize_db()
root = tk.Tk()
root.title("Gestor de Tareas")

tk.Button(root, text="Agregar Tarea", command=add_task_gui).pack()
task_frame = tk.Frame(root)
task_frame.pack()
refresh_task_list()
root.mainloop()
