import pickle
import itertools

from Input import mouse_mover
from Input import key_presser

accept_repeated_clicks = False


class InputObject:
    key_inputs = {}
    key_inputs_delta = {}

    scalar_inputs = {}
    scalar_inputs_delta = {}

    def has_deltas(self):
        return len(self.key_inputs_delta) > 0 or len(self.scalar_inputs_delta) > 0

    def __init__(self, serialized=None):
        self.key_inputs = {}
        self.scalar_inputs = {}

        self.accept_repeated_clicks = accept_repeated_clicks

        self.control_config = None

        if serialized is not None:
            self.deserialize(serialized)

    def serialize(self):
        return pickle.dumps((self.key_inputs, self.scalar_inputs))

    def serialize_chunks(self, max_chunksize):
        chunks = []
        for i in range(0, len(self.key_inputs), max_chunksize):
            chunks.append(pickle.dumps((dict(itertools.islice(self.key_inputs.items(), i, i + max_chunksize)), {})))
        for i in range(0, len(self.scalar_inputs), round(max_chunksize / 2)):
            chunks.append(
                pickle.dumps(({}, dict(itertools.islice(self.scalar_inputs, i, i + round(max_chunksize / 2))))))
        return chunks

    def serialize_delta(self, clear_deltas=True):
        serialized = pickle.dumps((self.key_inputs_delta, self.scalar_inputs_delta))
        if clear_deltas:
            self.key_inputs_delta = {}
            self.scalar_inputs_delta = {}
        return serialized

    def deserialize(self, data):
        self.key_inputs, self.scalar_inputs = pickle.loads(data)

    def deserialize_delta(self, data):
        self.key_inputs_delta, self.scalar_inputs_delta = pickle.loads(data)
        for key in self.key_inputs_delta:
            self.key_inputs[key] = self.key_inputs_delta[key]

        for key in self.scalar_inputs_delta:
            self.scalar_inputs[key] = self.scalar_inputs_delta[key]

    def input(self, key, value, is_scalar=False, is_delta=False, repeat_inputs=accept_repeated_clicks):
        if key[:2] == "M." and self.control_config["enable_mouse"] \
                or key[:2] != "M." and self.control_config["enable_keyboard"]:
            if is_scalar:
                if is_delta:
                    if not ((key == "M.x" and not self.control_config["enable_mouse_x"])
                            or (key == "M.y" and not self.control_config["enable_mouse_y"])):

                        if not self.scalar_inputs.__contains__(key):
                            self.scalar_inputs[key] = value
                        else:
                            self.scalar_inputs[key] += value

                        if value != 0:
                            if not self.scalar_inputs_delta.__contains__(key):
                                self.scalar_inputs_delta[key] = value
                            else:
                                self.scalar_inputs_delta[key] += value

                else:
                    if not (self.scalar_inputs.__contains__(key) and self.scalar_inputs[key] == value):
                        self.scalar_inputs[key] = value
                        self.scalar_inputs_delta[key] = value
            else:

                key = self.apply_controls(key, do_conversion_first=False)

                if key is not None:
                    if repeat_inputs or not (
                            self.key_inputs.__contains__(key) and self.key_inputs[key] == value):
                        self.key_inputs[key] = value
                        self.key_inputs_delta[key] = value

    def execute_deltas(self, clear_deltas=True):
        self.execute_scalar_deltas()
        self.execute_key_deltas()

        if clear_deltas:
            self.key_inputs_delta = {}
            self.scalar_inputs_delta = {}

    def apply_controls(self, key, do_conversion_first=True):
        do_execute = True
        if self.control_config is not None:
            if do_conversion_first:
                if self.control_config["enable_key_conversion"] and key in self.control_config["key_conversion"]:
                    key = self.control_config["key_conversion"][key]

            do_execute = (not self.control_config["enable_key_whitelist"] or
                          key in self.control_config["key_whitelist"]) and not \
                             (self.control_config["enable_key_blacklist"] and
                              key in self.control_config["key_blacklist"])

            if not do_conversion_first:
                if self.control_config["enable_key_conversion"] and key in self.control_config["key_conversion"]:
                    key = self.control_config["key_conversion"][key]

        if do_execute:
            return key
        return None

    def execute_scalar_deltas(self):
        if self.control_config["enable_mouse"]:
            mouse_x_delta = 0
            mouse_y_delta = 0
            if self.scalar_inputs.__contains__("M.x") and self.control_config["enable_mouse_x"]:
                mouse_x_delta += self.scalar_inputs["M.x"]
                self.scalar_inputs["M.x"] = 0
            if self.scalar_inputs.__contains__("M.y") and self.control_config["enable_mouse_y"]:
                mouse_y_delta += self.scalar_inputs["M.y"]
                self.scalar_inputs["M.y"] = 0

            if mouse_x_delta != 0 or mouse_y_delta != 0:
                mouse_mover.move(mouse_x_delta, mouse_y_delta)

    def execute_key_deltas(self):
        for key in self.key_inputs_delta:
            val = self.key_inputs_delta[key]
            key = self.apply_controls(key)

            if key is not None:
                from_mouse = False
                if key[:2] == "M.":
                    key = key[2:]
                    from_mouse = True

                if from_mouse and self.control_config["enable_mouse"] or \
                        not from_mouse and self.control_config["enable_keyboard"]:
                    key_presser.press(key, val, from_mouse)
