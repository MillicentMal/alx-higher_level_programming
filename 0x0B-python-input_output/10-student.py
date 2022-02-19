#!/usr/bin/python3
"""Student to JSON
"""


class Student:
    """ student class
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a new student.
       """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        """
        if (isinstance(attrs, list) and
                all(isinstance(i, str) for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
