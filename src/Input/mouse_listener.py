# todo: fix scrolling

import pynput
import win32api
from Input import input_listener

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
midWidth = int((width + 1) / 2)
midHeight = int((height + 1) / 2)
from pynput.mouse import Button, Controller

mouse_controller = Controller()


def update():
    if input_listener.suppress_inputs:

        # somehow hide cursor?!

        print("\t\t\t", input_listener.input_obj.scalar_inputs_delta)

        new_mouse_position = mouse_controller.position
        mouse_delta = (new_mouse_position[0] - midWidth, new_mouse_position[1] - midHeight)

        print(mouse_delta)
        input_listener.input_obj.input("MouseXDelta", mouse_delta[0], is_scalar=True, is_delta=True)
        input_listener.input_obj.input("MouseYDelta", mouse_delta[1], is_scalar=True, is_delta=True)

        win32api.SetCursorPos((midWidth, midHeight))

    else:
        # somehow show cursor
        pass


def on_move(x, y):
    pass


def on_click(x, y, button, pressed):
    input_listener.input_obj.input(str(button).replace("Button","M"), pressed)


def on_scroll(x, y, dx, dy):
    input_listener.input_obj.input("M.scroll_x", dx)
    input_listener.input_obj.input("M.scroll_y", dy)


def run():
    listener = pynput.mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)
    listener.start()
