#!/usr/bin/python3
"""Making a class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """def a func with fname, lname, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary represen... of a Student instance"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
