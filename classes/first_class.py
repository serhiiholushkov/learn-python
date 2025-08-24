class FirstClass:
    """A simple example class."""

    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2


instance = FirstClass("value1", "value2")
print(FirstClass.__doc__)
print(instance.prop1)
print(instance.prop2)
