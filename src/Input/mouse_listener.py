import time
from multiprocessing import Process

from Input import input_listener
from pynput.mouse import Button, Controller

mouse = Controller()
mouse_position = (0, 0)
mouse_delta = (0, 0)


def get_mouse_delta():
    global mouse_position, mouse_delta, mouse

    print("\t\t\t\t\t\t", input_listener.input_obj.scalar_inputs_delta)
    time.sleep(0.01)

    new_mouse_position = mouse.position
    mouse_delta = (new_mouse_position[0] - mouse_position[0], new_mouse_position[1] - mouse_position[1])
    input_listener.input_obj.input("MouseXDelta", mouse_delta[0], is_scalar=True, is_delta=True)
    input_listener.input_obj.input("MouseYDelta", mouse_delta[1], is_scalar=True, is_delta=True)
    mouse_position = new_mouse_position


"""
def listen():
    mouse_position = (0, 0)
    mouse_delta = (0, 0)
    last = time.time()
    while True:
        print("\t\t\t\t\t\t", input_listener.input_obj.scalar_inputs_delta)
        time.sleep(0.01)
        last = time.time()

        last = time.time()
        # print(mouse_delta)

        new_mouse_position = mouse.position
        mouse_delta = (new_mouse_position[0] - mouse_position[0], new_mouse_position[1] - mouse_position[1])
        input_listener.input_obj.input("MouseXDelta", mouse_delta[0], is_scalar=True, is_delta=True)
        input_listener.input_obj.input("MouseYDelta", mouse_delta[1], is_scalar=True, is_delta=True)
        mouse_position = new_mouse_position


def run():
    p = Process(target=listen)
    p.start()


if __name__ == "__main__":
    run()

    while True:
        pass
"""
