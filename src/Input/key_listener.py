from Input import input_listener
from pynput import keyboard

global alt_gr_pressed
global t_pressed
alt_gr_pressed = False
t_pressed = False
global listener
listener = None


def do_suppress_inputs(val):
    listener._suppress = val


def on_press(key):
    global alt_gr_pressed
    global t_pressed
    global listener

    if isinstance(key, keyboard.KeyCode):
        t_pressed = (key.vk == 84)  # 84 = vk code of t

        part_of_shortcut = False

        if alt_gr_pressed and t_pressed:
            part_of_shortcut = True
            input_listener.toggle_suppress_inputs()

        if input_listener.suppress_inputs and not part_of_shortcut:
            input_listener.input("Keyboard", str(key.vk), 1)
    else:
        alt_gr_pressed = (key == keyboard.Key.alt_gr)
        if input_listener.suppress_inputs:
            input_listener.input("Keyboard", str(key), 1)

    print(input_listener.input_obj.key_inputs)
    pass


def on_release(key):
    global alt_gr_pressed
    global t_pressed

    if isinstance(key, keyboard.KeyCode):
        if key.vk == 84:
            # 84 = vk code of t
            t_pressed = False
        input_listener.input("Keyboard", str(key.vk), 0)
    else:
        if key == keyboard.Key.alt_gr:
            alt_gr_pressed = False
        input_listener.input("Keyboard", str(key), 0)
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
