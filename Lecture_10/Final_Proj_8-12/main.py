import task_class


def menu():
    """
    Функция для отображения меню с доступными действиями пользователя.
    """
    print("""
         1 - добавить запись пароля
         2 - просмотреть все пароли
         3 - найти пароль по ID
         4 - изменить запись пароля по ID
         5 - удалить запись пароля по ID
         -1 - выйти из хранилища паролей""")


def main():
    """
    Основная функция программы. Обрабатывает ввод пользователя, вызывает
    соответствующие методы для управления паролями, отображает меню и
    выполняет проверки на корректность ввода.
    """
    print("Привет! Это хранилище паролей!")
    manager = task_class.PasswordManager()  # Создаем объект менеджера паролей
    menu()

    while True:
        try:
            oper = int(input("Выбери нужную функцию из меню: "))
            if oper < -1 or oper > 5:  # Проверка на корректность ввода
                print("Неверный выбор! Пожалуйста, выбери число от -1 до 5.")
                continue
            if oper == 0:  # Обработка случая, если введен 0
                print("Ошибка! Пункт с номером 0 отсутствует в меню.")
                continue
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите число.")
            continue

        if oper == -1:
            print("До свидания!")
            break  # Завершаем программу

        elif oper == 1:
            # Проверка ID
            while True:
                try:
                    pass_id = int(input("Введите ID для записи: "))
                    break
                except ValueError:
                    print("Ошибка ввода ID! Пожалуйста, введите число.")

            # Проверка обязательных полей
            while True:
                name = input("Введите название сервиса: ").strip()
                if len(name) >= 3:
                    break
                print("Ошибка! Название сервиса должно быть не менее 3 символов.")

            while True:
                username = input("Введите логин: ").strip()
                if len(username) >= 3:
                    break
                print("Ошибка! Логин должен быть не менее 3 символов.")

            while True:
                password = input("Введите пароль: ").strip()
                if len(password) >= 3:
                    break
                print("Ошибка! Пароль должен быть не менее 3 символов.")

            try:
                manager.add_password(pass_id, name, username, password)  # Добавление пароля
            except Exception as e:
                print(e)

        elif oper == 2:
            manager.show_all_passwords()  # Отображение всех паролей
        elif oper == 3:
            # Проверка ID
            while True:
                try:
                    pass_id = int(input("Введите ID для поиска пароля: "))
                    break
                except ValueError:
                    print("Ошибка ввода ID! Пожалуйста, введите число.")

            result = manager.find_password(pass_id)  # Поиск пароля по ID
            if result:  # Если пароль найден, вывести его
                print(result)

        elif oper == 4:
            # Проверка ID для изменения пароля
            while True:
                try:
                    pass_id = int(input("Введите ID для изменения пароля: "))
                    break
                except ValueError:
                    print("Ошибка ввода ID! Пожалуйста, введите число.")

            # Проверка обязательных полей
            while True:
                new_name = input("Введите новое название сервиса: ").strip()
                if new_name and len(new_name) >= 3:
                    break
                print("Ошибка! Название сервиса должно быть не менее 3 символов.")

            while True:
                new_username = input("Введите новый логин: ").strip()
                if new_username and len(new_username) >= 3:
                    break
                print("Ошибка! Логин должен быть не менее 3 символов.")

            while True:
                new_password = input("Введите новый пароль: ").strip()
                if new_password and len(new_password) >= 3:
                    break
                print("Ошибка! Пароль должен быть не менее 3 символов.")

            # Попытка изменить пароль
            manager.change_password(pass_id, new_name, new_username, new_password)  # Изменение пароля

        elif oper == 5:
            # Проверка ID для удаления пароля
            while True:
                try:
                    pass_id = int(input("Введите ID для удаления пароля: "))
                    break
                except ValueError:
                    print("Ошибка ввода ID! Пожалуйста, введите число.")
            manager.delete_password(pass_id)  # Удаление пароля

        menu()  # Выводим меню после выполнения действия


if __name__ == "__main__":
    main()  # Запуск основной функции
