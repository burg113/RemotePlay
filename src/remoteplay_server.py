from Networking import networking
from Input import input_object

PORT = 5000
key_input = input_object.InputObject()


def press_keys(data):
    key_input.deserialize_delta(data)
    print(key_input.key_inputs)


def received(uuid, data, send_back):
    ##print("received:-", data, "-", "from", uuid)
    press_keys(data)


if __name__ == "__main__":
    networking.Server(PORT, received)