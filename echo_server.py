import socket

try:
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP)

    address = ('127.0.0.1', 50000)
    server_socket.bind(address)
    server_socket.listen(1)
    while True:
        connection, client_address = server_socket.accept()
        buffersize = 32
        response = ''
        done = False
        while not done:
            msg_part = connection.recv(buffersize)
            if len(msg_part) < buffersize:
                done = True
            response += msg_part
        connection.sendall(response)
        connection.shutdown(socket.SHUT_WR)
        connection.close()

except KeyboardInterrupt:
    server_socket.close()
