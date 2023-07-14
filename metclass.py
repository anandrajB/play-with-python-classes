class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        # Modify or customize the class attributes here
        attrs['finance_amount'] = 0 
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    
    def __init__(self ,a):
        self.a = a 

print(MyClass(a = 1).finance_amount)  # Output: 10
