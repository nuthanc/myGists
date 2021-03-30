# first: mkdir user && cd user && cp /path/to/get_gists.py .
# python3 get_gists.py user
import os
import json
import requests
import sys
from subprocess import call

# user = sys.argv[1]

# r = requests.get('https://api.github.com/users/{0}/gists'.format(user))

# for i in r.json():
#     folder = i['description'][0:255] if i['description'] else i['id']
#     call(['git', 'clone', i['git_pull_url'], folder])
#     description_file = './{0}/description.txt'.format(folder)
#     with open(description_file, 'w') as f:
#         f.write('{0}\n'.format(i['description']))


def download_gists(gists: list):
    for gist in gists:
        folder = gist['description'][0:255] if gist['description'] else gist['id']
        call(['git', 'clone', gist['git_pull_url'], folder])
        description_file = './{0}/description.txt'.format(folder)
        with open(description_file, 'w') as f:
            f.write('{0}\n'.format(gist['description']))


def visit_pages(user: str):
    next_page = True
    page = 1
    while next_page:
        url = f"https://api.github.com/users/{user}/gists?page={page}"
        r = requests.get(url)

        if not len(r.json()):
            next_page = False
        else:
            page += 1

        download_gists(r.json())


user = sys.argv[1]
visit_pages(user)
