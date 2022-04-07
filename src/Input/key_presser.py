from ahk import AHK

key_dict = {
    "Key.ctrl_l": "control",
    "Key.space": "space",
    "Key.shift": "shift",
    "Key.caps_lock": "capsLock",
    "Key.cmd": "command",
    "Key.alt_l": "alt",
    "Key.tab": "tab",
    "Key.alt_gr": "altgr",
    "Key.ctrl_r": "control",
    "Key.menu": "menu",
    "Key.backspace": "backspace",
    "Key.enter": "enter",
    "Key.esc": "e   scape",

    "Key.shift_r": "shift_r",
    "Key.delete": "delete",
    "Key.insert": "insert",
    "Key.scroll_lock": "scroll_lock",
    "Key.pause": "pause",
    "Key.print_screen": "print_screen",

    "Key.left": "left",
    "Key.right": "right",
    "Key.up": "up",
    "Key.down": "down",

    "Key.f1": "F1",
    "Key.f2": "F2",
    "Key.f3": "F3",
    "Key.f4": "F4",
    "Key.f5": "F5",
    "Key.f6": "F6",
    "Key.f7": "F7",
    "Key.f8": "F8",
    "Key.f9": "F9",
    "Key.f10": "F10",
    "Key.f11": "F11",
    "Key.f12": "F12"
}

ahk = AHK()


def press(key_object):
    for k in key_object.key_inputs:
        key = ""
        if key_dict.__contains__(k):
            key = key_dict[k]
        else:
            try:
                key = chr(int(k))
            except ValueError:
                print("key:", k, "could not be pressed")

        if key_object.key_inputs[k] == 1:
            print("pressing", key)
            ahk.key_down(key, False)

        if key_object.key_inputs[k] == 0:
            print("releasing", key)
            ahk.key_up(key, False)
