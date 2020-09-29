cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[0]},
            {'user': users[1], 'city': cities[1]},
            {'user': users[2], 'city': cities[2]}]

city = input('Введите город: ')

if city.upper() == cities[0].upper():
    print(
        f"Турист {users[0]['name']} возраст {users[0]['age']} . Посетил город {cities[0]}")

if city.upper() == cities[1].upper():
    print(
        f"Турист {users[1]['name']} возраст {users[1]['age']} . Посетил город {cities[1]}")

if city.upper() == cities[2].upper():
    print(
        f"Турист {users[2]['name']} возраст {users[2]['age']} . Посетил город {cities[2]}")
