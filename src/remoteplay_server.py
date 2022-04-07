"""

    keys being stuch when sending deltas


    key being held in all games

    key delay

    not getting proper inputs in game
    but minecraft chat working

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
last_sync= time.time()
SYNCDURATION=1

def press_keys(data):
    global last_sync
    global key_input
    """key_input.deserialize_delta(data)

    delta = input_object.InputObject()
    delta.deserialize_delta(data)
    print(delta.key_inputs)
    key_presser.press(delta)"""

    key_input.deserialize(data)
    key_presser.press(key_input)

    if time.time() - last_sync > SYNCDURATION:
        #key_presser.press(key_input)
        last_sync = time.time()
        print(10*"-------------------------------------------------------\n")
        print(key_input.key_inputs)
        print(10*"-------------------------------------------------------\n")





def received(uuid, data, send_back):
    # print("received:-", data, "-", "from", uuid)
     (data)


if __name__ == "__main__":
    networking.Server(PORT, received,host_ip="0.0.0.0")
