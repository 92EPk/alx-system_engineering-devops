#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests
from collections import Counter
import re

def count_words(subreddit, word_list):
    # Construct the URL for the subreddit hot endpoint with pagination
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    
    # Set a new User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if the subreddit is valid by inspecting the response status code
        if response.status_code == 404:
            return  # Invalid subreddit
        
        # Check if the response was successful
        if response.status_code != 200:
            print(f"Failed to retrieve hot posts. Status code: {response.status_code}")
            return
        
        # Parse the JSON response
        data = response.json()
        
        # Recursively fetch all hot posts
        hot_list = fetch_hot_posts(data, subreddit, headers)
        
        # Count the occurrences of keywords in the hot_list
        count_keyword_occurrences(hot_list, word_list)
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def fetch_hot_posts(data, subreddit, headers, hot_list=None):
    if hot_list is None:
        hot_list = []
    
    # Add the titles of the current page to the hot_list
    for post in data['data']['children']:
        hot_list.append(post['data']['title'])
    
    # Get the 'after' token for the next page
    after = data['data']['after']
    
    # Recursively fetch the next page of hot posts
    if after:
        # Construct the URL for the next page
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
        
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Parse the JSON response
        next_data = response.json()
        
        # Recursively call the function with the next page
        hot_list = fetch_hot_posts(next_data, subreddit, headers, hot_list)
    
    return hot_list

def count_keyword_occurrences(hot_list, word_list):
    # Create a Counter to count occurrences of each keyword
    word_counts = Counter()
    
    # Compile regex patterns for each keyword to match whole words
    patterns = {word.lower(): re.compile(r'\b' + re.escape(word.lower()) + r'\b') for word in word_list}
    
    # Count occurrences in each title
    for title in hot_list:
        for word, pattern in patterns.items():
            word_counts[word] += len(pattern.findall(title.lower()))
    
    # Print the sorted word counts
    for word, count in sorted(word_counts.items(), key=lambda x: (-x[1], x[0])):
        if count > 0:
            print(f"{word}: {count}")
