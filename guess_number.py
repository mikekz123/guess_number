from random import randint as rnd
while True:
    number_of_user = int(input('Введи число: '))
    number_of_pc = rnd(1, 5)
    if number_of_user > number_of_pc:
        # ...выводим сообщение.
        print('Ваше число больше того, что загадано')
    elif number_of_user < number_of_pc:
        # ...выводим сообщение.
        print('Ваше число меньше того, что загадано')
    else:
        # ...прерываем выполнение программы и...
        break
    
# ...выводим сообщение.
print('Отличная интуиция! Вы угадали число :)')
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA