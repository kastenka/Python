# Методы. Часть 2
# Вычисляемые свойства класса(property)

# свойства позволяют изменять поведение и выполнять какую-то вычислительную работу при обращении к атрибуту экземпляра,
# либо при изменении атрибута, либо при его удалении
class Robot:

    def __init__(self, power):
        self.power = power

    # метод, который будет проверять, чтобы мощность не была меньше 0
    def set_power(self, power):
        if power < 0:
            self.power = 0
        else:
            self.power = power


wall_e = Robot(100)
wall_e.power = -20
print(wall_e.power)  # -20