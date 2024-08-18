#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    # Set the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Specify a custom User-Agent to avoid ‘Too Many Requests’ errors
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the subreddit does not exist, a 404 status code will be returned
        if response.status_code == 404:
            return 0
        
        # If the request was successful, parse the JSON response
        data = response.json()
        
        # Return the number of subscribers
        return data['data']['subscribers']
    
    except Exception as e:
        # In case of any other exceptions, return 0
        return 0
