#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""


import requests
import sys


def append_post(hot_list, posts):
    """Append post to list"""
    if len(posts) == 0:
        return
    hot_list.append(posts[0]['data']['title'])
    posts.pop(0)
    append_post(hot_list, posts)


def recurse(subreddit, hot_list=[], after=None):
    """A recursive function that queries the Reddit API"""
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']
    append_post(hot_list, posts)

    after = data['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
