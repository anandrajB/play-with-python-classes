class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")


class Wheel:
    def rotate(self):
        print("Wheel rotating")


class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

    def drive(self):
        for wheel in self.wheels:
            wheel.rotate()


class Driver:
    def __init__(self, name):
        self.name = name

    def drive_car(self, car):
        print(f"{self.name} is driving the car.")
        car.start_engine()
        car.drive()
        car.stop_engine()


# Usage
car = Car()
driver = Driver("John")
driver.drive_car(car)