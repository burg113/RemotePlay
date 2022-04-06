import input_object

if __name__ == "__main__":
    i = input_object.InputObject()
    i.key_inputs["key_A"] = 1
    i.key_inputs["key_B"] = 0
    i.key_inputs["key_C"] = 0
    print(i.key_inputs)

    i2 = input_object.InputObject(i.serialize())
    print(i2.key_inputs)

    delta = input_object.InputObject()
    delta.key_inputs["key_C"] = 1
    print(delta.key_inputs)

    i2.deserialize_delta(delta.serialize())




