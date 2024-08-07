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


point = Point(2, 3)
print(point.x)
print(point.y)

point.x = 10
point.y = 20
print(point.x)
print(point.y)
