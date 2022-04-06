from input_object import InputObject
from pynput import keyboard


input_obj = InputObject()

def on_press(key):
	if isinstance(key, keyboard.KeyCode):
		input_name = str(key.vk)
		input_obj.key_inputs[input_name] = 1
	else:
		input_name = str(key)
		input_obj.key_inputs[input_name] = 1
	print(input_obj.key_inputs)
	pass

def on_release(key):
	if isinstance(key, keyboard.KeyCode):
		input_name = str(key.vk)
		input_obj.key_inputs[input_name] = 0
	else:
		input_name = str(key)
		input_obj.key_inputs[input_name] = 0
	print(input_obj.key_inputs)
	pass

listener = keyboard.Listener(
	on_press=on_press, 
	on_release=on_release)
listener.start()

while True: pass