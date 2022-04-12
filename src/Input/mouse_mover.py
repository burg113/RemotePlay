from ahk import AHK
import win32api
import win32con

ahk = AHK()


def move(mouse_x_delta, mouse_y_delta):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, mouse_x_delta, mouse_y_delta, 0, 0)
