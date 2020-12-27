# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().



# с задачей немного потупила, сразу не смогла решить через for, улучшенный вариант в файле 2_1

user_list = list(input('Введите элементы списка и нажмите Enter ').split())
new_list_1 = user_list[1::2]
new_list_2 = user_list[::2]
list_result = []
count = len(new_list_1)  
i = 0
while count > 0:
    list_result.append(new_list_1[i])
    list_result.append(new_list_2[i])
    i += 1
    count -= 1
if len(user_list) % 2 != 0:
    last_number = user_list.pop()
    list_result.append(last_number)
print(list_result)



