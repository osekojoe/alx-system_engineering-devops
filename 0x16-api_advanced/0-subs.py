#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""


import requests
import sys


def number_of_subscribers(subreddit):
    """Queries the Reddit API"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent":'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data = response.json()
    if 'data' not in data:
        return 0

    subscribers = data['data']['subscribers']
    if not subscribers:
        return 0

    return subscribers
