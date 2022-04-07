import pynput
from pynput.keyboard import Key


keyboard = pynput.keyboard.Controller()

key_dict = {
    "Key.ctrl_l": Key.ctrl_l,
    "Key.space": Key.space,
    "Key.shift": Key.shift,
    "Key.caps_lock": Key.caps_lock,
    "Key.cmd": Key.cmd,
    "Key.alt_l": Key.alt_l,
    "Key.tab": Key.tab,
    "Key.alt_gr": Key.alt_gr,
    "Key.ctrl_r": Key.ctrl_r,
    "Key.menu": Key.menu,

    "Key.left": Key.left,
    "Key.right": Key.right,
    "Key.up": Key.up,
    "Key.down": Key.down,

    "Key.backspace": Key.backspace,
    "Key.enter": Key.enter,
    "Key.esc": Key.esc,
    "Key.shift_r": Key.shift_r,
    "Key.delete": Key.delete,
    "Key.insert": Key.insert,
    "Key.scroll_lock": Key.scroll_lock,
    "Key.pause": Key.pause,
    "Key.print_screen": Key.print_screen,

    "Key.f1": Key.f1,
    "Key.f2": Key.f2,
    "Key.f3": Key.f3,
    "Key.f4": Key.f4,
    "Key.f5": Key.f5,
    "Key.f6": Key.f6,
    "Key.f7": Key.f7,
    "Key.f8": Key.f8,
    "Key.f9": Key.f9,
    "Key.f10": Key.f10,
    "Key.f11": Key.f11,
    "Key.f12": Key.f12
}


def press(key_object):
    for k in key_object.key_inputs:
        key = None
        if key_dict.__contains__(k):
            key = key_dict[k]
        else:
            try:
                key = pynput.keyboard.KeyCode(int(k))
            except ValueError:
                print("cannot press", k)
                return
        if key_object.key_inputs[k] == 1:
            keyboard.press(key)
        if key_object.key_inputs[k] == 0:
            keyboard.release(key)
