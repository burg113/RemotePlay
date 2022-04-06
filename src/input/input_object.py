import pickle


class InputObject:
    key_inputs = {}
    scalar_inputs = {}


    def __init__(self, serialized=None):
        if serialized is not None:
            self.deserialize(serialized)

    def serialize(self):
        return pickle.dumps((self.key_inputs, self.scalar_inputs))

    def deserialize(self, data):
        self.key_inputs, self.scalar_inputs = pickle.loads(data)

    def deserialize_delta(self,data):
        key_inputs_delta, scalar_inputs_delta = pickle.loads(data)
        for pair in key_inputs_delta:
            self.key_inputs[pair[0]] = pair[1]

