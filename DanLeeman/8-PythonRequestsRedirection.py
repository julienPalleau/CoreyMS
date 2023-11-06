# https://www.youtube.com/watch?v=lfqG4q8hVew&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=8

###############################
# Python Requests Redirection #
###############################
"""
The Requests library performs location redirection for each of the HTTP request types such as:
    + Get
    + Post
    + Put
    + Delete

By default, location redirection will not be performed for the head HTTP verb.
The head http verb is used to request the headers returned from a resource if the resource was requested using an http get request.
The head request should not return a response body.
Let's start by importing the requests library.
Next we will create a get request by declaring a response object r and setting this equal to requests.get().
Within the get function, we will add the url 'http://github.com'.
Notice that the protocol used in the scheme of this url is http and not https.
This is on purpose because GitHub will automatically redirect all traffic through the http protocol to the https protocol.
When r.url is printed to the console, notice that the url from the response object uses the https protocol in the scheme.
However, when we call the status_code function on the response object, the code is 200 indicating a successful response even though we did not request the github page using the
https protocol.
To view the http status code that shows us the page has been redirected we must call the history function on the response object.
This function returns a list containing all of the response objects that were created in order to complete our request.
The list is sorts the responses from oldest to newest.
When the script is run, we can see the history function returned a single response object with the status code of 301, indicating the request has been redirected and the URL for
the resource has been moved permanently, as demonstrated by the URL returned from GitHub containing the https protocol in the scheme. If we would like to disable redirection in our
request, we can add the keyword allow_redirects within the get function.
"""
import requests
r = requests.get('http://github.com')
print(f'requests url: {r.url}')
print(f"requests status code: {r.status_code}")
print(f"r.history: {r.history}")

r= requests.get('http://github.com', allow_redirects=False)
print(f"We ran r= requests.get('http://github.com', allow_redirects=False) and we check r.history: {r.history}")
print(f'requests url: {r.url}')
r=requests.head('http://github.com', allow_redirects=True)
print(f"We ran r=requests.head('http://github.com', allow_redirects=True) and we check r.history: {r.history}")
print(f'requests url: {r.url}')
