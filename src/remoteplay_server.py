"""
    todo:
        cleanup key_presser + send less data over network (String --> int)  [see win32con]
        write bat for starting client/server
        support controller
        (make prints toggleable)
        add different modes for handling multiple inputs

"""
import json
import pickle
import time

from Networking import networking
from Input import input_object
from Input import key_presser
from Input import mouse_mover

PORT = None  # loaded from server_config_file
IP = None  # loaded from server_config_file


key_input = input_object.InputObject()


def load_settings():
    global PORT, IP
    with open("../profiles/default_server.json", "r") as f:
        data = json.load(f)
        PORT = data["port"]
        IP = data["host-ip"]

    pass


def press_keys(data):
    global key_input
    key_input.deserialize_delta(data)

    delta = input_object.InputObject()
    delta.deserialize_delta(data)
    print(delta.key_inputs)
    key_presser.press(delta.key_inputs)

    mouse_mover.move(delta.scalar_inputs)


def received(data, respond, uuid):
    print("received:-", len(data), "-", "from", uuid)
    press_keys(data)


def connected(send, source):
    print("connected with", source)


if __name__ == "__main__":
    global server

    load_settings()

    print("running server on port", PORT, "...")

    server = networking.Server(PORT, received, callback_on_connection=connected, chunksize=64, host_ip=IP)
