# account = {'login': '', 'password': ''}
# user = {'name': '', 'age': , 'account': }

account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

user_list = [user1, user2, user3, user4]

# part1

key_ = input('Введите ключ (name или account): ')
key_ = key_.lower()
try:
    print(f'значение ключа {key_} для юзера 1 = {user1[key_]}')
    print(f'значение ключа {key_} для юзера 2 = {user2[key_]}')
    print(f'значение ключа {key_} для юзера 3 = {user3[key_]}')
    print(f'значение ключа {key_} для юзера 4 = {user4[key_]}')
except:
    print('Введенный ключ не найден')

# part2

number = int(input('Введите порядковый номер: '))
user = user_list[number-1]
print(f'Данные по юзеру № {number}:')
print(f"имя: {user['name']}")
print(f"возраст: {user['age']}")
print(f"логин: {user['account']['login']}")
print(f"пароль: {user['account']['password']}")

# part3

num = int(input('Введите номер пользователя, которого нужно переместить в конец: '))
print(user_list[num - 1])
print(user_list)
extra_user = user_list.pop(num - 1)
user_list.append(extra_user)
print(user_list)

# part4
summ = user1['age'] + user2['age'] + user3['age'] + user4['age']
print()
print(f'Средний возраст всех юзеров: {summ/4} лет')
