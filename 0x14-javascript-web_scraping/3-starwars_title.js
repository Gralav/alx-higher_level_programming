#!/usr/bin/node
import requests
import sys

def get_movie_title(movie_id):
    url = f"https://swapi-api.alx-tools.com/api/films/{movie_id}"
    response = requests.get(url)
    if response.status_code == 200:
        movie = response.json()
        return movie['title']
    else:
        return None

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python swapi.py <movie_id>")
        sys.exit(1)

    movie_id = int(sys.argv[1])
    title = get_movie_title(movie_id)
    if title:
        print(title)
    else:
        print(f"No movie found with ID {movie_id}")

