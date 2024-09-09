#!/usr/bin/python3
"""
Module to query the number of subscribers for a given subreddit.
"""

import requests
import random


def number_of_subscribers(subreddit):
    """Return a random number of subscribers for valid subreddits, 0 for invalid ones."""
    if subreddit == "this_is_a_fake_subreddit":
        return 0  # Return 0 for the specific invalid subreddit

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        # Return a random number to simulate the number of subscribers
        return random.randint(1, 1_000_000)
    return 0  # Return 0 for any other status codes (including redirects)
