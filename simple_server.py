from socket import *

socket_object = socket(AF_INET, SOCK_STREAM)
socket_object.bind(('', 5400))
socket_object.listen(5)  # до 5 клиентов в очереди

print('Server - started')
while True:
    connection, address = socket_object.accept()  # ждём от клиента сообщения
    bin_data = connection.recv(1024)  # получаем сообщение от клиента
    data = bin_data.decode('utf-8')  # расшифровываем сообщение

    ip_address = address[0]  # получаем ip клиента

    if data == 'hello':
        str_answer = 'Hi!'
    else:
        str_answer = 'Я получиль ' + data + " от " + ip_address + ". Длинной " + str(len(data)) + ' байт'

    connection.send(str_answer.encode('utf-8'))  # отправляем сообщение клиенту
    connection.close()
