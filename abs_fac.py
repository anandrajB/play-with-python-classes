from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass

class CircleFactory(ShapeFactory):
    def create_shape(self):
        return Circle()

class RectangleFactory(ShapeFactory):
    def create_shape(self):
        return Rectangle()

RectangleFactory().create_shape()