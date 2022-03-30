# Сокеты. Клиент-сервер
"""Сокеты - это кросс-платформенный механизм для обмена данными между отдельными процессами. Эти процессы могут работать
на разных серверах, могут быть написаны на разных языках. Программа на Python, которая использует механизм сокетов,
осуществляет системные вызовы и взаимодействует с ядром ОС.
Для организации сетевого взаимодействия нужен сервер, который изначально создает некое соединение, и начинает слушать
все запросы, которые поступают в него, и программа-клиент, которая присоединяется к серверу и отправляет ему нужные
данные."""


# Создание сокета, сервер
import socket  # для создания сокета импортируем модуль socket


# создаем объект socket, в него передаем некоторые параметры - константа AF_INET и тип сокета SOCK_STREAM(потоковый)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Передаем в метод bind адресную пару - host(передаем "127.0.0.1", те сервер будет слушать все входящие соединения
# только локально на одной машине, если указать пустую строку или адрес "0.0.0.0", то сервер будет слушать входящие
# соединения со всех интерфейсов) и порт(целочисленная константа, существуют зарезервированные порты)
sock.bind(("127.0.0.1", 10001))  # регистрирует адресную пару в ОС, max port 65535

# Чтобы начать принимать соединения необходимо вызвать метод listen, у которого есть необязательный параметр - так
# называемый backlog, или размер очереди входящих соединений, которые еще не обработаны, для которых не был вызван
# метод accept. Если сервер не будет успевать принимать входящие соединения, то все эти соединения будут копиться в этой
# очереди и если она превысит это максимальное значение, то ОС выдаст ошибку ConnectionRefused для клиентской программы
sock.listen(socket.SOMAXCONN)

# вызываем метод accept(), чтобы начать принимать входящее клиентское соединение
# системный вызов accept по умолчанию заблокируется до тех пор, пока не появится клиентское соединение
# Если клиент вызовет метод connect, то метод accept вернет объект, который будет являться полнодуплексным каналом, у
# этого объекта будут доступны методы записи в этот канал и методы чтения
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)  # чтение из полнодуплексного канала
    if not data:
        # если ничего не прочитали, это будет означать, что клиент закрыл соединение и нам тоже надо прекратить работу
        break

    # в качестве обработки данных, которые прочитали с канала, просто выводим их в консоль
    print(data.decode("utf8"))


################################################################################################################
"""
addr = ('127.0.0.1', 52063)
conn = <socket.socket fd=264, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, 
laddr=('127.0.0.1', 10001), raddr=('127.0.0.1', 52063)>
"""
print(f"addr = {addr}\n conn = {conn}")
################################################################################################################

# после того как закончили работу с клиентом вызываем метод close для нашего объекта, который представляет собой
# полнодуплексный канал и закрываем сокет, который слушает новые соединения со стороны клиента
conn.close()
sock.close()