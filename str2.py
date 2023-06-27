import functools

class ExpensiveDataCalculator:
    def compute_expensive_data(self, attrs):
        print(attrs.attr1)
        result =  attrs.attr1 + attrs.attr2
        print("the sum is" , result)
        return result

class ExpensiveDataCalculator2:
    def compute_expensive_data(self, attrs):
        print(attrs.attr1)
        result =  attrs.attr1 + attrs.attr2
        print(result)
        return result

from dataclasses import dataclass
from typing import Optional

@dataclass
class MyClass:
    attr1 : int
    attr2 : int
    calculator : Optional = ExpensiveDataCalculator()

    # cal2 : ExpensiveDataCalculator2()

    def method1(self):
        result = self.calculator.compute_expensive_data(self)
        # Use result

# Usage
obj = MyClass(5 , 5)
obj.method1()  # Computes and caches result

