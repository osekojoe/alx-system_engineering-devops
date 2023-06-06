#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed
 for a given subreddit.
"""


import requests
import sys


def top_ten(subreddit):
    """Queries the Reddit API"""
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data['data']['children']
    if len(posts) is 0:
        print(None)
    else:
        for post in posts:
            title = post['data']['title']
            print(title)
