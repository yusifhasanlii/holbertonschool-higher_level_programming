#!/usr/bin/python3
'''
This module provide a single function that convert datas in a CSV file
to JSON using serialization
'''
import csv
import json


def convert_csv_to_json(filename):
    '''
    The function to transform CSV to JSON
    Args:
        filename: The name of the CSV file
    '''
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"Error occured: {e}")
        return False
