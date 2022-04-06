import socket

def connect(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")

