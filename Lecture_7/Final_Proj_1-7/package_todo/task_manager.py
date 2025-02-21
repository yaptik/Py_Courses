def create_task(tasks, task):
    """добавляет новую задачу в to-do прогу.

    Аргументы:
        tasks (dict): Словарб задач.
        task (str): Добавляемая задача.
    """
    if task not in tasks:
        tasks[task] = False  # False means task is not completed
        print("Task added successfully!")
    else:
        print("Task already exists!")


def read_tasks(tasks):
    """Показывает все задачи в to-do списке.

    Аргументы:
        tasks (dict): Словарь с задачами.
    """
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nTo-Do List:")
        for task, completed in tasks.items():
            status = "[✔] Completed" if completed else "[ ] In Progress"
            print(f"- {task} {status}")
        print()


def mark_task_completed(tasks, task):
    """Помечает как выполненное.

    Аргументы:
        tasks (dict): Слоаврь с задачами.
        task (str): Задача которую пометить как выполненную.
    """
    if task in tasks:
        tasks[task] = True
        print("Task marked as completed!")
    else:
        print("Task not found!")


def delete_task(tasks, task):
    """Удаляет задачи.

    Аргументы:
        tasks (dict): Словарь с задачами.
        task (str): Задача которую удалить.
    """
    if task in tasks:
        del tasks[task]
        print("Task deleted!")
    else:
        print("Task not found!")
