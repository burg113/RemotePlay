import time

from Input import input_listener
from pynput.mouse import Button, Controller
import mouse

mouse_controller = Controller()
mouse_delta = (0, 0)


def get_mouse_delta():
    global mouse_delta, mouse_controller

    print("\t\t\t\t\t\t", input_listener.input_obj.scalar_inputs_delta)
    time.sleep(0.01)

    new_mouse_position = mouse_controller.position
    mouse_delta = (new_mouse_position[0] - 500, new_mouse_position[1] - 500)
    input_listener.input_obj.input("MouseXDelta", mouse_delta[0], is_scalar=True, is_delta=True)
    input_listener.input_obj.input("MouseYDelta", mouse_delta[1], is_scalar=True, is_delta=True)

#    mouse.move(1, 1, absolute=False)

