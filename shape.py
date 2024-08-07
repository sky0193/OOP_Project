import math

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


class Shape: 
    def __init__(self, x, y): 

        """ 
        Initialize a new shape. 
        :param x: The x-coordinate of the top-left corner of the shape. 
        :param y: The y-coordinate of the top-left corner of the shape. 
        """ 
        self.x = x 
        self.y = y 

    def area(self): 
        raise NotImplementedError("Should be implemented") 

    def circumference(self): 
        raise NotImplementedError("Should be implemented") 
    

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        """
        :param x: The x-coordinate of the top-left corner.
        :param y: The y-coordinate of the top-left corner.
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        super().__init__(x, y)
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def circumference(self):
        return 2 * (self._width + self._height)

class Triangle(Shape):
    def __init__(self, x, y, a, b, c):
        """
        :param x: The x-coordinate of the top-left corner (reference point).
        :param y: The y-coordinate of the top-left corner (reference point).
        :param a: The length of side a.
        :param b: The length of side b.
        :param c: The length of side c.
        """
        super().__init__(x, y)
        self._a = a
        self._b = b
        self._c = c

    def area(self):
        # Satz des Herons
        s = (self._a + self._b + self._c) / 2
        return (s * (s - self._a) * (s - self._b) * (s - self._c)) ** 0.5

    def circumference(self):
        return self._a + self._b + self._c
    
class Square(Rectangle):
    def __init__(self, x, y, side_length):
        """
        :param x: The x-coordinate of the top-left corner.
        :param y: The y-coordinate of the top-left corner.
        :param side_length: The side length of the square.
        """
        super().__init__(x, y, side_length, side_length)

rectangle_A = Rectangle(0,0,10,5)
print(f"rectangle_A has area : {rectangle_A.area()} and circumference {rectangle_A.circumference()}") 

square_A = Square(0,0,5)
print(f"square_A has area : {square_A.area()} and circumference {square_A.circumference()}") 

triangle_A = Triangle(0,0,5,5,5)
print(f"triangle_A has area : {triangle_A.area()} and circumference {triangle_A.circumference()}") 