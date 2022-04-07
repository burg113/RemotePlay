"""

    The default max length of a send bytestream is 16380 (128^2 - 2 - 1).
    It can be increased by setting

"""
import math
import socket
import uuid as unique_id
from multiprocessing import Process

MAX_MESSAGE_LENGTH = 8192

def send(conn, msg):
    conn.sendall(msg)


class Server:
    sock = None
    callback = None
    connections = []

    def default_callback(uuid, data, send_back):
        print("received:-", data, "-", "from", uuid, "no callback function configured")

    def __init__(self, port, callback=default_callback, chunksize=MAX_MESSAGE_LENGTH, host_ip="0.0.0.0"):
        self.callback = callback
        self.host(host_ip, port, chunksize)

    def host(self, host_ip, port, chunksize=MAX_MESSAGE_LENGTH):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.bind((host_ip, port))
        self.sock.listen()

        while True:
            conn, addr = self.sock.accept()
            p = Process(target=self.on_new_client, args=(conn, addr, unique_id.uuid4(), chunksize))
            self.connections.append([p, conn, addr])
            p.start()

    class Connection:
        conn = None

        def __init__(self, conn):
            self.conn = conn

        def send(self, msg):
            send(self.conn, msg)

    def on_new_client(self, conn, addr, uuid, chunksize):
        print(f"Connected: {addr}", uuid)
        while True:
            try:
                data = conn.recv(chunksize)
                connection = self.Connection(conn)
                self.callback(uuid, data, connection.send)
            except ConnectionResetError:
                break
        print(f"Disconnected: {addr}", uuid)

    def broadcast(self, msg):
        for connection in self.connections:
            process, conn, addr = connection
            if process.is_alive():
                conn.sendall(msg)


class Client:
    # callback, sock, process

    def default_callback(data, send_back):
        print("received:-", data, "- no callback function configured")
        pass

    def __init__(self, host, port, callback=default_callback, chunksize=MAX_MESSAGE_LENGTH):
        self.callback = callback
        self.connect(host, port, chunksize)

    def listen(self, sock, callback, chunksize=MAX_MESSAGE_LENGTH):
        while True:
            try:
                data = sock.recv(32768)
                callback(data, self.send)
            except ConnectionResetError:
                break
        print(f"Disconnected")

    def connect(self, host, port,chunksize=MAX_MESSAGE_LENGTH):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        print("connected")

        self.process = Process(target=self.listen, args=(self.sock, self.callback,chunksize))
        self.process.start()

    def send(self, data):
        send(self.sock, data)
