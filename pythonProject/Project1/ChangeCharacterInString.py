# Изменение строки через преобразование её в список
myStr = 'maska_kastenka'
print(f'{myStr} has {type(myStr)}')

myStr = list(myStr)
myStr[3] = 'h'
print(f'{myStr} has {type(myStr)}')

myStr = ''.join(myStr)
print(f'{myStr} has {type(myStr)}')


# Изменение строки через преобразование её в bytearray
myStr = 'maska_kastenka'
print(f'{myStr} has {type(myStr)}')

myStr = bytearray(b'myStr')
print(f'{myStr} has {type(myStr)}')

myStr[0] = 101 # поддерживает изменения для текста, где есть символы, у которых ширина не более 8 битов (ASCII)
myStr = myStr.decode()  # преобразование в обычную строку
print(f'{myStr} has {type(myStr)}')

