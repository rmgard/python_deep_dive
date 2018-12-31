################################################
# Classes & OOP
################################################

################################################ 
# Class with Getters and setters
################################################

class RectangleGetSet:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeters(self):
        return 2 * (self._width + self._height)

    '''def to_string(self):
        return 'Rectangle: width={0}, height={1}'.format(self._width, self._height)
'''
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self._width, self._height)

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        else:
            self._width = width

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self. area() < other.area()
        else:
            return NotImplemented

################################################ 
# Pythonic Class
################################################

class Rectangle:
''' The commented out init method below instantiates our width and height in such a way
    that a rectangle can take negative values for width and height.
    To resolve this, we can write an init function that calls our property getter
    in order to run through some of the logic of the property. This can be seen in 
    the new init method directly below this commented out block.
    
    def __init__(self, width, height):
        self._width = width
        self._height = height
'''

    def __init__(self, width, height):
        self.width = width
        self.height = height

''' We can basically bypass Java like getters and setters by using our properties
    These properties can be left alone until they're actually needed, which is 
    helpful because we won't break backwards compatability even though we doing 
    instantiate the class with a get/set method'''

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('width must be positive')
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('height must be positive')
        else:
            self._height = height

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def getwidth(self):
        return self.width

    def setwidth(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        else:
            self.width = width

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self. area() < other.area()
        else:
            return NotImplemented
