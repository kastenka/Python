import sys


print(sum([int(i) for i in sys.argv[1] if i.isdigit()]))

