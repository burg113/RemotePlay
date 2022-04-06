import input_object

if __name__ == "__main__":
    i = input_object.InputObject()
    i.input("key_A", 1)
    i.input("key_B", 0)
    i.input("key_C", 0)
    i.input("key_B", 1)
    i.input("key_B", 0)
    print(i.key_inputs)

    i2 = input_object.InputObject(i.serialize())
    print(i2.key_inputs)

    delta = input_object.InputObject()
    print("--",delta.key_inputs)
    delta.input("key_C", 1)
    delta.input("key_A", 0)
    print(delta.key_inputs)

    i2.deserialize_delta(delta.serialize())
    print(i2.key_inputs)
