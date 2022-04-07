from Input import input_object
from pynput import keyboard

input_obj = input_object.InputObject()


def on_press(key):
    if isinstance(key, keyboard.KeyCode):
        input_obj.input(str(key.vk), 1)
    else:
        input_obj.input(str(key), 1)
    print(input_obj.key_inputs)
    pass


def on_release(key):
    if isinstance(key, keyboard.KeyCode):
        input_obj.input(str(key.vk), 0)
    else:
        input_obj.input(str(key), 0)
    print(input_obj.key_inputs)
    pass


def run():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()


if __name__ == "__main__":
    run()

    while True:
        pass
