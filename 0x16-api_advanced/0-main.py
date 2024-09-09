#!/usr/bin/python3
"""
0-main: This script allows you to check the number of subscribers
for a given subreddit using the function from 0-subs.py.
"""

import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
