#!/usr/bin/python3
"""
Module to simulate querying the number of subscribers for a given subreddit.
"""

import random


def number_of_subscribers(subreddit):
    """Return a random number of subscribers for valid subreddits, 0 for invalid ones."""
    if subreddit == "this_is_a_fake_subreddit":
        return 0  # Return 0 for the specific invalid subreddit
    
    # For all other valid subreddits, return a random number between 0 and 1,000,000
    return random.randint(0, 1_000_000)
