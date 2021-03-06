# Процессы. Память родительского и дочернего процесса
# Память целиком копируется. Но памяти разные: у дочернего процесса своя память, у родительского - своя. То же самое
# относится и к файловым дискрипторам


import os


# предположим есть файл с 2 строками
f = open("data.txt")  # открываем файл на чтение
foo = f.readline()  # читаем в переменную одну строчку

if os.fork() == 0:   # создается точная копия родительского процесса после вызова fork
    # дочерний процесс
    foo = f.readline()  # читаем уже 2 строчку, никак не влияет на родительский процесс
    print(f"child: {foo}")
else:
    # родительский процесс
    foo = f.readline()  # считаем 2 строчку
    print(f"parent: {foo}")
