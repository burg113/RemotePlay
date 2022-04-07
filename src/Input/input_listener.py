from Input import input_object
from Input import key_listener
from Input import mouse_listener

input_obj = input_object.InputObject()


def get_mouse_delta():
    mouse_listener.get_mouse_delta()


def run():
    key_listener.run()


if __name__ == "__main__":
    run()

    while True:
        pass
