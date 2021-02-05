#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ 10 hot posts. """
    sub = requests.get("https://reddit.com/r/{}/hot.json".format(subreddit),
                       headers={"User-Agent": "Custom"}, params={"limit": 10})

    if (sub.status_code == 200):
        for i in sub.json().get("data").get("children"):
            print("{}".format(i.get("data").get("title")))
    else:
        print(None)
