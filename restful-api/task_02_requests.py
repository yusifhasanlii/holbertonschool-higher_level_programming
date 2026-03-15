#!/usr/bin/python3
'''
This module provides 2 functions to fetch datas with requests.
'''
import requests
import csv


def fetch_and_print_posts():
    '''
    This function will fetch posts from JSONPlaceholder and displays them
    to the stdout.
    '''
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        data = r.json()
        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    '''
    This function will fetch posts from JSONPlaceholder and saves them
    to a CSV file named 'posts.csv'.
    '''
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        data = r.json()
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            fields = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()

            for row in data:
                filtered_row = {key: row[key] for key in fields}
                writer.writerow(filtered_row)
