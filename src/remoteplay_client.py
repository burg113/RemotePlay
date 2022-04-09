import time

import win32api

from Networking import networking
from Input import input_listener
from Input import input_object

# HOST = "127.0.0.1"
HOST = "79.244.152.71"
PORT = 5000

last_sync = time.time()


def received(data, respond, ip):
    print("received:-", data, "from", ip)


width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
midWidth = int((width + 1) / 2)
midHeight = int((height + 1) / 2)

if __name__ == "__main__":
    input_listener.run()

    client = networking.Client(HOST, PORT, received)

    while True:
        time.sleep(0.01)

        input_listener.update()

        if input_listener.input_obj.has_deltas():
            msg = input_listener.input_obj.serialize_delta()
            client.send(msg)

            print("sending")
            input_o = input_object.InputObject()
            input_o.deserialize(msg)
            print(input_o.key_inputs, "\t", msg)

