import requests
from bs4 import BeautifulSoup as bs
"""
The function scrapes the profile picture URL 
of a GitHub user and prints it to the console.
"""


def github_profile_pic(username):
    profile_url = f"https://github.com/{username}"
    # Send a GET request to the profile URL
    req = requests.get(profile_url)
    # Parse the HTML content using BeautifulSoup
    scraper = bs(req.content, "html.parser")
    # Search for the profile picture URL
    profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
    return profile_picture


userName = "Afrahaden"
profile_pic_url = github_profile_pic(userName)
print(profile_pic_url)
