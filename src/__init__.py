import time

import win32api
import win32con

if __name__ == "__main__":
    print(win32con.VK_APPS)
    for i in range(255):
        print(i)
        win32api.keybd_event(i, 0, 0, 0)
        time.sleep(.1)
        win32api.keybd_event(i, 0, win32con.KEYEVENTF_KEYUP, 0)
    pass
