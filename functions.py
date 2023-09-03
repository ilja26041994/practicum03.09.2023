# Напишите функцию,
# которая будет принимать список чисел и возвращать два числа,
# абсолютная разность которых минимальна.
# Пару чисел нужно вернуть в виде списка,
# отсортированного по возрастанию.

def get_min_difference(list_of_numbers):
    min1 = 0
    min2 = 0
    for i in list_of_numbers:
        if i > min1:
            min1 = i
    for i in list_of_numbers:
        if i > min2 and i != min1:
            min2 = i
    return min1 , min2
