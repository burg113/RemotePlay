"""
    todo:
        support controller
        make program customisable though jsons
        (make prints toggleable)
        add different modes for handling multiple inputs

"""
import json
import time

from Networking import networking
from Input import input_object
from Input import key_presser
from Input import mouse_mover

PORT = 5000
global key_input
key_input = input_object.InputObject()


def load_settings():
    global PORT
    with open("../profiles/default.json", "r") as f:
        data = json.load(f)
        PORT = data["port"]

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
    print("received:-", data, "-", "from", uuid)
    press_keys(data)


if __name__ == "__main__":
    global server

    load_settings()

    print("running server on port", PORT, "...")

    server = networking.Server(PORT, received, host_ip="0.0.0.0")

