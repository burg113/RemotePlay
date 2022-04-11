import time

import win32api
import win32con
from ahk import AHK

key_dict = {
    "Key.ctrl_l": "Lcontrol",
    "Key.space": "space",
    "Key.shift": "Lshift",
    "Key.caps_lock": "capsLock",
    "Key.cmd": "Lwin",
    "Key.alt_l": "alt",
    "Key.tab": "tab",
    "Key.alt_gr": "altgr",
    "Key.ctrl_r": "Rcontrol",
    "Key.menu": "home",
    "Key.backspace": "backspace",
    "Key.enter": "enter",
    "Key.esc": "escape",

    "Key.shift_r": "Rshift",
    "Key.delete": "delete",
    "Key.insert": "insert",
    "Key.scroll_lock": "scrollLock",
    "Key.pause": "pause",
    "Key.print_screen": "printScreen",

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
    "Key.f12": "F12",

    "Key.page_up": "a",
    "Key.page_down": "b",
    "Key.end": "end",
    "Key.home": "home",

}

VK_CODE = {'backspace': 0x08,
           'tab': 0x09,
           'clear': 0x0C,
           'enter': 0x0D,
           'shift': 0x10,
           'ctrl': 0x11,
           'alt': 0x12,
           'altgr': 0x12,
           'pause': 0x13,
           'capsLock': 0x14,
           'escape': 0x1B,
           'space': 0x20,
           'pageUp': 0x21,
           'pageDown': 0x22,
           'end': 0x23,
           'home': 0x24,
           'left': 0x25,
           'up': 0x26,
           'right': 0x27,
           'down': 0x28,
           'select': 0x29,
           'print': 0x2A,
           'execute': 0x2B,
           'printScreen': 0x2C,
           'insert': 0x2D,
           'delete': 0x2E,
           'help': 0x2F,
           '0': 0x30,
           '1': 0x31,
           '2': 0x32,
           '3': 0x33,
           '4': 0x34,
           '5': 0x35,
           '6': 0x36,
           '7': 0x37,
           '8': 0x38,
           '9': 0x39,
           'a': 0x41,
           'b': 0x42,
           'c': 0x43,
           'd': 0x44,
           'e': 0x45,
           'f': 0x46,
           'g': 0x47,
           'h': 0x48,
           'i': 0x49,
           'j': 0x4A,
           'k': 0x4B,
           'l': 0x4C,
           'm': 0x4D,
           'n': 0x4E,
           'o': 0x4F,
           'p': 0x50,
           'q': 0x51,
           'r': 0x52,
           's': 0x53,
           't': 0x54,
           'u': 0x55,
           'v': 0x56,
           'w': 0x57,
           'x': 0x58,
           'y': 0x59,
           'z': 0x5A,
           'numpad_0': 0x60,
           'numpad_1': 0x61,
           'numpad_2': 0x62,
           'numpad_3': 0x63,
           'numpad_4': 0x64,
           'numpad_5': 0x65,
           'numpad_6': 0x66,
           'numpad_7': 0x67,
           'numpad_8': 0x68,
           'numpad_9': 0x69,
           'multiply_key': 0x6A,
           'add_key': 0x6B,
           'separator_key': 0x6C,
           'subtract_key': 0x6D,
           'decimal_key': 0x6E,
           'divide_key': 0x6F,
           'F1': 0x70,
           'F2': 0x71,
           'F3': 0x72,
           'F4': 0x73,
           'F5': 0x74,
           'F6': 0x75,
           'F7': 0x76,
           'F8': 0x77,
           'F9': 0x78,
           'F10': 0x79,
           'F11': 0x7A,
           'F12': 0x7B,
           'F13': 0x7C,
           'F14': 0x7D,
           'F15': 0x7E,
           'F16': 0x7F,
           'F17': 0x80,
           'F18': 0x81,
           'F19': 0x82,
           'F20': 0x83,
           'F21': 0x84,
           'F22': 0x85,
           'F23': 0x86,
           'F24': 0x87,
           'numLock': 0x90,
           'scrollLock': 0x91,
           'Lshift': 0xA0,
           'Rshift': 0xA1,
           'Lcontrol': 0xA2,
           'Rcontrol': 0xA3,
           'left_menu': 0xA4,
           'right_menu': 0xA5,
           'browser_back': 0xA6,
           'browser_forward': 0xA7,
           'browser_refresh': 0xA8,
           'browser_stop': 0xA9,
           'browser_search': 0xAA,
           'browser_favorites': 0xAB,
           'browser_start_and_home': 0xAC,
           'volume_mute': 0xAD,
           'volume_Down': 0xAE,
           'volume_up': 0xAF,
           'next_track': 0xB0,
           'previous_track': 0xB1,
           'stop_media': 0xB2,
           'play/pause_media': 0xB3,
           'start_mail': 0xB4,
           'select_media': 0xB5,
           'start_application_1': 0xB6,
           'start_application_2': 0xB7,
           'attn_key': 0xF6,
           'crsel_key': 0xF7,
           'exsel_key': 0xF8,
           'play_key': 0xFA,
           'zoom_key': 0xFB,
           'clear_key': 0xFE,
           '+': 0xBB,
           ',': 0xBC,
           '-': 0xBD,
           '.': 0xBE,
           '/': 0xBF,
           '`': 0xC0,
           ';': 0xBA,
           '[': 0xDB,
           '\\': 0xDC,
           ']': 0xDD,
           "'": 0xDE,
           '`': 0xC0,

           # no text output
           'Lwin': 0x5C,
           'Rwin': 0x5C,

           }

SCANCODES = {
    'escape': [[0x01], [0x81]],
    '1': [[0x02], [0x82]], '!': [[0x2A, 0x02], [0x82, 0xAA]],
    '2': [[0x03], [0x83]], '@': [[0x2A, 0x03], [0x83, 0xAA]],
    '3': [[0x04], [0x84]], '#': [[0x2A, 0x04], [0x83, 0xAA]],
    '4': [[0x05], [0x85]], '$': [[0x2A, 0x05], [0x85, 0xAA]],
    '5': [[0x06], [0x86]], '%': [[0x2A, 0x06], [0x86, 0xAA]],
    '6': [[0x07], [0x87]], '^': [[0x2A, 0x07], [0x87, 0xAA]],
    '7': [[0x08], [0x88]], '&': [[0x2A, 0x07], [0x87, 0xAA]],
    '8': [[0x09], [0x89]], '*': [[0x2A, 0x09], [0x89, 0xAA]],
    '9': [[0x0A], [0x8A]], '(': [[0x2A, 0x0A], [0x8A, 0xAA]],
    '0': [[0x0B], [0x8B]], ')': [[0x2A, 0x0B], [0x8B, 0xAA]],
    '-': [[0x0C], [0x8C]], '_': [[0x2A, 0x0C], [0x8C, 0xAA]],
    '=': [[0x0D], [0x8D]], '+': [[0x2A, 0x0D], [0x8D, 0xAA]],
    'backspace': [[0x0E], [0x8E]],
    '\b': [[0x0E], [0x8E]],
    'tab': [[0x0F], [0x8F]],
    '\t': [[0x0F], [0x8F]],
    'q': [[0x10], [0x90]], 'Q': [[0x2A, 0x10], [0x90, 0xAA]],
    'w': [[0x11], [0x91]], 'W': [[0x2A, 0x11], [0x91, 0xAA]],
    'e': [[0x12], [0x92]], 'E': [[0x2A, 0x12], [0x92, 0xAA]],
    'r': [[0x13], [0x93]], 'R': [[0x2A, 0x13], [0x93, 0xAA]],
    't': [[0x14], [0x94]], 'T': [[0x2A, 0x14], [0x94, 0xAA]],
    'y': [[0x15], [0x95]], 'Y': [[0x2A, 0x15], [0x95, 0xAA]],
    'u': [[0x16], [0x96]], 'U': [[0x2A, 0x16], [0x96, 0xAA]],
    'i': [[0x17], [0x97]], 'I': [[0x2A, 0x17], [0x97, 0xAA]],
    'o': [[0x18], [0x98]], 'O': [[0x2A, 0x18], [0x98, 0xAA]],
    'p': [[0x19], [0x99]], 'P': [[0x2A, 0x19], [0x99, 0xAA]],
    '[': [[0x1A], [0x9A]], '}': [[0x2A, 0x1A], [0x9A, 0xAA]],
    ']': [[0x1B], [0x9B]], '{': [[0x2A, 0x1B], [0x9B, 0xAA]],
    'enter': [[0x1C], [0x9C]],
    '\r': [[0x1C], [0x9C]],
    '\n': [[0x1C], [0x9C]],
    'Lcontrol': [[0x1D], [0x9D]],
    'a': [[0x1E], [0x9E]], 'A': [[0x2A, 0x1E], [0x9E, 0xAA]],
    's': [[0x1F], [0x9F]], 'S': [[0x2A, 0x1F], [0x9F, 0xAA]],
    'd': [[0x20], [0xA0]], 'D': [[0x2A, 0x20], [0xA0, 0xAA]],
    'f': [[0x21], [0xA1]], 'F': [[0x2A, 0x21], [0xA1, 0xAA]],
    'g': [[0x22], [0xA2]], 'G': [[0x2A, 0x22], [0xA2, 0xAA]],
    'h': [[0x23], [0xA3]], 'H': [[0x2A, 0x23], [0xA3, 0xAA]],
    'j': [[0x24], [0xA4]], 'J': [[0x2A, 0x24], [0xA4, 0xAA]],
    'k': [[0x25], [0xA5]], 'K': [[0x2A, 0x25], [0xA5, 0xAA]],
    'l': [[0x26], [0xA6]], 'L': [[0x2A, 0x26], [0xA6, 0xAA]],
    ';': [[0x27], [0xA7]], ':': [[0x2A, 0x27], [0xA7, 0xAA]],
    '\'': [[0x28], [0xA8]], '\"': [[0x2A, 0x28], [0xA8, 0xAA]],
    '`': [[0x29], [0xA9]], '~': [[0x2A, 0x29], [0xA9, 0xAA]],
    'Lshift': [[0x2A], [0xAA]],
    '\\': [[0x2B], [0xAB]], '|': [[0x2A, 0x2B], [0xAB, 0xAA]],
    'z': [[0x2C], [0xAC]], 'Z': [[0x2A, 0x2C], [0xAC, 0xAA]],
    'x': [[0x2D], [0xAD]], 'X': [[0x2A, 0x2D], [0xAD, 0xAA]],
    'c': [[0x2E], [0xAE]], 'C': [[0x2A, 0x2E], [0xAE, 0xAA]],
    'v': [[0x2F], [0xAF]], 'V': [[0x2A, 0x2F], [0xAF, 0xAA]],
    'b': [[0x30], [0xB0]], 'B': [[0x2A, 0x30], [0xB0, 0xAA]],
    'n': [[0x31], [0xB1]], 'N': [[0x2A, 0x31], [0xB1, 0xAA]],
    'm': [[0x32], [0xB2]], 'M': [[0x2A, 0x32], [0xB2, 0xAA]],
    ',': [[0x33], [0xB3]], '<': [[0x2A, 0x33], [0xB3, 0xAA]],
    '.': [[0x34], [0xB4]], '>': [[0x2A, 0x34], [0xB4, 0xAA]],
    '/': [[0x35], [0xB5]], '?': [[0x2A, 0x35], [0xB5, 0xAA]],
    'Rshift': [[0x36], [0xB6]],
    'printScreen': [[0x37], [0xB7]],
    'altgr': [[0x38], [0xB8]],
    'space': [[0x39], [0xB9]],
    ' ': [[0x39], [0xB9]],
    'capsLock': [[0x3A], [0xBA]],
    'F1': [[0x3B], [0xBB]],
    'F2': [[0x3C], [0xBC]],
    'F3': [[0x3D], [0xBD]],
    'F4': [[0x3E], [0xBE]],
    'F5': [[0x3F], [0xBF]],
    'F6': [[0x40], [0xC0]],
    'F7': [[0x41], [0xC1]],
    'F8': [[0x42], [0xC2]],
    'F9': [[0x43], [0xC3]],
    'F10': [[0x44], [0xC4]],
    'F11': [[0x57], [0xD7]],
    'F12': [[0x58], [0xD8]],
    'numLock': [[0x45], [0xC5]],
    'scrollLock': [[0x46], [0xC6]],
    'home': [[0x47], [0xC7]],
    'up': [[0x48], [0xC8]],
    'pageUp': [[0x49], [0xC9]],
    'minus': [[0x4A], [0xCA]],
    'left': [[0x4B], [0xCB]],
    'center': [[0x4C], [0xCC]],
    'right': [[0x4D], [0xCD]],
    'plus': [[0x4E], [0xCE]],
    'end': [[0x4F], [0xCF]],
    'down': [[0x50], [0xD0]],
    'pageDown': [[0x51], [0xD1]],
    'insert': [[0x52], [0xD2]],
    'delete': [[0x53], [0xD3]],
    'alt': [[0x0C, 0x38], [0xC0, 0xB8]],
    'Rcontrol': [[0x0C, 0x1D], [0xC0, 0x9D]],
    'Lwin': [[0x5D, 0x5B], [0xE0, 0xDB]],
    'Rwin': [[0xE0, 0x5C], [0xE0, 0xDC]],

    'E_DIV': [[0xE0, 0x54], [0xE0, 0xD4]],
    'E_ENTER': [[0xE0, 0x1C], [0xE0, 0x9C]],
    'E_INS': [[0xE0, 0x52], [0xE0, 0xD2]],
    'E_DEL': [[0xE0, 0x53], [0xE0, 0xD3]],
    'E_HOME': [[0xE0, 0x47], [0xE0, 0xC7]],
    'E_END': [[0xE0, 0x4F], [0xE0, 0xCF]],
    'E_PGUP': [[0xE0, 0x49], [0xE0, 0xC9]],
    'E_PGDN': [[0xE0, 0x51], [0xE0, 0xD1]],
    'E_LEFT': [[0xE0, 0x4B], [0xE0, 0xCB]],
    'E_RIGHT': [[0xE0, 0x4D], [0xE0, 0xCD]],
    'E_UP': [[0xE0, 0x48], [0xE0, 0xC8]],
    'E_DOWN': [[0xE0, 0x50], [0xE0, 0xD0]],
    # No scan code for pause key released
    'pause': [[0xE1, 0x1D, 0x45, 0xE1, 0x9D, 0xC5], []],

}

mouse_key_dict = {
    "M.left": "LButton",
    "M.right": "RButton",
    "M.middle": "MButton",
}
mouse_wheel_dict = {
    "M.scroll_y": ("WheelDown", "WheelUp"),
    "M.scroll_x": ("WheelLeft", "WheelRight")
}

ahk = AHK()


def press(key_inputs, controls):

    for k in key_inputs:

        t1 = time.time()
        key = ""
        if key_dict.__contains__(k):
            key = key_dict[k]
            if (not controls["enable_key_whitelist"] or key in controls["key_whitelist"]) and \
                    not (controls["enable_key_blacklist"] and key in controls["key_blacklist"]):
                if controls["enable_key_conversion"] and key in controls["key_conversion"]:
                    key = controls["key_conversion"][key]
            else:
                continue

        elif mouse_key_dict.__contains__(k):
            key = mouse_key_dict[k]
            if key_inputs[k] == 1:
                ahk.key_down(key, False)

            if key_inputs[k] == 0:
                ahk.key_up(key, False)

            continue

        elif mouse_wheel_dict.__contains__(k):

            for i in range(abs(key_inputs[k])):
                key_inputs[k] /= abs(key_inputs[k])
                if key_inputs[k] == -1:
                    key = mouse_wheel_dict[k][0]
                if key_inputs[k] == 1:
                    key = mouse_wheel_dict[k][1]
                # print("pressing:" + str(key))
                ahk.key_press(key, False)

            continue
        else:
            try:
                key = chr(int(k)).lower()
                if 160 < int(k):
                    print("key:", key, "could not be pressed")
                    continue
            except ValueError:
                print("key:", k, "could not be pressed")
                continue

        if (not controls["enable_key_whitelist"] or key in controls["key_whitelist"]) and \
                not (controls["enable_key_blacklist"] and key in controls["key_blacklist"]):
            if controls["enable_key_conversion"] and key in controls["key_conversion"]:
                k = controls["key_conversion"][k]
            if key_inputs[k] == 1:
                win32api.keybd_event(VK_CODE[key], SCANCODES[key][0][0], 0, 0)

            if key_inputs[k] == 0:
                win32api.keybd_event(VK_CODE[key], SCANCODES[key][0][0], win32con.KEYEVENTF_KEYUP, 0)
