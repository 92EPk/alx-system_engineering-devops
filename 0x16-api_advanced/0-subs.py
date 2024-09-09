#!/usr/bin/python3
"""
Script that simulates querying subscribers on a given Reddit subreddit.
"""

import random


def number_of_subscribers(subreddit):
    """Return a random number of subscribers for a given subreddit."""
    # Generate a random number between 0 and 1,000,000
    return random.randint(0, 1_000_000)


# Example usage
if __name__ == '__main__':
    subreddit = 'example_subreddit'  # Replace with any subreddit name
    print(f'Subscribers for r/{subreddit}: {number_of_subscribers(subreddit)}')
