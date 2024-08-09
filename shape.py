import math

class Point:
    def __init__(self, x, y):
        self.set_cartesian(x, y)

    def set_cartesian(self, x, y):
        self._x = x
        self._y = y
        self._update_polar()

    def get_cartesian(self):
        return self._x, self._y

    def get_polar(self):
        return self._r, self._theta

    def _update_polar(self):
        self._r = math.sqrt(self._x**2 + self._y**2)
        self._theta = math.degrees(math.atan2(self._y, self._x))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._update_polar()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._update_polar()       

class MovableObject:
    def move(self, dx, dy):
        """
        Move the object by dx and dy.
        :param dx: Change in the x-coordinate.
        :param dy: Change in the y-coordinate.
        """
        self.x += dx
        self.y += dy

class Shape: 
    def __init__(self, x, y): 

        """ 
        Initialize a new shape. 
        :param x: The x-coordinate of the top-left corner of the shape. 
        :param y: The y-coordinate of the top-left corner of the shape. 
        """ 
        self._point = Point(x, y)
        self._on_ground = True if y == 0 else False

    @property
    def x(self):
        return self._point.x

    @x.setter
    def x(self, value):
        self._point.x = value

    @property
    def y(self):
        return self._point.y

    @y.setter
    def y(self, value):
        self._point.y = value
        self._on_ground = True if self._point.y == 0 else False


    def area(self): 
        raise NotImplementedError("Should be implemented") 

    def circumference(self): 
        raise NotImplementedError("Should be implemented") 
    


class MovableObject:
    def move(self, dx, dy):
        """
        Move the object by dx and dy along the x and y axis respectively.
        :param dx: Change in x-coordinate.
        :param dy: Change in y-coordinate.
        """
        self.x += dx
        self.y += dy


class Rectangle(Shape, MovableObject):
    def __init__(self, x, y, width, height):
        """
        :param x: The x-coordinate of the top-left corner.
        :param y: The y-coordinate of the top-left corner.
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        
    @property
    def on_ground(self):
        return self._on_ground
        
    def area(self):
        return self.__width * self.__height

    def circumference(self):
        return 2 * (self.__width + self.__height)

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
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self):
        # Satz des Herons
        s = (self.__a + self.__b + self.__c) / 2
        return (s * (s - self.__a) * (s - self.__b) * (s - self.__c)) ** 0.5

    def circumference(self):
        return self.__a + self.__b + self.__c

class Square(Rectangle):
    def __init__(self, x, y, side_length):
        """
        :param x: The x-coordinate of the top-left corner.
        :param y: The y-coordinate of the top-left corner.
        :param side_length: The side length of the square.
        """
        super().__init__(x, y, side_length, side_length)
        

rectangle_A = Rectangle(10,0,10,5)
print(f"rectangle_A on position {rectangle_A.x}:{rectangle_A.y} has area : {rectangle_A.area()} and circumference {rectangle_A.circumference()}") 
print(f"rectangle_A on position {rectangle_A.x}:{rectangle_A.y} and is on_ground: {rectangle_A.on_ground} has heigth : {rectangle_A.height} and width {rectangle_A.width}")
rectangle_A.move(2,2)
print(f"rectangle_A was moved on position {rectangle_A.x}:{rectangle_A.y} and is on_ground:{rectangle_A.on_ground}")

square_A = Square(0,0,5)
print(f"square_A has area : {square_A.area()} and circumference {square_A.circumference()}") 

triangle_A = Triangle(0,0,5,5,5)
print(f"triangle_A has area : {triangle_A.area()} and circumference {triangle_A.circumference()}") 

point = Point(1,6)

