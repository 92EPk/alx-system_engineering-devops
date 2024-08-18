#!/usr/bin/python3
""" queries Reddit API and returns number of subscribers for a
    given subreddit """
import requests
import sys


def number_of_subscribers(subreddit):
    """ Returns number of subscribers to the subreddit,
        or 0 if subreddit requested is invalid """
    headers = {'User-Agent': '0x16-api_advanced'}
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(URL, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
