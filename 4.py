number = int(input('Пожалуйста, введите целое положительное число '))
biggest_num = number % 10
while number != 0:
    number = number // 10
    if biggest_num < number % 10:
        biggest_num = number % 10
print(biggest_num)
