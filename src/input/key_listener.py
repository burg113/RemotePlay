from input_object import InputObject
from pynput import keyboard


if __name__ == "__main__":
	input_obj = InputObject()

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

	listener = keyboard.Listener(
		on_press=on_press, 
		on_release=on_release)
	listener.start()

	while True: pass