"""
В этом задании вам нужно создать интерфейс для работы с файлами. Интерфейс должен предоставлять следующие
возможности по работе с файлами:
- чтение из файла, метод read возвращает строку с текущим содержанием файла
- запись в файл, метод write принимает в качестве аргумента строку с новым содержанием файла
- сложение объектов типа File, результатом сложения является объект класса File, при этом создается новый файл и
файловый объект, в котором содержимое второго файла добавляется к содержимому первого файла. Новый файл должен
создаваться в директории, полученной с помощью функции tempfile.gettempdir. Для получения нового пути можно
использовать os.path.join.
- возвращать в качестве строкового представления объекта класса File полный путь до файла
- поддерживать протокол итерации, причем итерация проходит по строкам файла
При создании экземпляра класса File в конструктор передается полный путь до файла на файловой системе.
Если файла с таким путем не существует, он должен быть создан при инициализации.
"""
import os
import tempfile
import uuid


class File:

    def __init__(self, filepath):
        self.filepath = filepath
        self.current_position = 0

        if not os.path.exists(self.filepath):
            open(filepath, "w").close()

    def read(self):
        with open(self.filepath, "r") as f:
            return f.read()

    def write(self, new_string):
        with open(self.filepath, "w") as f:
            f.write(new_string)

    def __add__(self, obj):
        file_path = os.path.join(
            tempfile.gettempdir(),
            str(uuid.uuid4()))
        """
        file_path = os.path.join(
            os.path.dirname(self.filepath), 
            str(uuid.uuid4().hex))
        """
        new_obj = type(self)(file_path)
        new_obj.write(self.read() + obj.read())
        return new_obj

    def __str__(self):
        return f"{self.filepath}"

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.filepath, "r") as file:
            file.seek(self.current_position)  # перемещаем указатель текущей позиции в файле на self.current_position
            result = file.readline()  # считываем одну строку
            self.current_position = file.tell()  # для self.current_position возвращаем текщую позицию указателя
            if not result:
                self.current_position = 0
                raise StopIteration
            return result


# Тестирование программы

path_to_file = 'some_filename'
print(os.path.exists(path_to_file))  # False

file_obj = File(path_to_file)
print(os.path.exists(path_to_file))  # True

print(file_obj)  # some_filename
print(file_obj.read())  # ""
file_obj.write('some text')
print(file_obj.read())  # "some text"
file_obj.write('other text')
print(file_obj.read())  # "other text"

file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
file_obj_1.write('line 1\n')
file_obj_2.write('line 2\n')
new_file_obj = file_obj_1 + file_obj_2
print(isinstance(new_file_obj, File))  # True

print(new_file_obj)  # C:\Users\masha\AppData\Local\Temp\3a47e663-28a8-46fc-a770-0a926861a7d1

for line in new_file_obj:
    print(ascii(line))  # выведет построчно данные из файла: 'line 1\n', 'line 2\n'

new_path_to_file = str(new_file_obj)
print(os.path.exists(new_path_to_file))  # True

file_obj_3 = File(new_path_to_file)
print(file_obj_3)  # C:\Users\masha\AppData\Local\Temp\3a47e663-28a8-46fc-a770-0a926861a7d1
