#!/usr/bin/python3
"""Making a class Student(same one as the 9)"""


class Student:
    def __init__(self, first_name, last_name, age):
        """def a func with fname, lname, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary represen... of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict
