# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import socket
import email.utils


def response_ok(request):
    response_code = "HTTP/1.1 200 OK"
    date = "Date: {}".format(email.utils.formatdate(usegmt=True))
    headers = "Content-Type Text/HTML"
    response = "{}\r\n{}\r\n{}\r\n\r\n".format(response_code, date, headers)
    return response.encode('utf-8')


def response_error(code, reason):
    response_code = "HTTP/1.1 {} {}".format(code, reason)
    date = "Date: {}".format(email.utils.formatdate(usegmt=True))
    headers = "Content-Type:Text/HTML"
    response = "{}\r\n{}\r\n{}\r\n\r\n".format(response_code, date, headers)
    return response.encode('utf-8')


def parse_request(request):
    request = request.split('\r\n')
    first_line = request[0].split(' ')
    if first_line[0] != "GET":
        return response_error(405, "Request not allowed")
    if first_line[2] != "HTTP/1.1":
        return response_error(505, "Invalid protocol")
    return response_ok(first_line[1])

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
        buffersize = 4096
        response = ''
        done = False
        while not done:
            msg_part = connection.recv(buffersize)
            if len(msg_part) < buffersize:
                done = True
            response += msg_part

            response = parse_request(response)

        connection.sendall(response)
        connection.shutdown(socket.SHUT_WR)
        connection.close()

except KeyboardInterrupt:
    server_socket.close()
