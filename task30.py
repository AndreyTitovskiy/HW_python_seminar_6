# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('Введите превый элемент: '))
n = int(input('Введите разность прогрессии: '))
d = int(input('Введите количество элементов: '))
rez = []
for i in range (d):
    rez.append(a + i * n)
for element in rez:
    print(element)

