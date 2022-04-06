import time

from Networking import networking
from Input import key_listener

HOST = "127.0.0.1"
PORT = 5000

def received(data, send_back):
    print("received:-", data)


if __name__ == "__main__":
    key_listener.run()


    client = networking.Client(HOST, PORT, received)


    while True:
        time.sleep(0.01)
        client.send(key_listener.input_obj.serialize_delta())

