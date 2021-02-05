# API Advanced

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.
<center><img src="https://github.com/AlisonQuinter17/holberton-system_engineering-devops/blob/master/0x16-api_advanced/multimedia/apiadv.png" class="responsive"/></center>

RedditAPI: https://www.reddit.com/dev/api/

### 0. How many subs?
- Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

- Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

```shell
$ python3 0-main.py programming
756024
```
```shell
$ python3 0-main.py this_is_a_fake_subreddit
0
```

### 1. Top Ten mandatory
- Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

```shell
$ python3 1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
Spend effort on your Git commits
It's a few years old, but I just discovered this incredibly impressive video of researchers reconstructing sounds from video information alone
From the D Blog: Introspection, Introspection Everywhere
Do MVC like it’s 1979
GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
Google Bug Bounty - The 5k Error Page
PyCon 2017 Talk Videos
```
```shell
$ python3 1-main.py this_is_a_fake_subreddit
None
```

### 2. Recurse it! mandatory
- Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

- Hint: The Reddit API uses pagination for separating pages of responses.

- Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)

```shell
$ python3 2-main.py programming
932
```
```shell
$ python3 2-main.py this_is_a_fake_subreddit
None
```
