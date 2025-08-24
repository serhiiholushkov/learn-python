class Dog:
    # Class variables are shared across all instances like static variables in other languages
    kind = "canine"  # class variable
    tricks = []  # class variable. Causes shared state issue!

    # there is no private keyword in Python, but prefixing with underscore is a convention
    _private_var = "I am private"
    # or prefixing with double underscore for name mangling
    __name_mangled_var = "I am name mangled"

    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age  # instance variable
        # tricks should be an instance variable to avoid shared state issue
        # self.tricks = []  # instance variable

    def bark(self):
        return f"{self.name} says woof!"


d1 = Dog("Fido", 3)
d2 = Dog("Buddy", 5)
print(d1.kind)  # Accessing class variable
print(d2.kind)  # Accessing class variable

print("changing d1's kind to 'wolf'")
d1.kind = "wolf"  # This creates an instance variable for d1
print(d1.kind)  # Now d1 has its own 'kind'
print(d2.kind)  # d2 still refers to the class variable

print("mutating tricks list via d1")
d1.tricks.append("roll over")  # Modifying the shared class variable
print(d1.tricks)  # Both d1 and d2 see the change
print(d2.tricks)  # Both d1 and d2 see the change
print("mutating tricks list via d2")
d2.tricks.append("play dead")  # Modifying the shared class variable
print(d1.tricks)  # Both d1 and d2 see the change
print(d2.tricks)  # Both d1 and d2 see the change

print("Accessing class variable via class name")
print(Dog.kind)  # Accessing class variable via class name
Dog.kind = "something"
print(d1.kind)  # d1 still has its own 'kind
print(d2.kind)  # d2 now sees the updated class variable
print(Dog.kind)  # Accessing updated class variable via class name
