# Тк словари хранят ключи в неупорядоченном виде имеется в модуле collections тип OrderedDict, который гарантирует, что
# ключи содержатся в том порядке, в котором вы добавили их в словарь
from collections import OrderedDict


ordered = OrderedDict()
for number in range(10):
    ordered[number] = str(number)
print(ordered)  # OrderedDict([(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5') ... ])

for key in ordered:
    print(key)