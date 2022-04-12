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
    if controls_data["enable_key_whitelist"]:
        input_listener.enable_key_whitelist = True
        input_listener.key_whitelist = controls_data["key_whitelist"]
    if controls_data["enable_key_blacklist"]:
        input_listener.enable_key_blacklist = True
        input_listener.key_blacklist = controls_data["key_blacklist"]

    if controls_data["enable_key_conversion"]:
        input_listener.enable_key_conversion = True
        input_listener.key_conversion_dict = controls_data["key_conversion"]


def load_settings():
    global HOST, PORT
    with open("../profiles/default_client.json", "r") as f:
        data = json.load(f)
        HOST = data["ip"]
        PORT = data["port"]

        controls_data = data["controls"]
        input_listener.enable_keyboard = controls_data["enable_keyboard"]
        input_listener.enable_mouse = controls_data["enable_mouse"]

        load_controls(controls_data)


def connected(send, source):
    with open("../profiles/default_client.json", "r") as f:
        data = json.load(f)

        print(data["client_id"])
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
            print(input_o.key_inputs, input_o.scalar_inputs, "\t\t\t\t\t", msg)
