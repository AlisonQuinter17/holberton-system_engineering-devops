#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of
subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Return the total number of subscribers. """
    sub = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                       headers={"User-Agent": "Custom"})

    if (sub.status_code == 200):
        return sub.json().get("data").get("subscribers")
    else:
        return (0)
