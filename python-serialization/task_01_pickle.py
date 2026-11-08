#!/usr/bin/env python3
"""Custom class serialization"""


import pickle


class CustomObject:
    """Custom class"""
    def __init__(self, name, age, is_student):
        """constroctor"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the content of object"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize a custom class"""
        with open(filename, "wb") as customfile:
            pickle.dump(self, customfile)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a custom class"""
        try:
            with open(filename, "rb") as myfile:
                return pickle.load(myfile)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
