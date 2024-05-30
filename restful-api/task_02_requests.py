#!/usr/bin/python3
"""A basic Python script to fetch posts form JSONPlaceholder"""
import requests
import csv


def fetch_and_print_posts():
    """"""

    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """comment"""

    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        data = []
        for post in posts:
            post_data = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']}
            data.append(post_data)

        with open('posts.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)
