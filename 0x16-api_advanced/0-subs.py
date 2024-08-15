#!/usr/bin/env python3
"""
0-subs.py

This module provides a function to get the number of subscribers for a given subreddit using the Reddit API.
"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0

if __name__ == "__main__":
    print(number_of_subscribers('learnpython'))
