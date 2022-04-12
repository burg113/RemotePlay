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
        input_listener.input("Mouse", "MouseXDelta", x, is_scalar=True, is_delta=True)
        input_listener.input("Mouse", "MouseYDelta", y, is_scalar=True, is_delta=True)

        win32api.SetCursorPos((0, 0))
        pass


def on_click(x, y, button, pressed):
    if input_listener.suppress_inputs:
        input_listener.input("Mouse", str(button).replace("Button", "M"), pressed)


def on_scroll(x, y, dx, dy):
    if input_listener.suppress_inputs:
        input_listener.input("Mouse", "M.scroll_x", dx)
        input_listener.input("Mouse", "M.scroll_y", dy)


def run():
    global listener
    listener = pynput.mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll,
        suppress=True)
    listener.start()
    win32api.SetCursorPos((0, 0))
