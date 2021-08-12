import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.0.100', 1021))
clients = []
print("Server start")
while True:
    data, address = sock.recvfrom(1024)
    print(address[0], address[1])
    if address not in clients:
        clients.append(address)
    for client in clients:
        if client == address:
            continue
        sock.sendto(data, client)