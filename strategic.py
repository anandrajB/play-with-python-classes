class ConditionClassA:
    def __init__(self, main_instance):
        self.main_instance = main_instance

    def execute(self):
        attribute_value = self.main_instance.attribute
        print(f"Condition Class A is executed with attribute value: {attribute_value}")

class MainClass:
    def __init__(self):
        self.attribute = "example"
        self.b = "some"
        self.condition_a = ConditionClassA(self)

    def perform_operation(self, condition):
        if condition == "A":
            self.condition_a.execute()
        else:
            print("Invalid condition")

# Example usage:
main = MainClass()

main.perform_operation("A") 
main.perform_operation("B")  
