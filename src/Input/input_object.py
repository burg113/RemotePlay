import pickle


class InputObject:
    key_inputs = {}
    key_inputs_delta = {}

    scalar_inputs = {}
    scalar_inputs_delta = {}

    def has_deltas(self):
        return len(self.key_inputs_delta)>0 or len(self.scalar_inputs_delta)>0

    def __init__(self, serialized=None):
        self.key_inputs = {}
        self.scalar_inputs = {}
        if serialized is not None:
            self.deserialize(serialized)

    def serialize(self):
        return pickle.dumps((self.key_inputs, self.scalar_inputs))

    def serialize_delta(self):
        serialized = pickle.dumps((self.key_inputs_delta, self.scalar_inputs_delta))
        self.key_inputs_delta = {}
        self.scalar_inputs_delta = {}
        return serialized

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
            self.scalar_inputs_delta[key] = value
        else:
            self.key_inputs[key] = value
            self.key_inputs_delta[key] = value
