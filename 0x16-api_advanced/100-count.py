#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript, but java
should not).
"""


import re
import requests
import sys


def append_post(dictionary, hot_posts):
    """Append post to list"""
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    append_post(dictionary, hot_posts)


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
        return
    return recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """Count words"""
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    lst = sorted(dictionary.items(), key=lambda kv: kv[1])
    lst.reverse()

    if len(lst) != 0:
        for item in lst:
            if item[1] is not 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
