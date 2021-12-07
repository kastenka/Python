example_dict = {"num": [1, 2, 3], "str": ["one", "two", "three"]}
print(example_dict)  # {'num': [1, 2, 3], 'str': ['one', 'two', 'three']}
print(*example_dict)  # num str

# вывод значений по ключу с помощью get
print(example_dict.get("num"))  # [1, 2, 3]
print(*example_dict.get("num"))  # 1 2 3
print(*example_dict.get("num"), sep=", ")  # 1, 2, 3

# попытка вывода, если ключа нет в словаре
# dict.get(key[, default] -> Значение по ключу, либо default.
# default - значение, которое следует вернуть, если в словаре не окажется указанного ключа (по умолчанию None)
print(example_dict.get("unknown", list()))  # вернет [], тк ключа "unknown" нет (исключения KeyError никогда не будет)




