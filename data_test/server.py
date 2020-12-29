import pandas


excel_data = pandas.read_excel('data.xlsx', sheet_name='users')

print(excel_data)
