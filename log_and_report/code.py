import pandas as pd
import collections
import openpyxl

# открываем экселевский файл журнал логов
excel_data = pd.read_excel(
    'logs.xlsx', sheet_name='log')

# открываем таблицу с отчетом и заполняем ячейк
wb = openpyxl.load_workbook(
    filename='report.xlsx')
sheet = wb['Лист1']

# выделяем столбец с браузерами в отдельную переменную
browsers = excel_data['Браузер']

# считаем кол-во повторений каждого браузера
collections_of_browsers = collections.Counter(browsers)

# выделяем 7 самых популярных браузеров
most_common_browsers = collections_of_browsers.most_common(7)

# аналогично выделяем Купленные товары в отдельную переменную
products = excel_data['Купленные товары']

# Каждая строка столбца с товарами содержит несколько товаров, разделенных запятой
# Для удобства подсчета создаем список all_products, в который будем добавлять все товары по отдельности, исключая "Еще 2 варианта" и тп'''
all_products = []
for product in products:
    string = product.split(',')
    for element in string:
        if 'Ещё' not in element:
            all_products.append(element)

# далее аналогично браузерам находим 7 самых популярных товаров
collections_of_products = collections.Counter(all_products)
most_common_products = collections_of_products.most_common(7)

# Заполняем названия браузеров
sheet['A5'] = most_common_browsers[0][0]
sheet['A6'] = most_common_browsers[1][0]
sheet['A7'] = most_common_browsers[2][0]
sheet['A8'] = most_common_browsers[3][0]
sheet['A9'] = most_common_browsers[4][0]
sheet['A10'] = most_common_browsers[5][0]
sheet['A11'] = most_common_browsers[6][0]

# Заполняем тренд браузеров
sheet['B5'] = most_common_browsers[0][1]
sheet['B6'] = most_common_browsers[1][1]
sheet['B7'] = most_common_browsers[2][1]
sheet['B8'] = most_common_browsers[3][1]
sheet['B9'] = most_common_browsers[4][1]
sheet['B10'] = most_common_browsers[5][1]
sheet['B11'] = most_common_browsers[6][1]

# Заполняем названия товаров
sheet['A19'] = most_common_products[0][0]
sheet['A20'] = most_common_products[1][0]
sheet['A21'] = most_common_products[2][0]
sheet['A22'] = most_common_products[3][0]
sheet['A23'] = most_common_products[4][0]
sheet['A24'] = most_common_products[5][0]
sheet['A25'] = most_common_products[6][0]

# Заполняем тренд товаров
sheet['B19'] = most_common_products[0][1]
sheet['B20'] = most_common_products[1][1]
sheet['B21'] = most_common_products[2][1]
sheet['B22'] = most_common_products[3][1]
sheet['B23'] = most_common_products[4][1]
sheet['B24'] = most_common_products[5][1]
sheet['B25'] = most_common_products[6][1]

# Нахождение Количества посещений по месяцам

# создадим словарь, ключами которого будут номера месяцев, значениями ключей - посещения в соответствующем месяце
year_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0,
             '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}

# Создадим словарь, ключи которого - популярные браузеры, значения - словари с посещениями по месяцам
browsers_month = {}
for i in range(7):
    browsers_month[most_common_browsers[i][0]] = year_dict.copy()

# Для удобства отдельно рассмотрим только столбцы с датой посещения и браузером
data_plus_browsers = excel_data[['Дата посещения', 'Браузер']]

# Узнаем количество строк
rows = data_plus_browsers.shape[0]

# Рассматриваем все строки, из каждой выделяем месяц и браузер,
# увеличивая кол-во посещений в соотвествующий месяц соответственного браузера в словаре browsers_month
for i in range(rows):
    bros = data_plus_browsers.loc[i]['Браузер']
    month = data_plus_browsers.loc[i]['Дата посещения'].month
    month = str(month)
    if bros in browsers_month.keys():
        browsers_month[bros][month] += 1

# Заполнение посещения браузеров
# Чтоб не прописывать все ячейки вручную, как выше, создадим списки с индексами ячеек и будем в цикле складывать их как текст
excel_rows = ['5', '6', '7', '8', '9', '10', '11']
excel_columns = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

# для удобства создадим вспомогательный список с названиями популярных браузеров
excel_browsers = []
for bros in browsers_month.keys():
    excel_browsers.append(bros)

# Заполнение Количества посещений по месяцам
for row in range(7):
    for col in range(12):
        cell = excel_columns[col]+excel_rows[row]
        sheet[cell] = browsers_month[excel_browsers[row]][str(col+1)]

# Подсчитываем кол-во посещений по месяцам со всех браузеров
month_sum = year_dict.copy()
for v in browsers_month.values():
    for month, amount in v.items():
        month_sum[month] += amount

# Заполняем кол-во посещений по месяцам со всех браузеров
col = 0
for v in month_sum.values():
    sheet[excel_columns[col]+'12'] = v
    col += 1

# аналогично считаем продажи продуктов
data_plus_products = excel_data[['Дата посещения', 'Купленные товары']]

products_month = {}
for i in range(7):
    products_month[most_common_products[i][0]] = year_dict.copy()

rows = data_plus_products.shape[0]

for i in range(rows):
    month = data_plus_products.loc[i]['Дата посещения'].month
    month = str(month)
    prod = data_plus_products.loc[i]['Купленные товары']
    string = prod.split(',')
    for element in string:
        if element in products_month.keys():
            products_month[element][month] += 1

# Заполнение товаров по месяцам
excel_rows = ['19', '20', '21', '22', '23', '24', '25']
excel_columns = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
excel_products = []
for prod in products_month.keys():
    excel_products.append(prod)

for row in range(7):
    for col in range(12):
        cell = excel_columns[col]+excel_rows[row]
        sheet[cell] = products_month[excel_products[row]][str(col+1)]

month_sum = year_dict.copy()
for v in products_month.values():
    for month, amount in v.items():
        month_sum[month] += amount
col = 0
for v in month_sum.values():
    sheet[excel_columns[col]+'26'] = v
    col += 1

# Находим популярные и непопулярные товары у мужчин и женщин
sex_plus_products = excel_data[['Пол', 'Купленные товары']]

# Создадим и заполним список с товарами, купленными мужчинами и отдельный список с купленными женщинами
men_products = []
women_products = []

rows = sex_plus_products.shape[0]

for i in range(rows):
    sex = sex_plus_products.loc[i]['Пол']
    prod = sex_plus_products.loc[i]['Купленные товары']
    string = prod.split(',')
    for element in string:
        if 'Ещё' not in element:
            if sex == 'м':
                men_products.append(element)
            else:
                women_products.append(element)

# Находим самый популярный товар у мужчин и самый популярный у женщин
men_products_counter = collections.Counter(men_products)
women_products_counter = collections.Counter(women_products)

most_common_men_product = men_products_counter.most_common(1)[0][0]
most_common_women_product = women_products_counter.most_common(1)[0][0]

# Находим самый непопулярный товар у мужчин и самый популярный у женщин
len_men = len(men_products_counter)
len_women = len(women_products_counter)

result_men = men_products_counter.most_common()[:-(len_men+1):-1]
result_women = women_products_counter.most_common()[:-(len_women+1):-1]

less_common_men_product = result_men[0][0]
less_common_women_product = result_women[0][0]

# Заполняем соответствующие ячейки в таблице
sheet['B31'] = most_common_men_product
sheet['B32'] = most_common_women_product
sheet['B33'] = less_common_men_product
sheet['B34'] = less_common_women_product

# Сохраняем файл с отчетом
wb.save('C:\\Users\\Elena\\Desktop\\pumpskill\\log_and_report\\report.xlsx')
