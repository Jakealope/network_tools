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
    buffersize = 16
    echomsg = client_socket.recv(buffersize)
    print echomsg
    client_socket.close()


if __name__ == '__main__':
    clientmessage(sys.argv[1])
