#here's a Python exercise that covers the four pillars of OOP: Inheritance, Polymorphism, Abstraction, and Encapsulation. This exercise is designed as a fill-in-the-blanks exercise:


# Task
#In this exercise, you will need to fill in and complete the """TODO""" sections. This will test their understanding of the four pillars of OOP. The `Shape` class is an example of abstraction, the `Rectangle` and `Circle` classes demonstrate inheritance, the `area` method shows polymorphism, and the encapsulation of width, height, and radius in the `Rectangle` and `Circle` classes illustrates encapsulation.

# ---------------start below----------------

# Import the necessary module to create an abstract class
from """TODO""" import """TODO"""


# Create an abstract class 'Shape' with an abstract method 'area'
class Shape("""TODO"""):
    @"""TODO"""
    def area("""TODO"""):
        pass

# TODO: Create a class 'Rectangle' that inherits from 'Shape'
class Rectangle("""TODO"""):
    def __init__(self, """TODO""", """TODO"""):
        # TODO: Encapsulate width and height (Hint: Use private variables)
        self.__width = width
        self.__height = height

    # TODO: Implement the 'area' method for the 'Rectangle' class
    """TODO"""

# TODO: Create a class 'Circle' that inherits from 'Shape'
class Circle("""TODO"""):
    def __init__(self, """TODO"""):
        # TODO: Encapsulate radius (Hint: Use a private variable)
        self.__radius = radius

    # TODO: Implement the 'area' method for the 'Circle' class
    def """TODO"""(self):
        return 3.14 * (self.__radius ** 2)

# TODO: Create a function 'print_area' that takes a shape object and prints its area
def print_area(shape):
    print("The area is:", shape.area())

# TODO: Create objects of 'Rectangle' and 'Circle', then call 'print_area' for both
"""TODO""" = """TODO"""(5, 4)
"""TODO""" = """TODO"""(3)

print_area("""TODO""")
print_area("""TODO""")


