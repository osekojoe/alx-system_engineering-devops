#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed
 for a given subreddit.
"""


import requests
import sys


def top_ten(subreddit):
    """queries the Reddit API"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    headers = {
        "User-Agent": 'Mozilla/5.0'
    }
    
    params = {
        'limit': 10
    }

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    
    if response.status_code != 200:
        print(None)

    data = response.json()
    posts = data['data']['children']
    
    if len(posts) == 0:
        print(None)

    for post in posts:
        title = post["data"]["title"]
        print(title)
