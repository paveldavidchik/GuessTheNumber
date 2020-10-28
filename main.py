
from random import randint


r = randint(0, 101)
number = None
print('Угадай число от 0 до 100')
while True:
    number = int(input('Введите число: '))
    if number > r:
        print('Загаданное число меньше!')
    elif number < r:
        print('Загаданное число больше!')
    else:
        print('Вы угадали!!!')
        break

