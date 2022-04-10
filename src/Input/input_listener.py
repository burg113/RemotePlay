from Input import input_object
from Input import key_listener
from Input import mouse_listener

input_obj = input_object.InputObject()

suppress_inputs = True

enable_keyboard = True
enable_mouse = True

enable_key_whitelist = False
key_whitelist = []
enable_key_blacklist = False
key_blacklist = []

enable_key_conversion = False
key_conversion_dict = {}


def input(flag, key, value, is_scalar=False, is_delta=False):
    if flag == "Keyboard" and enable_keyboard:
        if (not enable_key_whitelist or key in key_whitelist) and \
                not (enable_key_blacklist and key in key_blacklist):
            if enable_key_conversion and key in key_conversion_dict:
                key = key_conversion_dict[key]

            input_obj.input(key, value, is_scalar, is_delta)
    if flag == "Mouse" and enable_mouse:
        input_obj.input(key, value, is_scalar, is_delta)


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
