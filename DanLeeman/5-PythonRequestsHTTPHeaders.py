#https://www.youtube.com/watch?v=bPZvWJLx_jA&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=5

#################################
# 5-Python Requests HTTTPHeaders #
#################################

"""
When a request is made to the server, the reponse object contains headers which pass additional information within the request.
One common header sent in a request is the content-type header which is used to indicate the media type of the resource being sent in the request.
Some common media types are: 'application/json', 'text/plain', 'text/javascript', and 'multipart/form-data'.
The use of the content-type header is important to inform the server what type of content to receive, or for the client to only accept the media types expected in the response.
To send a custom header with our request, we will create a new file with the requests library imported.
Then we will create a dictionary called headers, with a key of Content-Type and value of multipart/form-data.
"""
import requests
headers = {'content-type': 'multipart/form-data'}

"""
Next, we will create a new response object r and set this equal to requests.post(). Within the get function, we will enter the url in quotes, 'https://httpbin.org/post'. This
url is an endpoint setup to return a response object when a post request is sent the httpbin server.
In order to send our custom headers with this post request, we will add the headers keyword within the post function and assign our headers dictionary to the keyword.
"""
r = requests.post('https://httpbin.org/post', headers=headers)

"""
To view the custom header sent in the request, we can call the request function on the response object r to retrieve the request object, and then chain on the headers function to
retrieve the headers for the request object. When this is printed to the console, we can see our header Content-Type has been sent in the request with our value of 
multipart/form-data.
We can also view the headers on the response request from the server by calling the headers function on the response object r.
Note that we will not call rhe requests function on the response object r because we want to work with the response from the server and not the request made to the server.
When the headers function is called, it will return a dictionary of all the headers from the response object.
This dictionary is special because the keys used to reference each corresponding value are case-insensitive.
To retrive the value of a particular header, such as content-type, we will add squre brackets after the headers function and with quotes, the name content-type will be added.
When the request is executed, the value of the content-type header from the response object will be printed to the console.
In this case, the value of the content-type header on the response object is 'application/json'.
"""
print(r.headers['Content-Type'])