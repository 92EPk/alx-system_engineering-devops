#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests
import time

def number_of_subscribers(subreddit, retries=5, timeout=10):

    
    # Construct the URL for the subreddit about endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a new User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    
    for attempt in range(retries):
        try:
            # Make the request to the Reddit API
            response = requests.get(url, headers=headers, timeout=timeout)
            
            # Check if the subreddit is valid by inspecting the response status code
            if response.status_code == 404:
                return 0  # Invalid subreddit
            
            # Check if the response was successful
            if response.status_code == 403:
                print(f"Attempt {attempt + 1} failed: Access forbidden (403). Please check if the subreddit exists.")
                return 0  # Handle forbidden access
            
            if response.status_code != 200:
                print(f"Attempt {attempt + 1} failed with status code: {response.status_code}")
                time.sleep(2)  # Wait before retrying
                continue  # Retry on failure
            
            # Parse the JSON response
            data = response.json()
            return data['data']['subscribers']
        
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            time.sleep(2)  # Wait before retrying
    
    return 0  # Return 0 if all retries fail

