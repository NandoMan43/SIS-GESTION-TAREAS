from db_manager import add_task, get_tasks, complete_task, delete_task

# Puedes agregar funciones adicionales según sea necesario.
def list_tasks():
    tasks = get_tasks()
    for task in tasks:
        print(f"{task[0]}: {task[1]} - {task[2]}")
