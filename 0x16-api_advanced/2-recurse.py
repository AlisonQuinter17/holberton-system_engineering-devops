#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Recurse it! """
    sub = requests.get("https://reddit.com/r/{}/hot.json".format(subreddit),
                       headers={"User-Agent": "Custom"},
                       params={"after": after})

    if (sub.status_code == 200):
        for i in sub.json().get("data").get("children"):
            hot_list.append(i.get("data").get("title"))
        after = sub.json().get("data").get("after")
        if after is None:
            return hot_list
    else:
        return None
    return recurse(subreddit, hot_list, after)
