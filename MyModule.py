from MyModule import *

while True:
    print("Выберите действие:")
    print("1-Регистрация\n2-Авторизация\n3-Изменение имени или пароля\n4-Восстановление пароля\n5-Завершение\n")
    choice = input()
    if choice == "1":
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        register_user,password_user = register_user(username, password)
    elif choice == "2":
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        register_user,password_user = register_user(username, password)
    elif choice =="3":
        username = input("Введите текущее имя пользователя: ")
        new_username = input("Введите новое имя пользователя: ")
        new_password = input("Введите новый пароль: ")
        register_user,password_user = register_user(username, new_username, new_password)
    elif choice == "4":
        username = input("Введите имя пользователя для восстановления пароля: ")
        register_user,password_user = reset_password(username)
    elif choice =="5":
        print("Завершение.")
        break