import socket
import threading
import re

def read_sock():
    global alias
    while True:
        data = sock.recv(1024).decode('utf-8')
        try:
            user_nickname = re.search("\[(.*)\]", data).group(0)
        except AttributeError:
            user_nickname = ''
        if user_nickname not in blocked_users:
            print(data)
        else:
            message = "@" + recipient + ", " + " you blocked by this user"
            sock.sendto(('[' + alias + '] ' + message).encode('utf-8'), server)

while True:
    server = ('192.168.0.109', 5051)
    alias = input("Your username: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 0))
    sock.sendto(("[" + alias + "] Connect to server").encode('utf-8'), server)
    answer = sock.recv(1024).decode('utf-8')
    if answer == 'You have wrong name, please try another one':
        print(answer)
        continue
    elif answer == 'Its fine':
        pass
    blocked_users = []

    potik = threading.Thread(target=read_sock)
    potik.start()

    while True:
        print('1. Group 2. Private 3. Block user')
        try:
            menu_choose = int(input(':'))
        except ValueError:
            continue
        if menu_choose == 1:
            message = input("Your message: ")
            sock.sendto(('[' + alias + '] ' + message).encode('utf-8'), server)
        elif menu_choose == 2:
            recipient = input('Recipient(Nickname): ')
            message = input("Your message: ")
            message = "@" + recipient + ", " + message
            sock.sendto(('[' + alias + '] ' + message).encode('utf-8'), server)
        elif menu_choose == 3:
            recipient = input('Which user you want to block ? (Nickname): ')
            blocked_users.append("[" + recipient + "]")
            print("User " + recipient + " blocked!")

