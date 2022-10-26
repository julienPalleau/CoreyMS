import json

json_list = []

with open('csv_file.txt', 'r') as f:
    content = f.readlines()
    i = 0
    for line in content:
        club, city, country = line.strip().split(',')
        data = {
            'club': club,
            'city': city,
            'country': country,
        }
        json_list.append(data)

    json_file = open('json_file.txt', 'w')
    json.dump(json_list, json_file)
    json_file.close()

