register_user = []
password_user = []


def register_user(username, password)->any:
    """
    Регистрация нового пользователя.

    Parameters:
    username: Имя пользователя.
    password: Пароль пользователя.
    """
    register_user.append({'username': username, 'password': password})
    print(f"Пользователь {username} успешно зарегистрирован.")
def vhod_user(username, password)->bool:
    """
    Авторизация пользователя.

    Parameters:
    username: Имя пользователя.
    password: Пароль пользователя.

    Returns:
    bool: Возвращает True, иначе False.
    """
    for user in register_user:
        if user['username'] == username and user['password'] == password:
            print(f"Пользователь {username} успешно авторизован.")
            return True
    print("Ошибка авторизации. Проверьте имя пользователя и пароль.")
    return False
def change_user(username, new_username, new_password)->any:
    """
    Изменение имени пользователя или пароля.

    Parameters:
    username: Имя текущего пользователя.
    new_username: Новое имя пользователя.
    new_password: Новый пароль пользователя.
    """
    for i in register_user:
        if i['username'] == username:
            i['username'] = new_username
            i['password'] = new_password
            print(f"успешно изменены.")
            return
    print(f"Пользователь {username} не найден.")
def reset_password(username)->any:
    """Восстановление пароля пользователя.
    Parameters:
    username: Имя пользователя, пароль которого нужно сбросить.
    """
    for i in register_user:
        if i['username'] == username:
            new_password = reset_password()
            print(f"Пароль {username} сброшен.")
            return new_password
   
