'''
    Сервер для консольной игры "Бойцовский Клуб".

    Протокол общения:
        "_место_удара_ _защищаемое_место_"  - ход игрока
'''

from socket import *

# Настройка сокета
socket_object = socket(AF_INET, SOCK_STREAM)
# Обработка сигналов от клиента
socket_object.bind(('', 5400))
socket_object.listen(5)  # до 5 клиентов в очереди

print('Сервер - работает.')

while True:
    # Ждём соединения от клиента
    connection, address = socket_object.accept()
    # Получаем данные от клиента
    bin_data = connection.recv(1024)
    str_data = bin_data.decode('utf-8')     # 1-4 1-4

    print(str_data)

    # получаем ip клиента
    ip_address = address[0]

    # Список с местами для удара/защиты
    hit_markers = ['голова', "торс", "пояс", "ноги"]
    "3 2"
    data_list = str_data.split()    # формируем список команд от клиента
    msg_hit = int(data_list[0])     # Выделяем номер места для удара
    msg_block = int(data_list[1])   # Выделяем номер места для защиты

    # Формируем сообщение для ответа клиенту
    answer = f'Игрок 1 ударил в {hit_markers[msg_hit]} защитил {hit_markers[msg_block]}'

    # Отправляем ответ клиенту
    connection.send(answer.encode('utf-8'))
    connection.close()
