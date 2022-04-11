"""
    The default max length of a converted bytestream is 16383 (128^2 - 1).

    control bytes               message length
         1						 127 	 B
         2						 16.0 	 KB
         3						 2.0 	 MB
         4						 256.0 	 MB
         5						 32.0 	 GB
         6						 4.0 	 TB
         7						 512.0 	 TB
         8						 64.0 	 PB
"""

import math
import socket
import uuid as unique_id
from multiprocessing import Process

SOCKET_CHUNK_SIZE = 2048

MAX_MESSAGE_LENGTH = 16383
CONTROL_BYTE_LENGTH = math.ceil(math.log(MAX_MESSAGE_LENGTH, 128))


def int_to_bytes(i, n=CONTROL_BYTE_LENGTH):
    b = b''
    for c in range(n):
        print(c, "--", int((i / 128 ** c) % 128))
        b += chr(int((i / 128 ** c) % 128)).encode()
    return b


def int_from_bytes(b):
    i = 0
    for c in range(len(b)):
        i += b[c] * 128 ** c
    return i


def send(conn, msg, control_bytes=CONTROL_BYTE_LENGTH):
    if type(msg) == str:
        msg = bytes(msg, 'utf-8')

    header = int_to_bytes(len(msg), control_bytes)
    conn.sendall(header + msg)


def listen(self, conn, context, respond):
    buffer = b""
    while True:
        try:
            try:
                buffer += conn.recv(self.CHUNK_SIZE)
                while len(buffer) >= CONTROL_BYTE_LENGTH:
                    total_length = int_from_bytes(buffer[:self.CONTROL_BYTE_LENGTH]) + self.CONTROL_BYTE_LENGTH
                    if len(buffer) >= total_length:
                        data = buffer[self.CONTROL_BYTE_LENGTH:total_length]
                        buffer = buffer[total_length:]
                        self.callback(data, respond, context)
                    else:
                        break
            except TypeError as e:
                print(e)
        except ConnectionResetError:
            break


def default_callback(data, respond, source):
    print("received:-", data, "-", "from", source, "no callback function configured")


def default_callback_on_connection(send, source):
    print("new connection from", source, ". no callback function configured")


class Server:

    def __init__(self, port, callback=default_callback, callback_on_connection=default_callback_on_connection,
                 chunksize=SOCKET_CHUNK_SIZE, host_ip="0.0.0.0", blocking=True):
        self.callback = callback
        self.callback_on_connection = callback_on_connection
        self.CONTROL_BYTE_LENGTH = CONTROL_BYTE_LENGTH
        self.CHUNK_SIZE = chunksize

        self.sock = None
        self.connections = []
        self.process = None

        self.host(host_ip, port, blocking)

    def host(self, host_ip, port, blocking=True):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.bind((host_ip, port))
        self.sock.listen()

        self.process = Process(target=self.run)
        self.process.start()
        if blocking:
            self.process.join()

    def run(self):
        while True:
            conn, addr = self.sock.accept()
            this_id = unique_id.uuid4()
            p = Process(target=self.on_new_client, args=(conn, addr, this_id))
            self.connections.append((conn, addr, this_id))
            p.start()

    class Connection:
        conn = None

        def __init__(self, conn):
            self.conn = conn

        def send(self, msg):
            send(self.conn, msg)

    def on_new_client(self, conn, addr, id):
        print(f"Connected: {addr}", id)
        connection = self.Connection(conn)

        self.callback_on_connection(connection.send, id)

        listen(self, conn, id, connection.send)

        for c in range(len(self.connections)):
            connection = self.connections[c]
            _, _, some_id = connection
            if some_id is id:
                self.connections.remove(connection)

        print(f"Disconnected: {addr}", id)

    def broadcast(self, msg):
        for connection in self.connections:
            conn, addr, uuid = connection
            try:
                send(conn, msg)
            except ConnectionResetError:

                pass

    def join(self):
        self.process.join()

    def set_max_message_length(self, length):
        self.CONTROL_BYTE_LENGTH = math.ceil(math.log(length + math.ceil(math.log(length, 128)), 128))


class Client:

    def __init__(self, host, port, callback=default_callback, callback_on_connection=default_callback_on_connection,
                 chunksize=SOCKET_CHUNK_SIZE, blocking=True):
        self.callback = callback
        self.callback_on_connection = callback_on_connection

        self.CONTROL_BYTE_LENGTH = CONTROL_BYTE_LENGTH
        self.CHUNK_SIZE = chunksize
        self.host_ip = host

        self.sock = None
        self.process = None

        self.connect(host, port, blocking)

    def on_connection(self, sock):
        print("Connected")
        self.callback_on_connection(send, self.host_ip)
        listen(self, sock, self.host_ip, send)

        print(f"Disconnected")

    def connect(self, host, port, blocking=True):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        self.process = Process(target=self.on_connection, args=(self.sock,))
        self.process.start()

        if blocking:
            self.process.join()

    def send(self, data):
        send(self.sock, data)

    def join(self):
        self.process.join()
