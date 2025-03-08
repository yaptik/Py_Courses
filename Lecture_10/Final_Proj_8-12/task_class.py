class PasswordManager:
    """Класс для управления записями паролей."""

    def __init__(self):
        self.password_list = {}

    def add_password(self, pass_id, name, username, password):
        """Добавление записи пароля с проверкой длины строк."""
        if pass_id in self.password_list:
            raise ValueError("Пароль с таким ID уже существует!")

        # Проверка на минимальную длину
        if len(name) < 3 or len(username) < 3 or len(password) < 3:
            raise ValueError("Название сервиса, логин и пароль должны быть длиной не менее 3 символов!")

        self.password_list[pass_id] = (name, username, password)

    def find_password(self, pass_id):
        """Поиск записи пароля по ID."""
        if pass_id in self.password_list:
            name, username, password = self.password_list[pass_id]
            return f"Сервис: {name}, Логин: {username}, Пароль: {password}"
        else:
            print("Пароль с таким ID не найден!")  # Сообщение, если пароль не найден
            return None

    def change_password(self, pass_id, new_name, new_username, new_password):
        """Изменение записи пароля."""
        if pass_id in self.password_list:
            self.password_list[pass_id] = (new_name, new_username, new_password)
        else:
            print("ID не найден!")

    def delete_password(self, pass_id):
        """Удаление записи пароля по ID."""
        if pass_id in self.password_list:
            del self.password_list[pass_id]
            print(f"Пароль с ID {pass_id} был удален.")
        else:
            print("ID не найден!")

    def show_all_passwords(self):
        """Показать все записи паролей."""
        if self.password_list:
            for pass_id, (name, username, password) in self.password_list.items():
                print(f"ID: {pass_id}, Сервис: {name}, Логин: {username}, Пароль: {password}")
        else:
            print("Нет сохраненных паролей.")
