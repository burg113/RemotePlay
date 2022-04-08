import time

import win32api
from Input import input_listener
from pynput.mouse import Button, Controller

mouse_controller = Controller()
mouse_delta = (0, 0)

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
midWidth = int((width + 1) / 2)
midHeight = int((height + 1) / 2)


def get_mouse_delta():
    global mouse_delta, mouse_controller
    win32api.ShowCursor(False)
    if input_listener.suppress_inputs:
        # mouse.visible = False
        win32api.SetCursorPos((midWidth, midHeight))

        print("\t\t\t", input_listener.input_obj.scalar_inputs_delta)
        time.sleep(0.01)

        new_mouse_position = mouse_controller.position
        mouse_delta = (new_mouse_position[0] - midWidth, new_mouse_position[1] - midHeight)
        input_listener.input_obj.input("MouseXDelta", mouse_delta[0], is_scalar=True, is_delta=True)
        input_listener.input_obj.input("MouseYDelta", mouse_delta[1], is_scalar=True, is_delta=True)


