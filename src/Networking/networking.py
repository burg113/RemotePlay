import socket


class Server:

    def __init__(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


class Client:

    def default_callback(self):
        pass

    callback = default_callback

    def __init__(self, host, port,callback):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(b"Hello, world")

        while True:
            data = s.recv(1024)
            callback(data)
