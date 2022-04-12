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

        self.control_config = None

        if serialized is not None:
            self.deserialize(serialized)

    def serialize(self):
        return pickle.dumps((self.key_inputs, self.scalar_inputs))

    def serialize_chunks(self, max_chunksize):
        chunks = []
        for i in range(0, len(self.key_inputs), max_chunksize):
            print(self.key_inputs)
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

    def input(self, key, value, is_scalar=False, is_delta=False):
        accept_input = True
        if self.control_config is not None:

            accept_input = (not self.control_config["enable_key_whitelist"] or key in self.control_config[
                "key_whitelist"]) and \
                           not (self.control_config["enable_key_blacklist"] and key in self.control_config[
                               "key_blacklist"])

            if self.control_config["enable_key_conversion"] and key in self.control_config["key_conversion"]:
                key = self.control_config["key_conversion"][key]

        if accept_input:

            if is_scalar:
                if is_delta:
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
                if accept_repeated_clicks or not (self.key_inputs.__contains__(key) and self.key_inputs[key] == value):
                    self.key_inputs[key] = value
                    self.key_inputs_delta[key] = value

    def execute_deltas(self, clear_deltas=True):
        self.execute_scalar_deltas()
        self.execute_key_deltas()

        if clear_deltas:
            self.key_inputs_delta = {}
            self.scalar_inputs_delta = {}

    def execute_scalar_deltas(self):
        mouse_x_delta = 0
        mouse_y_delta = 0

        if self.scalar_inputs.__contains__("MouseXDelta"):
            mouse_x_delta += self.scalar_inputs["MouseXDelta"]
        if self.scalar_inputs.__contains__("MouseYDelta"):
            mouse_y_delta += self.scalar_inputs["MouseYDelta"]

        mouse_mover.move(mouse_x_delta, mouse_y_delta)

    def execute_key_deltas(self):
        for key in self.key_inputs_delta:
            val = self.key_inputs_delta[key]
            do_execute = True
            if self.control_config is not None:
                print(10 * "#", key)
                if self.control_config["enable_key_conversion"] and key in self.control_config["key_conversion"]:
                    key = self.control_config["key_conversion"][key]

                do_execute = (not self.control_config["enable_key_whitelist"] or
                              key in self.control_config["key_whitelist"]) and not \
                                 (self.control_config["enable_key_blacklist"] and
                                  key in self.control_config["key_blacklist"])

            if do_execute:
                key_presser.press(key, val)
