import time

print('Секундомер - 1      Таймер - 2')
i = int(input())

while i == 1 or i == 2:
    if i == 2:
        print('Таймер. Введите время в секундах ниже')
        sec = int(input())
        print('Начинаем! Осталось:', sec)
        while sec != 0:
            sec -= 1
            time.sleep(1)
            if sec % 5 == 0 and sec != 0:
                print('Осталось:', sec)
        print('Время вышло!')
        print('')
        print('Секундомер - 1      Таймер - 2')
        i = int(input())
    elif i == 1:
        print('Секундомер.')
        input("Enter - Начать")
        start = time.time()
        input("Enter - Остановить")
        end = time.time()
        timer = round(float(end - start), 3)
        print('')
        print(timer, 'сек')
        print('Секундомер - 1      Таймер - 2')
        i = int(input())

