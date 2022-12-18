#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    hdrs = {"Accept": "application/vnd.github.v3+json"}
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)
    req = requests.get(url, headers=hdrs)
    for commit in req.json()[0:10]:
        [print('{}: {}'.format(commit['sha'], commit['commit']['author']['name']))]
