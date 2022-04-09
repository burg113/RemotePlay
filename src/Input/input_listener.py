from Input import input_object
from Input import key_listener
from Input import mouse_listener

input_obj = input_object.InputObject()

suppress_inputs = True

enable_keyboard = True
enable_mouse = True


def toggle_suppress_inputs():
    do_suppress_inputs(not suppress_inputs)


def do_suppress_inputs(val=True):
    global suppress_inputs
    suppress_inputs = val

    mouse_listener.do_suppress_inputs(val)
    key_listener.do_suppress_inputs(val)


def get_mouse_delta():
    mouse_listener.get_mouse_delta()


def update():
    if enable_mouse:
        mouse_listener.update()


def run():
    if enable_keyboard:
        key_listener.run()

    if enable_mouse:
        mouse_listener.run()


if __name__ == "__main__":
    run()

    while True:
        pass
