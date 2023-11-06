# https://www.youtube.com/watch?v=ET-RYAYl3GU&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=10

############################
# PythonRequestsEventHooks #
############################
"""
Event hooks using the requests library can be used to signal events when a response is generated from a request.
A hook callback function is called when a response is received from an http request.
The callback can be passed to each request by creating a dictionary containing the hook_name and callback_function.
Before we define the hooks dictionary we will import the requests library.
Next we will define a function called response_info which will take the following arguments: r, *args and **kwargs.
#https://www.geeksforgeeks.org/args-kwargs-python/
The *args arguments is used to pass a variable number of arguments to a function.
This allows the function to take in more arguments than the number of formally defined arguments.
The **kwargs parameter works similarly to *args except it takes in any number of keyword arguments passed to the function which are passed with a name corresponding to the argument.
Winthin the response_info function, we can call the status_code, url, and text functions on the response object r provided in the argument list and print them to the console.
"""
import requests


def response_info(r, *args, **kwargs):
    print(r.status_code, r.url)
    print(r.text)


"""
Now we can define a dictionary called hooks with a key of response and a value of response_info.
This corresponds the name of the hook, response, with the callback function we want called when the response hook event is triggered, response_info.
Now that we have a callback function and dictionary defined, we can create a response object r and set this equal to requests.get(). 
Within the get function we will add the url 'https://httpbin.org/get'.
This url is setup to return a response object when an http get request is sent to httpbin server.
Following the url, we will add the keyword hooks and assign the value hooks which is the name of the dictionary we defined earlier.
"""
hooks = {'response': response_info}
r = requests.get('https://httpbin.org/get', hooks=hooks)

"""
When this request is made, we can see that the status code, url and response body text are printed to the console because our function, response_info, was called as an event hook
for the response event.
We are also able to pass multiple callback functions within the hooks keyword.
To do this we will define another function called response_headers with the same arguments as the previous function.
This function will print the headers of the response object r using the headers function.
Now we can add this new function to the hooks dictionary by adding the name of the function within a tuple after the response_info function.
Our new function will now be called when the response event is triggered by the http get request.
When the request is made, we can see the output from the response_info callback function followed by the headers pringted by the response_headers function.

"""


def response_headers(r, *args, **kwargs):
    print(r.headers)


hooks = {'response': (response_info, response_headers)}
r = requests.get('https://httpbin.org/get', hooks=hooks)
