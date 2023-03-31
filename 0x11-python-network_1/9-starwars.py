#!/usr/bin/python3
"""
Python script that takes in a string and sends a search request to
the Star Wars API (https://swapi.co/documentation)
"""
if __name__ == "__main__":

    import requests
    import sys

    search = sys.argv[1]
    url = 'https://swapi.co/api/people/?search=' + search
    response = requests.get(url)
    json_response = response.json()
    print("Number of results: {}".format(json_response.get('count')))
    for count in range(len(json_response.get('results'))):
        print(json_response.get('results')[count].get('name'))
