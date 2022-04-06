import socket
import uuid as unique_id
from multiprocessing import Process


class Server:
    sock = None
    callback = None

    def default_callback(self, uuid, conn, data):
        print("received:-", data, "-", "from", uuid, "no callback function configured")
        pass

    def on_new_client(self, conn, addr, uuid):
        print(f"Connected by {addr}", uuid)
        while True:
            data = conn.recv(1024)
            self.callback(uuid, conn, data)

    def __init__(self, host, port):
        self.callback = self.default_callback
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.bind((host, port))
        sock.listen()

        while True:
            print(0)
            conn, addr = sock.accept()
            print(1)
            p = Process(target=self.on_new_client, args=(conn, addr, unique_id.uuid4()))
            print(2)
            p.start()
            print(3)


"""        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
"""


class Client:
    callback = None
    sock = None

    def default_callback(data):
        print("received:-", data, "- no callback function configured")
        pass

    def __init__(self, host, port, callback=default_callback):
        self.callback = callback
        self.connect(host, port)

    def connect(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print("connected")
        sock.sendall(b"Hello, world")

        while True:
            data = sock.recv(1024)
            self.callback(data)
