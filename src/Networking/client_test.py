import networking

HOST = "127.0.0.1"
PORT = 5000


def recieved(data, send_back):
    print("received:-", data)


if __name__ == "__main__":
    networking.Client(HOST, PORT, recieved)
