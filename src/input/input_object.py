import pickle


class InputObject:

    def __init__(self, serialized=None):
        self.key_inputs = {}
        self.scalar_inputs = {}
        if serialized is not None:
            self.deserialize(serialized)

    def serialize(self):
        return pickle.dumps((self.key_inputs, self.scalar_inputs))

    def deserialize(self, data):
        self.key_inputs, self.scalar_inputs = pickle.loads(data)

    def deserialize_delta(self, data):
        key_inputs_delta, scalar_inputs_delta = pickle.loads(data)
        for key in key_inputs_delta:
            self.key_inputs[key] = key_inputs_delta[key]

        for key in scalar_inputs_delta:
            self.scalar_inputs[key] = scalar_inputs_delta[key]

    def input(self, key, value, is_scalar=False):
        if is_scalar:
            self.scalar_inputs[key] = value
        else:
            self.key_inputs[key] = value
