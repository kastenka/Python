import os
import csv


class CarBase:
    """Базовый класс"""
    required_attr = []  # атрибут для хранения обязательных параметров класса

    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = self.validate_photo_name(photo_file_name)
        self.brand = self.validate_data(brand)
        self.carrying = float(self.validate_data(carrying))

    def get_photo_file_ext(self):
        """Получить расширение файла. [0] - расположение файла, [1] - расширение файла"""
        ext = os.path.splitext(self.photo_file_name)[1]
        return ext

    def validate_data(self, attr_value):
        """Проверка данных на пустоту"""
        if not attr_value:
            return None
        return attr_value

    def validate_photo_name(self, filename):
        """Проверка наименования файла"""
        photo_ext = [".jpg", ".jpeg", ".png", ".gif"]
        for ext in photo_ext:
            if filename.endswith(ext) and (len(filename) > len(ext)):
                return filename
        raise ValueError

    @classmethod
    def create_from_dict(cls, data):
        """создает экземпляр класса из словаря с параметрами"""
        parameters = [data[parameter] for parameter in cls.required_attr]
        return cls(*parameters)


class Car(CarBase):
    """Класс, описывающий легковые автомобили"""
    car_type = "car"
    required_attr = ["brand", "photo_file_name", "carrying", "passenger_seats_count"]

    def __init__(self,  brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(self.validate_data(passenger_seats_count))


class Truck(CarBase):
    """Класс, описывающий автомобили для грузоперевозок"""
    car_type = "truck"
    required_attr = ["brand", "photo_file_name", "carrying", "body_whl"]

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.body_length, self.body_width, self.body_height = self.parse_body_whl(self.body_whl)

    def get_body_volume(self):
        """Возвращает объем кузова"""
        volume = self.body_length * self.body_width * self.body_height
        return volume

    def parse_body_whl(self, body_whl):
        """Вытаскиваем реальные размеры кузов из body_whl(в формате 2x3x4)"""
        try:
            whl = [float(par) for par in body_whl.split("x", 2)]
        except Exception:
            whl = 0.0, 0.0, 0.0
        return whl


class SpecMachine(CarBase):
    car_type = "spec_machine"
    required_attr = ["brand", "photo_file_name", "carrying", "extra"]

    """Класс, описывающий специальную технику"""
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = self.validate_data(extra)


def get_car_list(csv_filename):
    """возвращает список объектов, сохраненных в файле csv_filename"""
    car_types = {"car": Car, "spec_machine": SpecMachine, "truck": Truck}
    car_list = []
    csv.register_dialect("cars", delimiter=';')  # создаем и связываем диалект с именем "cars"

    with open(csv_filename, 'r') as file:
        reader = csv.DictReader(file, dialect="cars")  # DictReader отображает информацию о столбцах в словарь
        for row in reader:
            try:
                car_class = car_types[row['car_type']]
                car_list.append(car_class.create_from_dict(row))
            except Exception:
                pass

    return car_list

# Для тестирования работы класса
"""
car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')

truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width,
      truck.body_height, sep='\n')

spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name,
      spec_machine.extra, sep='\n')

print(spec_machine.get_photo_file_ext())
"""

cars = get_car_list('example.csv')
for car in cars:
    print(type(car))