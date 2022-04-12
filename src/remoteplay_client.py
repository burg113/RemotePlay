import json
import time

import win32api

from Networking import networking
from Input import input_listener
from Input import input_object

HOST = ""
PORT = 0

last_sync = time.time()


def received(data, respond, ip):
    print("received:-", data, "from", ip)


width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
midWidth = int((width + 1) / 2)
midHeight = int((height + 1) / 2)


def load_controls(controls_data):
        input_listener.control_config = controls_data


def load_settings():
    global HOST, PORT
    with open("../profiles/client_config.json", "r") as f:
        data = json.load(f)
        HOST = data["ip"]
        PORT = data["port"]

        controls_data = data["controls"]
        input_listener.enable_keyboard = controls_data["enable_keyboard"]
        input_listener.enable_mouse = controls_data["enable_mouse"]

        load_controls(controls_data)


def connected(send, source):
    with open("../profiles/client_config.json", "r") as f:
        data = json.load(f)

        send("client_id " + str(data["client_id"]))


if __name__ == "__main__":

    load_settings()

    input_listener.run()

    client = networking.Client(HOST, PORT, received, callback_on_connection=connected, blocking=False)

    while True:
        time.sleep(0.01)

        if input_listener.input_obj.has_deltas():
            msg = input_listener.input_obj.serialize_delta()

            client.send(msg)

            print("sending")
            input_o = input_object.InputObject()
            input_o.deserialize(msg)
            print(input_o.key_inputs, input_o.scalar_inputs)
