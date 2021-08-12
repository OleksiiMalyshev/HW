import socket
import threading
from PIL import Image
import os


def read_sock():
    while True:
        data = sock.recv(1024)
        part = data
        if part == b'Send_files':
            bytesss = b''
            while part != b'Sent':
                part = sock.recv(1024)
                bytesss += part
            b = open('downloaded_file.txt', 'wb')
            b.write(bytesss)
            b.close()

            path_to_file = 'downloaded_file.txt'
            save_path = path_to_file.replace('.txt', '.jpg')
            with open(path_to_file, 'rb') as textfile:
                bytestring = textfile.read()

            with open(save_path, 'wb') as imagefile:
                imagefile.write(bytestring)

            image = Image.open(save_path)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'downloaded_file.txt')
            os.remove(path)

        else:
            decoded_data = data.decode('utf-8')
            print(decoded_data)


def send_file():
    file = input('Write path to file - ')
    file_to_send = open(file, 'rb')
    bytess = file_to_send.readlines()
    file_to_send.close()
    new_bytess = b''
    for _ in bytess:
        new_bytess += _
    start = 0
    end = 1024
    sock.sendto(b'Send_files', server)
    while end < len(new_bytess):
        sock.sendto((new_bytess[start:end]), server)
        start = end
        end += 1024
    sock.sendto(b'Sent', server)


server = ('192.168.0.100', 1021)
alias = input("Your username: ")
print('To send file type "Send_file')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))
sock.sendto((alias + " Connect to server").encode('utf-8'), server)

potik = threading.Thread(target=read_sock)
potik.start()

while True:
    message = input("Your message: ")
    if message == 'Send_file':
        send_file()
    else:
        sock.sendto(('[' + alias + '] ' + message).encode('utf-8'), server)
