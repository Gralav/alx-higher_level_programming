#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":

    import requests
    from requests.exceptions import HTTPError
    import sys

    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        print(response.text)
    except HTTPError as e:
        print("Error code: {}".format(str(e).split(' ')[0]))
