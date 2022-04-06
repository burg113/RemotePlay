import networking

PORT = 5000


def received(uuid, data, send_back):
    print("received:-", data, "-", "from", uuid)
    send_back(data)


if __name__ == "__main__":
    networking.Server(PORT, received)
