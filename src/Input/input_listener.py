from Input import input_object
from Input import key_listener
from Input import mouse_listener

input_obj = input_object.InputObject()

suppress_inputs = True

control_config = None


def input(flag, key, value, is_scalar=False, is_delta=False):
    input_obj.control_config = control_config
    if flag == "Keyboard":
        input_obj.input(key, value, is_scalar, is_delta)
    if flag == "Mouse":
        input_obj.input("M." + str(key), value, is_scalar, is_delta)


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
    key_listener.run()

    mouse_listener.run()


if __name__ == "__main__":
    run()

    while True:
        pass
