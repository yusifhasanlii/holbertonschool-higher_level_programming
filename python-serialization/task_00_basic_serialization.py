#!/usr/bin/python3
'''
This module provides 2 functions to serialize and deserialize JSON files
'''
import json


def serialize_and_save_to_file(data, filename):
    '''
    The function to serialize data and save them to a file
    Args:
        data: The Python dictionary
        filename: The file to save on
    '''
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    '''
    The function to deserialize JSON file
    Args:
        filename: The file to load from
    '''
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
