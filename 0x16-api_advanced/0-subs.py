#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    
    # Check if the subreddit is valid
    if response.status_code == 404:
        return 0
    
    # If valid, extract the number of subscribers
    data = response.json()
    return data['data']['subscribers']
