import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")


def get_movies():
    with open(DATA_FILE, "r") as f:
        movies_title = json.load(f)

    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies


class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def add_to_movies(self):
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} est déjà enregistré.")
            return False

    def _get_movies(self):  # methode privee car elle commence par _
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):  # methode privee car elle commence par _
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    def remove_from_movies(self):
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} n'est pas enregistré.")
            return False


if __name__ == "__main__":
    # m = Movie("Harry Potter")
    # m = Movie("Full Metal Jacket")
    # print(m)
    # print(m._get_movies())
    # print(m.add_to_movies())
    # print(m._get_movies())
    # m._write_movies(["Le Seigneur Des Anneaux", "Orange mecanique"])
    # print(m.remove_from_movies())
    # m._write_movies()
    # print(m._get_movies())

    m = get_movies()
    print(m)
