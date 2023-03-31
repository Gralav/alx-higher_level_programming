#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password) and
uses the Github API to display your id
"""
if __name__ == "__main__":

    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get('https://api.github.com/user',
                            auth=(username, password))
    json_response = response.json()
    print(json_response.get('id'))
