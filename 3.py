# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов


def my_func(a, b, c):
    return max(a, (max(b, c)))


num_1 = float(input('Введите первое число и нажмите Enter '))
num_2 = float(input('Введите второе число и нажмите Enter '))
num_3 = float(input('Введите третье число и нажмите Enter '))
print(f'Наибольшее число из введённых: {my_func(num_1, num_2, num_3)}')


# реализация без использования max:
def my_func_1(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    else:
        return c


num_11 = float(input('Введите первое число и нажмите Enter '))
num_22 = float(input('Введите второе число и нажмите Enter '))
num_33 = float(input('Введите третье число и нажмите Enter '))
print(f'Наибольшее число из введённых: {my_func_1(num_11, num_22, num_33)}')
