import functools

class ExpensiveDataCalculator:
    @functools.lru_cache(maxsize=None)
    def compute_expensive_data(self, param):
        # Simulating an expensive computation based on a parameter
        print("Computing expensive data...")
        return param + 100


class MyClass:
    def __init__(self, calculator):
        self.calculator = calculator

    def method1(self, param):
        result = self.calculator.compute_expensive_data(param)
        # Use result

    def method2(self, param):
        result = self.calculator.compute_expensive_data(param)
        # Use result

    def method3(self, param):
        result = self.calculator.compute_expensive_data(param)
        # Use result


# Usage
calculator = ExpensiveDataCalculator()
obj = MyClass(calculator)
obj.method1(5)  # Computes and caches result
obj.method2(5)  # Retrieves result from cache
obj.method3(10) # Computes and caches result for a different parameter
obj.method1(5)  # Retrieves result from cache