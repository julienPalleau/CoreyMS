import requests

r = requests.get('https://xkcd.com/353/')
print(dir(r))

r = requests.get('https://xkcd.com/353/')
print(help(r))

r = requests.get('https://xkcd.com/353/')
print(r.text)

r = requests.get('https://imgs.xkcd.com/comics/python.png')

with open('comic.png', 'wb') as f:
    f.write(r.content)

payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.url)
print(r.text)
print(r.json())

r_dict = r.json()

print(r_dict['form'])

r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'), timeout=3)
print(r.text)
print(r)
#
# r = requests.get('https://httpbin.org/delay/6', timeout=20)
# print(r)