class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # защищенный атрибут
        self._name = name        # защищенный атрибут
        self._access_level = "user"  # по умолчанию 'user'

    # Геттеры для атрибутов
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Сеттеры для изменяемых атрибутов
    def set_name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f"ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self._access_level}"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = "admin"  # переопределяем уровень доступа
        self._users_list = []         # список пользователей

    # Метод для добавления пользователя
    def add_user(self, user):
        if not isinstance(user, User):
            raise ValueError("Могут быть добавлены только пользовательские объекты")
        if user not in self._users_list:
            self._users_list.append(user)
            print(f"User {user.get_name()} добавлено успешно.")
        else:
            print(f"User {user.get_name()} уже существует.")

    # Метод для удаления пользователя
    def remove_user(self, user):
        if user in self._users_list:
            self._users_list.remove(user)
            print(f"User {user.get_name()} успешно удален.")
        else:
            print(f"User {user.get_name()} не найден в системе.")

    # Метод для просмотра всех пользователей
    def list_users(self):
        print("Текущие пользователи в системе:")
        for user in self._users_list:
            print(user)


# Пример использования
if __name__ == "__main__":
    # Создаем обычных пользователей
    user1 = User("001", "Вася")
    user2 = User("002", "Петя")

    # Создаем администратора
    admin = Admin("999", "Admin Коля")

    # Администратор добавляет пользователей
    admin.add_user(user1)
    admin.add_user(user2)

    # Пытаемся добавить не-пользователя
    try:
        admin.add_user("not a user")
    except ValueError as e:
        print(e)

    # Выводим список пользователей
    admin.list_users()

    # Удаляем пользователя
    admin.remove_user(user1)

    # Пытаемся удалить несуществующего пользователя
    admin.remove_user(user1)

    # Проверяем изменения
    admin.list_users()