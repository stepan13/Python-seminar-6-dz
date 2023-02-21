# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

n = randint(1,20)
defmax = randint(0,100)
defmin = randint(0,defmax)
list = [randint(0,100) for _ in range(n)]
res = []

for i in range(len(list)):
    if defmin <= list[i] <= defmax:
        res.append(i)

print(list)
print(f"min {defmin} max {defmax}")
print(res)