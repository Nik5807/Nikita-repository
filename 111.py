a = int (input('Введите число 1: '))
b = int (input('Введите число 2: '))

v = int (input('Какую операцию вы хотите выполнить? \n 1 + \n 2 - \n 3 / \n 4 * \n'))

if v == 1:
    r = a + b
if v == 2:
    r = a - b
if v == 3:
    r = float(a / b)
if v == 4:
    r = a * b
print ('Результат:',r)