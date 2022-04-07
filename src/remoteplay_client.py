import time

from Networking import networking
from Input import key_listener

# HOST = "127.0.0.1"

HOST = "80.137.72.11"
PORT = 5000

last_sync = time.time()
SYNCS_PER_SECOND = 1


def received(data, respond, ip):
    print("received:-", data, "from", ip)


if __name__ == "__main__":
    key_listener.run()

    client = networking.Client(HOST, PORT, received)

    while True:
        time.sleep(0.01)
        if key_listener.input_obj.has_deltas():
            client.send(key_listener.input_obj.serialize_delta())

        if time.time() - last_sync > 1 / SYNCS_PER_SECOND:
            for chunk in key_listener.input_obj.serialize_chunks(4):
                client.send(chunk)
