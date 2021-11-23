import sys


digit_string = sys.argv[1]
num = 0

for i in digit_string:
    if i.isdigit():
        num += int(i)

print(num)

