"""
    todo:
        test multiple input computers
        change output library to -Auto Hot Key-
        support mouse
        support controller
        make program customisable though jsons
        make prints toggleable
        add different modes for handling multiple inputs
        block keys for users

"""

import time

from Networking import networking
from Input import input_object
from Input import key_presser
import pynput

PORT = 5000
global key_input
key_input = input_object.InputObject()

global last_sync
last_sync = time.time()
SYNCDURATION = 1


def press_keys(data):
    global last_sync
    global key_input
    key_input.deserialize_delta(data)

    delta = input_object.InputObject()
    delta.deserialize_delta(data)
    print(delta.key_inputs)
    key_presser.press(delta)


""" if time.time() - last_sync > SYNCDURATION:
        # key_presser.press(key_input)
        last_sync = time.time()
        print("-------------------------------------------------------\n")
        print(key_input.key_inputs)
        print("-------------------------------------------------------\n")
"""


def received(data, respond, uuid):
    print("received:-", data, "-", "from", uuid)
    press_keys(data)


if __name__ == "__main__":
    global server
    server = networking.Server(PORT, received, host_ip="0.0.0.0")
