from Input import input_object
from Input import input_listener
from pynput import keyboard



def on_press(key):
    if isinstance(key, keyboard.KeyCode):
        input_listener.input_obj.input(str(key.vk), 1)
    else:
        input_listener.input_obj.input(str(key), 1)
    print(input_listener.input_obj.key_inputs)
    pass


def on_release(key):
    if isinstance(key, keyboard.KeyCode):
        input_listener.input_obj.input(str(key.vk), 0)
    else:
        input_listener.input_obj.input(str(key), 0)
    print(input_listener.input_obj.key_inputs)
    pass


def run():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release,
        suppress=True)
    listener.start()


if __name__ == "__main__":
    run()

    while True:
        pass
