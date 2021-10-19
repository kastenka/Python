import random


print("Добро пожаловать в игру 'Угадай число'!")
target_num = random.randint(-100, 100)
max_tries = 10
user_tries = 0
score = 100

while True:
    print(f"\nУ Вас осталось {max_tries - user_tries} попыток")
    if user_tries >= max_tries:
        print(f'Вы проиграли! У Вас больше нет попыток. Заданное число = {target_num}')
        break

    user_input = input("Угадайте число (введите 'stop', чтобы остановиться): ")
    if user_input == "stop":
        print(f"Игра закончена после ввода 'stop'. Заданное число = {target_num}")
        break

    try:
        user_input = int(user_input)
    except ValueError as ex:
        print("Вы должны ввести целое число!!!")
        continue

    user_tries += 1

    if target_num == user_input:
        print("Вы угадали число!")
        print(f"Ваш счет: {score * (max_tries - user_tries + 1) / max_tries}")
        break  # если угадал число
    else:
        diff = target_num - user_input
        if diff > 100:
            print("Загаданное число сильно больше, чем %s" % user_input)
        elif diff > 50:
            print("Загаданное число больше, чем %s" % user_input)
        elif diff > 0:
            print("Загаданное число немного больше, чем %s" % user_input)
        elif diff > -50:
            print(f"Загаданное число немного меньше, чем {user_input}")
        elif diff > -100:
            print(f"Загаданное число меньше, чем {user_input}")
        else:
            print(f"Загаданное число сильно меньше, чем {user_input}")
