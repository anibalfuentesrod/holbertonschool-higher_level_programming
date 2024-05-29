#!/usr/bin/python3
"""Desi and Seri using pickle method"""
import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        """Initilize some vars in this function"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """The intranet whants the displai this way :)"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Seri... using pickle and save it in filename[str]"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error derializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """this method will take filename as param, and using pickle
        it will load and return an instance of CustomObject
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None
