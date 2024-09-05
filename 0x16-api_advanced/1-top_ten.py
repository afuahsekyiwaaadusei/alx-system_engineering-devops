f
#!/usr/bin/python3
"""function that prints the
titles of the top 10 hottest posts a given subreddit."""


import requests


def top_ten(subreddit):
    """Prints the top 10 hottest posts listed for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            post = response.json().get('data').get('children')
            for i in range(10):
                print(post[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
