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

    def perimeter(self): 
        raise NotImplementedError("Should be implemented") 
    
