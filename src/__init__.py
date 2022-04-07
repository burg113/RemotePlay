import time
import pynput.keyboard
from ahk import AHK


def int_to_bytes(i, n=2):
    b = b''
    for c in range(n):
        print(c, "--", int((i / 128 ** c) % 128))
        b += chr(int((i / 128 ** c) % 128)).encode()
    return b


def int_from_bytes(b):
    i = 0
    for c in range(len(b)):
        i += b[c] * 128 ** (c)
    return i


if __name__ == "__main__":
    for i in range(16385):
        b = int_to_bytes(i)
        print(i, "\t", b)
        print(int_from_bytes(b))
        print("---------------------")

"""  time.sleep(1)

    ahk = AHK()
    # ahk.mouse_move(x=100, y=100, blocking=True)  # Blocks until mouse finishes moving (the default)
    time.sleep(1)
    ahk.key_down('w')
    time.sleep(5)
    ahk.key_up('w')"""
