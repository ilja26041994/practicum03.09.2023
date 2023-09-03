# Напишите функцию,
# которая будет принимать список чисел и возвращать два числа,
# абсолютная разность которых минимальна.
# Пару чисел нужно вернуть в виде списка,
# отсортированного по возрастанию.
import random
import functions
listOfNumbers = []
for i in range(20):
    listOfNumbers.append(random.randint(10, 100))
print(listOfNumbers)
minDifference = functions.get_min_difference(listOfNumbers)
print(minDifference)