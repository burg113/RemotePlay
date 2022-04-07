from Input import input_object
from Input import key_listener
from Input import mouse_listener

input_obj = input_object.InputObject()

def run():
    key_listener.run()
    mouse_listener.run()


if __name__ == "__main__":
    run()

    while True:
        pass
