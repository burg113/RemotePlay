from Networking import networking
from Input import input_object
from Input import key_presser
import pynput

PORT = 5000
key_input = input_object.InputObject()



def press_keys(data):
    key_input.deserialize_delta(data)

    delta = input_object.InputObject()
    delta.deserialize_delta(data)
    print(delta.key_inputs)
    key_presser.press(delta)



def received(uuid, data, send_back):
    # print("received:-", data, "-", "from", uuid)
    press_keys(data)


if __name__ == "__main__":
    networking.Server(PORT, received,host_ip="0.0.0.0")
