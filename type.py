from typing import Type

class Class2:
    def __init__(self, value: str):
        self.value = value

class MyClass:
    def __init__(self, value: int):
        self.value = value
        self.val2: Type[Class2] = Class2

# Creating instances
obj1 = MyClass(10)
obj2 = obj1.val2("Hello")

print(obj2.value)  # Output: Hello