from ahk import AHK

key_dict = {
    "Key.ctrl_l": "Lcontrol",
    "Key.space": "space",
    "Key.shift": "Lshift",
    "Key.caps_lock": "capsLock",
    "Key.cmd": "lwin",
    "Key.alt_l": "alt",
    "Key.tab": "tab",
    "Key.alt_gr": "altgr",
    "Key.ctrl_r": "Rcontrol",
    "Key.menu": "home",
    "Key.backspace": "backspace",
    "Key.enter": "enter",
    "Key.esc": "escape",

    "Key.shift_r": "Rshift",
    "Key.delete": "Delete",
    "Key.insert": "insert",
    "Key.scroll_lock": "ScrollLock",
    "Key.pause": "pause",
    "Key.print_screen": "PrintScreen",

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

mouse_key_dict = {
    "M.left": "LButton",
    "M.right": "RButton",
    "M.middle": "MButton",
}
mouse_wheel_dict = {
    "M.scroll_x": ("WheelDown", "WheelUp"),
    "M.scroll_y": ("WheelLeft", "WheelRight")
}

ahk = AHK()


def press(key_inputs):
    for k in key_inputs:
        key = ""
        if key_dict.__contains__(k):
            key = key_dict[k]
        elif mouse_key_dict.__contains__(k):
            key = mouse_key_dict[k]
        elif mouse_wheel_dict.__contains__(k):
            print(key_inputs)
            if key_inputs[k] == -1:
                key = mouse_wheel_dict[k][0]
                print("---1")
            if key_inputs[k] == 1:
                print("---2")
                key = mouse_wheel_dict[k][1]
            print("pressing:" + str(key))
            ahk.key_press(key)
            continue

        else:
            try:
                key = chr(int(k))
            except ValueError:
                print("key:", k, "could not be pressed")

        if key_inputs[k] == 1:
            print("pressing", key)
            ahk.key_down(key, False)

        if key_inputs[k] == 0:
            print("releasing", key)
            ahk.key_up(key, False)
