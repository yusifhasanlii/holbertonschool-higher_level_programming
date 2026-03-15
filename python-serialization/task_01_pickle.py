#!/usr/bin/python3
'''
This module provides a class to serialize and deserialize custom objects
using the pickle module.
'''
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Serialization failed: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Object is not of CustomObject type")
        except Exception as e:
            print(f"Deserialization failed: {e}")
        return None

    filename = "task_01_pickle.py"
