import pynput
from ahk import AHK

ahk = AHK()


def move(scalar_inputs):
    mouse_x_delta = 0
    mouse_y_delta = 0
    print("hi")
    if scalar_inputs.__contains__("MouseXDelta"):
        mouse_x_delta += scalar_inputs["MouseXDelta"]
    if scalar_inputs.__contains__("MouseYDelta"):
        mouse_y_delta += scalar_inputs["MouseYDelta"]

    ahk.mouse_move((mouse_x_delta, mouse_y_delta), relative=True, blocking=False)
