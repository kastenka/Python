import sys


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
x1 = x2 = 0

Discriminant = b**2 - 4*a*c
if Discriminant < 0:
    print("Нет корней!!!")
elif Discriminant == 0:
    x1 = (-b + Discriminant**0.5)/(2*a)
    print(f"Корень один: {x1}")
else:
    x1 = (-b + Discriminant**0.5)/(2*a)
    print(int(x1))
    x2 = (-b - Discriminant**0.5)/(2*a)
    print(int(x2))
