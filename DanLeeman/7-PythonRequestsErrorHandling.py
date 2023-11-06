# https://www.youtube.com/watch?v=Mw8K_QkoUUg&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=7

#######################
# Python Requests Error #
#######################
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

"""
Sometimes requests to a url will return an unsuccessful response.
We can tell the response was unseccessful by looking at the status code of the response object.
Examples of unsuccessful status codes are: a 400 bad request code, a 404 not found code, or a 500 internal server error code.
To handle these error codes, we will create a new script with the request libarary imported.
Next, we will create a new response object r, and set this equal to requests.get(). Within the get function, we will add the url 'https://httpbin.org/status/404'.
This url is an endpoint setup to return a response object with a 404 status code.
When we call the raise_for_status function on the response object r, an HTTPError will be raised.
This function will raise an HTTPError when the status code for the response object is a client error, any status code in the 400's, or a server error, which is any status code
in the 500's.
If we call raise_for_status on a response object that has a 200 status code, an error will not be raised and instead will return the value none.
Another common exception is a timeout exception.
This occurs if 0 bytes from the server are received for a defined period of time.
To define the number of seconds for the requests library to wait for a response from the server, we can use the timeout keyword in our get function.
To replicate a timeout error, we will set the value of the timeout keyword to 1/10th of a second.
This amount of time will raise a timeout error because the server at httpbin will not be able to send a response within 1/10th of a second.
It is good practice to define a timeout value for each request made because this will prevent the program from hanging, or waiting too long for a non-responsive server.

"""
import requests
r = requests.get("https://httpbin.org/status/404")
r.raise_for_status()

r = requests.get("https://httpbin.org/status/200", timeout=0.1)