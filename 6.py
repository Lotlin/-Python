# * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


count = 0  # счётчик для первого элемента кортежа структуры данных
goods_structure = []  # итоговая структура данных
dict_values_name = []  # для 2-й части, делаю список значений для названия
dict_values_price = []  # для 2-й части, делаю список значений для цен
dict_values_amount = []  # для 2-й части, делаю список значений для количества
dict_values_unit = []  # для 2-й части, делаю список значений для ед.изм

while True:
    menu = '1.Ввести данные\n2.Выввести данные\n3.Выход'
    print(menu)
    change = input('Выберете пункт меню - ')

    if change == '1':
        goods_char = input('Введите данные товара: название, цена, количество, ед. измерения через пробел ').split()
        goods = {
            'название': goods_char[0],
            'цена': goods_char[1],
            'количество': goods_char[2],
            'eд': goods_char[3]
            }
        count += 1
        tuple_goods_structure = (count, goods)
        goods_structure.append(tuple_goods_structure)
        goods_list = []  # обнуляю список товаров, чтобы не задваивался при следующем if
        dict_values_name.append(goods.get('название'))  # не смогла сделать в конце, поэтому собираю тут
        dict_values_price.append(goods.get('цена'))
        dict_values_amount.append(goods.get('количество'))
        dict_values_unit.append(goods.get('eд'))
        # собираю итоговый словарь для аналитики:
        dict_analyt = {
            'название': dict_values_name,
            'цена': dict_values_price,
            'количество': dict_values_amount,
            'ед': dict_values_unit
        }

    elif change == '2':
        for i in range(len(goods_structure)):
            print(goods_structure[i])  # для удобства, чтобы не в 1 строку печатал
        print('Аналитика:', dict_analyt)

    elif change == '3':
        break

    else:
        print('Пожалуйста, выберете пункт меню')
