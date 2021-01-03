# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def user_sum(*args):
    return sum(*args)


intermediate_result = 0
result = 0
while True:
    user_num = list(input('Введите числа через пробел и нажмите Enter ').split())
    if '!!!' in user_num:
        user_num.pop()
        user_num = map(float, user_num)
        intermediate_result = user_sum(user_num)
        result += intermediate_result
        print(f'Программа завершила работу. Сумма введённых чисел равна: {result}')
        break
    else:
        user_num = map(float, user_num)
        intermediate_result = user_sum(user_num)
        result += intermediate_result
        print(f'Сумма введённых чисел равна: {result}')
