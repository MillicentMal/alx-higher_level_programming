#!/usr/bin/python3
"""
    3-rectangle: class Rectangle
"""


class Rectangle:
    """
        class Rectangle defines a rectangle
        Attributes:
            width (int): width of the rectangle
            height (int): height of the rectangle
            number_of_instances (int): number of
                rectangle instances
            print_symbol: representation of rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            initialises the instances
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            getter function for private attribute width
            Retruns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for private attribute width
            Args:
                value (int): new width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            getter function for private attribute height
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rectangle = ""
        if self.__width is 0 or self.__height is 0:
            return rectangle

        for i in range(self.__height - 1):
            rectangle += str(self.print_symbol) * self.__width + "\n"
        rectangle += str(self.print_symbol) * self.__width

        return rectangle

    def __repr__(self):
        rectangle = ''
        if self.__width is 0 or self.__height is 0:
            return rectangle
        rectangle = 'Rectangle({}, {})'.format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        """
            prints Bye rectangle... when an instance is
            deleted
        """
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            compares two rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        area_1 = rect_1.__width * rect_1.__height
        area_2 = rect_2.__width * rect_2.__height
        if area_1 == area_2 or area_1 > area_2:
            return rect_1
        return rect_2
