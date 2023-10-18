from collections import Counter

import requests
from bs4 import BeautifulSoup

from pprint import pprint


def extract_lyrics(url):
    print("Fetching lyrics...")
    r = requests.get(url)
    if r.status_code != 200:
        print("Page impossible a recuperer.")
        return []

    soup = BeautifulSoup(r.content, "html.parser")
    lyrics = soup.find("div", class_="lyrics")
    if not lyrics:
        return extract_lyrics(url)

    all_words = []
    for sentence in lyrics.stripped_strings:
        sentence_words = [word.strip(",").strip(".").lower() for word in sentence.split() if len(word) > 2]
        all_words.extend(sentence_words)

    counter = Counter(all_words)
    print(counter.most_common(10))


def get_all_urls():
    page_number = 1
    links = []
    while True:
        r = requests.get(f"https://genius.com/api/artists/29743/songs?page={page_number}&sort=popularity")
        if r.status_code == 200:
            response = r.json().get("response", {})  # {} pour renvoyer un dictionnaire vide si pas de response
            next_page = response.get("next_page")

            songs = response.get("songs")
            links.extend([song.get("url") for song in songs])
            page_number += 1

            if not next_page:
                print("No more pages to fetch.")
                break

    pprint(links)
    print(len(links))


extract_lyrics(url="https://genius.com/Patrick-bruel-elle-mregardait-comme-ca-lyrics")


# get_all_urls()


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"User(first_name='{self.first_name}', last_name='{self.last_name}"


patrick = User("Julie", "Smith")
print(repr(patrick))
julie = User(first_name='Julie', last_name='Smith')
print(julie)
