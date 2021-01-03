# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_description(name=input('name '), surname=(input('surname ')), birthday=(input('birthday ')),
                     location=(input('location ')), email=(input('email ')), phone=(input('phone '))):
    return 'Имя:{0}, фамилия: {1}, год рождения: {2}, город проживания: {3},' \
           ' email: {4}, телефон: {5}'.format(name, surname, birthday, location, email, phone)


print(user_description())
