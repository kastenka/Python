"""
Часто при зачислении каких-то средств на счет с нас берут комиссию. Давайте реализуем похожий механизм с
помощью дескрипторов. Напишите дескриптор Value, который будет использоваться в нашем классе Account.
"""
import os


class Value:
    def __init__(self):
        self.value = None

    def __set__(self, obj, value):
        self.value = value - value * obj.commission

    def __get__(self, obj, obj_type):
        return self.value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
print(new_account.commission)
new_account.amount = 100
print(new_account.amount)