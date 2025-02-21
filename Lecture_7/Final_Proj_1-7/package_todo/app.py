import package_todo.task_manager as task_manager


def display_menu():
    """Отображение пользовательского меню."""
    return """
    1 - Create New Task
    2 - Read All Tasks
    3 - Mark Task as Completed
    4 - Delete Task
    -1 - Exit
    """


def run_todo_app():
    """Запуск интерактивной части проги."""
    tasks = {}
    operation = 0

    while operation != -1:
        try:
            operation = int(input(display_menu()))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if operation == 1:
            task = input("Enter a new task: ").strip()
            task_manager.create_task(tasks, task)
        elif operation == 2:
            task_manager.read_tasks(tasks)
        elif operation == 3:
            task = input("Enter the task to mark as completed: ").strip()
            task_manager.mark_task_completed(tasks, task)
        elif operation == 4:
            task = input("Enter the task to delete: ").strip()
            task_manager.delete_task(tasks, task)
        elif operation != -1:
            print("Invalid option! Please choose a correct number.")
