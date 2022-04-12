# todo: fix scrolling

import pynput
import win32api
from Input import input_listener
from pynput.mouse import Controller

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
midWidth = int((width + 1) / 2)
midHeight = int((height + 1) / 2)

mouse_controller = Controller()

listener = None


def do_suppress_inputs(val):
    win32api.SetCursorPos((midWidth, midHeight))
    listener._suppress = val


def on_move(x, y):
    if input_listener.suppress_inputs:
        input_listener.input("Mouse", "x", x, is_scalar=True, is_delta=True)
        input_listener.input("Mouse", "y", y, is_scalar=True, is_delta=True)

        win32api.SetCursorPos((0, 0))
        pass


def on_click(x, y, button, pressed):
    if input_listener.suppress_inputs:
        input_listener.input("Mouse", str(button).replace("Button.", ""), pressed)


def on_scroll(x, y, dx, dy):
    if input_listener.suppress_inputs:
        input_listener.input("Mouse", "scroll_x", dx, repeat_clicks=True)
        input_listener.input("Mouse", "scroll_y", dy, repeat_clicks=True)


def run():
    global listener
    listener = pynput.mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll,
        suppress=True)
    listener.start()
    win32api.SetCursorPos((0, 0))
