from Input import input_object
from Input import input_listener
from pynput import keyboard

global alt_gr_pressed
global t_pressed
alt_gr_pressed = False
t_pressed = False
global listener
listener = None


def on_press(key):
    global alt_gr_pressed
    global t_pressed
    global listener

    if isinstance(key, keyboard.KeyCode):
        t_pressed = (key.vk == 84)  # 84 = vk code of t
        input_listener.input_obj.input(str(key.vk), 1)
    else:
        alt_gr_pressed = (key == keyboard.Key.alt_gr)
        input_listener.input_obj.input(str(key), 1)
    if alt_gr_pressed and t_pressed:
        input_listener.suppress_inputs = not input_listener.suppress_inputs
        listener._suppress = input_listener.suppress_inputs

    print(input_listener.input_obj.key_inputs)
    pass


def on_release(key):
    global alt_gr_pressed
    global t_pressed

    if isinstance(key, keyboard.KeyCode):
        if key.vk == 84:
            # 84 = vk code of t
            t_pressed = False
        input_listener.input_obj.input(str(key.vk), 0)
    else:
        if key == keyboard.Key.alt_gr:
            alt_gr_pressed = False
        input_listener.input_obj.input(str(key), 0)
    print(input_listener.input_obj.key_inputs)
    pass


def run():
    global listener
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release,
        suppress=True)
    listener.start()


if __name__ == "__main__":
    run()

    while True:
        pass
