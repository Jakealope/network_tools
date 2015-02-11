import socket
import sys


def clientmessage(msg):

    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)
    client_socket.connect(('127.0.0.1', 50000))
    client_socket.sendall(msg)
    client_socket.shutdown(socket.SHUT_WR)
    buffsize = 32
    response = ''
    done = False
    while not done:
        msg_part = client_socket.recv(buffsize)
        if len(msg_part) < buffsize:
            done = True
            client_socket.close()
        response += msg_part
    return response


if __name__ == '__main__':
    clientmessage(sys.argv[1])
