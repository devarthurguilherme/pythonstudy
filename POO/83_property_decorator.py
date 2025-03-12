class Rectangle:
    def __init__(self, width, height):
        self._myWidth = width
        self._myHeight = height

    # From getters to attributes, You must use the decorator @property
    @property
    def width(self):
        return self._myWidth

    @width.setter
    def width(self, value):
        if value > 0:
            self._myWidth = value
        else:
            print("\nWidth must be bigger than zero!\n")

    @property
    def height(self):
        return self._myHeight

    @height.setter
    def height(self, value):
        if value > 0:
            self._myHeight = value
        else:
            print("\nHeight must be bigger than zero!\n")

    @property
    def area(self):
        return self._myWidth * self._myHeight


r = Rectangle(10, 7)
print("Area: ", r.area)  # Area:  70

r.width = 12
print("Area: ", r.area)  # Area:  84

r.width = -8
print("Area: ", r.area)  # Area:  84
