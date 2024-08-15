#!/usr/bin/python3
"""
This module provides a function to get the number of subscribers for a given subreddit using the Reddit API.
"""
def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "MyUserAgent"
            }
    response = requests.get(url, headers = headers, allow_redirects = False)
    if response.status_code >= 300:
        return 0
        
    results = response.json().get("data")
    return results.get("subscribers")

