"""
    todo:
        pressing mouse buttons over win32api
        write docs:     Client                  Server
                whitelist conversion--->conversion whitelist

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

client_ids = {}


def load_settings():
    global PORT, IP
    with open("../profiles/server_config.json", "r") as f:
        data = json.load(f)
        PORT = data["port"]
        IP = data["host-ip"]

    pass


def press_keys(data, controls):
    global key_input
    key_input.deserialize_delta(data)

    delta = input_object.InputObject()
    delta.deserialize_delta(data)
    print(delta.key_inputs)

    key_input.control_config = controls

    key_input.execute_deltas()


def received(data, respond, uuid):
    global client_ids
    if data.__contains__(b"client_id"):
        client_ids[uuid] = int(str(data.decode("utf-8")).replace("client_id ", ""))
    else:
        with open("../profiles/server_config.json", "r") as f:
            file_data = json.load(f)

            print("received:-", data, "-", "from", uuid)
            print(file_data["client_controls"][client_ids[uuid]])
            press_keys(data, file_data["client_controls"][client_ids[uuid]])


if __name__ == "__main__":
    global server

    load_settings()

    print("running server on port", PORT, "...")

    server = networking.Server(PORT, received, chunksize=64, host_ip=IP)
