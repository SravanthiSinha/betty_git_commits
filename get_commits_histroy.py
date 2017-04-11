#!/usr/bin/python3
import requests
import json

url = 'https://api.github.com/repos/holbertonschool/Betty/commits'
response = requests.get(url)
repos = {}

if(response.ok):
    repoItems = json.loads(response.text or response.content)
    for repo in repoItems:
        date = repo['commit']['committer']['date']
        commitid = repo['sha']
        committer = repo['commit']['committer']['name']
        message = repo['commit']['message']
        op = date + ": " + commitid + " - " + committer + " - " + message
        repos[date] = op

for k, v in sorted(repos.items(), reverse=True):
    print(v)
