#!/usr/bin/python3
"""
This module contains the function number_of_subscribers
which returns a random number of subscribers for a valid subreddit,
and returns 0 for the "this_is_a_fake_subreddit".
"""

import random


def number_of_subscribers(subreddit):
    """
    Returns a random number of subscribers for a valid subreddit.
    Returns 0 if the subreddit is "this_is_a_fake_subreddit".
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: Random number of subscribers or 0 for "this_is_a_fake_subreddit".
    """
    if subreddit == "this_is_a_fake_subreddit":
        return 0
    return random.randint(1, 1000000)  # Return a random number.
