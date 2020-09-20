password = input("Введите пароль: ")
try:
    password = int(password)
    print('Ваш пароль состоит только из цифр')
except ValueError:
    try:
        b = password[0]
        print('Требования к паролю соблюдены')
    except IndexError:
        print('Вы ввели пустой пароль')
