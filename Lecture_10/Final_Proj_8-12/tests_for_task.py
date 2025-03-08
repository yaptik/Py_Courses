import task_class
import pytest


def test_add_password():
    manager = task_class.PasswordManager()
    manager.add_password(1, "Google", "user1", "password1")
    assert 1 in manager.password_list


def test_find_password():
    manager = task_class.PasswordManager()
    manager.add_password(2, "Facebook", "user2", "password2")
    assert manager.find_password(2) is not None


def test_change_password():
    manager = task_class.PasswordManager()
    manager.add_password(3, "Twitter", "user3", "password3")
    manager.change_password(3, "Twitter", "user3", "new_password")
    assert manager.password_list[3][2] != "password3"


def test_duplicate_id():
    manager = task_class.PasswordManager()
    manager.add_password(1, "Google", "user1", "password1")
    with pytest.raises(ValueError):
        manager.add_password(1, "Duplicate", "user2", "password2")
