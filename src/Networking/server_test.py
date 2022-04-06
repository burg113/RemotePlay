import networking

PORT = 5000


def recieved(uuid, data, send_back):
    print("received:-", data, "-", "from", uuid)
    send_back(data)


if __name__ == "__main__":
    networking.Server(PORT, recieved)
