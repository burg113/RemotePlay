import socket
import uuid as unique_id
from multiprocessing import Process


class Server:
    sock = None
    callback = None
    connections = []

    def default_callback(uuid, data, send_back):
        print("received:-", data, "-", "from", uuid, "no callback function configured")

    def __init__(self, port, callback=default_callback, chunksize=1024, host_ip="127.0.0.1"):
        self.callback = callback
        self.host(host_ip, port, chunksize)

    def host(self, host_ip, port, chunksize=1024):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.bind((host_ip, port))
        self.sock.listen()

        while True:
            conn, addr = self.sock.accept()
            p = Process(target=self.on_new_client, args=(conn, addr, unique_id.uuid4(), chunksize))
            self.connections.append([p, conn, addr])
            p.start()

    def on_new_client(self, conn, addr, uuid, chunksize):
        print(f"Connected: {addr}", uuid)
        while True:
            try:
                data = conn.recv(chunksize)
                self.callback(uuid, data, conn.sendall)
            except ConnectionResetError:
                break
        print(f"Disconnected: {addr}", uuid)

    def broadcast(self, msg):
        for connection in self.connections:
            process, conn, addr = connection
            if process.is_alive():
                conn.sendall(msg)


class Client:
    callback = None
    sock = None

    def default_callback(data, send_back):
        print("received:-", data, "- no callback function configured")
        pass

    def __init__(self, host, port, callback=default_callback):
        self.callback = callback
        self.connect(host, port)

    def connect(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        print("connected")
        self.sock.sendall(b"Hello, world")

        while True:
            data = self.sock.recv(1024)
            self.callback(data, self.sock.sendall)

    def send(self, data):
        self.sock.sendall(data)
