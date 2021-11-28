import sys


number = int(sys.argv[1])
for i in range(1, number+1):
    print(("#" * i).rjust(number))
