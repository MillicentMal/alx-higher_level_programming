#!/usr/bin/python3
"""Student
"""


class Student:
    """ student Class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns dict representation
        """
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        """
        for k, v in json.items():
            setattr(self, k, v)
