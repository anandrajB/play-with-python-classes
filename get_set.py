class MyClass:
    def __init__(self):
        self._attributes = {}

    def __getattr__(self, name):
        return self._attributes.get(name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            self._attributes[name] = value


# Example usage
my_obj = MyClass()
my_obj.attribute1 = 42
print(my_obj.attribute1)
my_obj.attribute2 = "Hello, world!"
my_obj.attribute3 = [1, 2, 3]
my_obj.attribute4 = {"name": "John", "age": 30}