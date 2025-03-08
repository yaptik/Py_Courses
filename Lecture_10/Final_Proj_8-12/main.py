import task_class


def menu():
    print("""
         1 - добавить запись пароля
         2 - просмотреть все пароли
         3 - найти пароль по ID
         4 - изменить запись пароля по ID
         -1 - выйти из хранилища паролей""")


def main():
    print("Привет! Это хранилище паролей!")
    manager = task_class.PasswordManager()
    menu()

    oper = int(input("Выбери нужную функцию из меню: "))
    while oper != 0:
        if oper == 1:
            pass_id = int(input("Введите ID для записи: "))
            name = input("Введите название сервиса: ")
            username = input("Введите логин: ")
            password = input("Введите пароль: ")  # Пароль вводится в открытом виде
            try:
                manager.add_password(pass_id, name, username, password)
            except Exception as e:
                print(e)
        elif oper == 2:
            manager.show_all_passwords()
        elif oper == 3:
            pass_id = int(input("Введите ID для поиска пароля: "))
            manager.find_password(pass_id)
        elif oper == 4:
            pass_id = int(input("Введите ID для изменения пароля: "))
            new_name = input("Введите новое название сервиса: ")
            new_username = input("Введите новый логин: ")
            new_password = input("Введите новый пароль: ")
            manager.change_password(pass_id, new_name, new_username, new_password)

        menu()
        oper = int(input("Выбери нужную функцию из меню: "))

    print("До свидания!")


if __name__ == "__main__":
    main()
