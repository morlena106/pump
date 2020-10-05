GENDER_MALE = 'm'
GENDER_FEMALE = 'f'


# Список пользователей
user_list = [{'name': 'Иван', 'gender': GENDER_MALE},
             {'name': 'Петр', 'gender': GENDER_MALE},
             {'name': 'Марья', 'gender': GENDER_FEMALE},
             {'name': 'Дарья', 'gender': GENDER_FEMALE},
             {'name': 'Юлия', 'gender': GENDER_FEMALE}, ]

# Список товаров
item_list = [{'title': 'Часы', 'cost': 9800},
             {'title': 'Кофемашина', 'cost': 23500},
             {'title': 'Фитнес-браслет', 'cost': 13200},
             {'title': 'Айфон', 'cost': 73900},
             {'title': 'Чехол для телефона', 'cost': 250}, ]

# Журнал регистрации - каждая запись в журнале содержит сведения о покупке
log = [{'user': user_list[0], 'purchases': [item_list[0], item_list[1], item_list[2]]},
       {'user': user_list[1], 'purchases': [item_list[0], item_list[2]]},
       {'user': user_list[2], 'purchases': [item_list[2], item_list[3]]},
       {'user': user_list[3], 'purchases': [item_list[2], item_list[3]]},
       {'user': user_list[4], 'purchases': [item_list[4], item_list[2]]}, ]

# Создадим список для хранения популярных товар: popular_items.
# Этот список будет состоять из словарей следующей структуры:
# {
#     'title':    наименование товара
#     'quantity': количество проданных товаров
# }

# создаем словарь, ключами которого будут названия купленных товаром, значениями - количество
popular_items = {}

# Обходим все записи из списка log
for record in log:

    # Для каждой записи из списка 'log' в цикле обходим все записи из списка 'purchases'
    for item in record['purchases']:

        # Получаем название купленного товара
        purchase_title = item['title']

        # если в словаре нет такого ключа, добавляем его, в противном случае увеличиваем значение соотвественного элемента на 1
        if purchase_title not in popular_items.keys():
            popular_items[purchase_title] = 1
        else:
            popular_items[purchase_title] += 1


# Выводим продажи по каждому товару
for k, v in popular_items.items():
    print(
        f"Количество продаж товара {k} = {v}")
