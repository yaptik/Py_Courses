import task_class
import pytest


def test_add_password():
    """
    Тест для проверки добавления пароля в менеджер паролей.
    """
    manager = task_class.PasswordManager()  # Создаем новый менеджер
    manager.password_list = {}  # Очищаем список паролей перед тестом
    manager.add_password(1, "Google", "user1", "password1")
    assert 1 in manager.password_list


def test_find_password():
    """
    Тест для проверки поиска пароля по ID в менеджере паролей.
    """
    manager = task_class.PasswordManager()  # Создаем новый менеджер
    manager.password_list = {}  # Очищаем список паролей перед тестом
    manager.add_password(2, "Facebook", "user2", "password2")
    assert manager.find_password(2) is not None  # Ожидается, что метод вернет строку, а не None


def test_change_password():
    """
    Тест для проверки изменения пароля по ID в менеджере паролей.
    """
    manager = task_class.PasswordManager()  # Создаем новый менеджер
    manager.password_list = {}  # Очищаем список паролей перед тестом
    manager.add_password(3, "Twitter", "user3", "password3")
    manager.change_password(3, "Twitter", "user3", "new_password")
    assert manager.password_list[3][2] != "password3"  # Проверяем, что пароль изменен


def test_duplicate_id():
    """
    Тест для проверки добавления записи с повторяющимся ID. Ожидается исключение ValueError.
    """
    manager = task_class.PasswordManager()  # Создаем новый менеджер
    manager.password_list = {}  # Очищаем список паролей перед тестом
    manager.add_password(1, "Google", "user1", "password1")
    with pytest.raises(ValueError):
        manager.add_password(1, "Duplicate", "user2", "password2")
