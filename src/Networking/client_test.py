import networking

HOST = "127.0.0.1"
PORT = 5000


def received(data, send_back):
    print("received:-", data)

if __name__ == "__main__":
    client = networking.Client(HOST, PORT, received)
    client.send(b"Hello")
