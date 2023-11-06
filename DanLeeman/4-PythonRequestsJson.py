# https://www.youtube.com/watch?v=zZU0JZmIvKA&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=4

##########################
# 4-Python Requests Json #
##########################

"""
The requests library has a built-in json decoder to work with json content when it is sent in response from the server.
The JSON decoder allows us to parse the JSON response into Python objects.
JSON stands for JavaScript Object Notation and it is an easy and light format to transport data between a server and a client.
Data in JSON format is stored in name and value pairs separated by commas.
Object are denoted by the use of curly braces and arrays are defined by square brackets.
"""
import requests

r = requests.get('https://api.github.com/events')
events = r.json()

# Say we want to access the first event in the array. We can add square brackets with the index of 0 to the event object.
print(f"first event: {events[0]}")

"""
Now only the first event is printed to the console.
We can retrieve the id from this first event by adding another set of squre brackets to the event object with the string 'id'.
This is will return the id of the first event in the array.
This is just one example of retrieving specific data from an object created from parsed JSON content.
"""
print(events[0]['id'])

"""
We can also send JSON content in a request using the request library.
To send JSON content to the server, the requests method contais a keyword, json, that we can add to our requests.
We will define a new dictionary called data and add the key firstName with the value John.
"""
data = {'firstName': 'John'}
r = requests.post('https://httpbin.org/post', json=data)
print(r.text)
