#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []
    
    # Construct the URL for the subreddit hot endpoint with pagination
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    
    # Set a new User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if the subreddit is valid by inspecting the response status code
        if response.status_code == 404:
            return None  # Invalid subreddit
        
        # Check if the response was successful
        if response.status_code != 200:
            print(f"Failed to retrieve hot posts. Status code: {response.status_code}")
            return None
        
        # Parse the JSON response
        data = response.json()
        
        # Add the titles of the current page to the hot_list
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        
        # Get the 'after' token for the next page
        after = data['data']['after']
        
        # Recursively call the function with the next page
        if after:
            recurse(subreddit, hot_list, after)
        
        return hot_list
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

