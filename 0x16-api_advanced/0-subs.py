#!/usr/bin/python3
"""
This module contains the function number_of_subscribers
which queries the Reddit API to return the number of subscribers
for a given subreddit using a SOCKS5 proxy and a random User-Agent.
"""

import random
import requests

# List of User-Agent strings
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) "
    "Gecko/20100101 Firefox/89.0",
    # Add more User-Agents here
]

# Define the SOCKS proxy settings (Replace with actual SOCKS5 proxy)
PROXIES = {
    "http": "socks5://185.38.111.1:1080",  # Replace with your SOCKS5 proxy address and port
    "https": "socks5://185.38.111.1:1080",  # Replace with your SOCKS5 proxy address and port
}


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit using a SOCKS5 proxy and a random User-Agent.
    Args:
        subreddit (str): The name of the subreddit.  
    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Randomly select a User-Agent from the list
    headers = {
        "User-Agent": random.choice(USER_AGENTS)
    }
    
    try:
        response = requests.get(
            url,
            headers=headers,
            proxies=PROXIES,
            allow_redirects=False
        )
        
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        
        return 0
    
    except requests.RequestException:
        return 0
