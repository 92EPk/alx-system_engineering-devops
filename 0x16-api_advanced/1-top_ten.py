#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests
import time

def top_ten(subreddit):
    # Construct the URL for the subreddit hot endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set a new User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if the subreddit is valid by inspecting the response status code
        if response.status_code == 404:
            print(None)  # Invalid subreddit
            return
        
        # Check if the response was successful
        if response.status_code != 200:
            print(f"Failed to retrieve hot posts. Status code: {response.status_code}")
            return
        
        # Parse the JSON response
        data = response.json()
        
        # Print the titles of the first 10 hot posts
        for post in data['data']['children']:
            print(post['data']['title'])
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

