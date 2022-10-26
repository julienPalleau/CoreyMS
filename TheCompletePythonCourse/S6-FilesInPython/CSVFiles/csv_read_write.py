Without csv module
movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "Green Book", "director": "Farrelly"},
    {"name": "Amadeus", "director": "Forman"}
]


def write_to_file(output):
    with open("file.csv", "w") as f:
        f.write("name,director\n")
        for line in output:
            f.write(f"{line['name']},{line['director']}\n")


def read_from_file():
    with open("file.csv", "r") as f:
        content = f.readlines()
        for line in content[1:]:
            columns = line.strip().split("'")
            print(f"Name: {columns[0]}\tDirector: {columns[1]}")

# With csv module
import csv

movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "Green Book", "director": "Farrelly"},
    {"name": "Amadeus", "director": "Forman"}
]


def write_to_file(output):
    with open("file.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "director"])
        writer.writeheader()
        writer.writerows(output)


def read_from_file():
    with open("file.csv", "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(f"Name: {line['name']}\tDirector: {line['director']}")


read_from_file()
