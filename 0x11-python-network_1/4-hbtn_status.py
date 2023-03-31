#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":

    import requests

    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        response.text.__class__, response.text))
