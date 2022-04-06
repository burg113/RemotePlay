

class InputObject:
    key_inputs = []
    scalar_inputs = []

    def __init__(self, serialized):
        self.deseriealize(serialized)

    def __init__(self, key_inputs, scalar_inputs):
        self.key_inputs = key_inputs
        self.scalar_inputs = scalar_inputs


    def seriealize(self):
        return ""


    def deseriealize(self):
        return ""

