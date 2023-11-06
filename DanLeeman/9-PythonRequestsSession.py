# https://www.youtube.com/watch?v=8qsNauBEVNM&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=9

#########################
# PythonRequestsSession #
#########################
"""
The use of sessions in a browser allows us to persit state information across multiple requests.
Sessions are used to store data for individual users which is tracked by a session ID.
The data for the user is stored on the server and the session ID is passed to the client, usually through a cookie.
The session ID is used to retrieve the existing data for the user on the server.
To create sessions using the request library, we will create session objects.
First, we will import the request library at the top of our script.
Then, we will declare an object and set that equal to requests.Session().
Note that the Session method has a capital S.
This line creates a new requests session object (s = requests.Session) which has all the same methods of the main requests API.
Before we demonstrate the ability to persist data across multiple requests, we are going to setup two dictionaries that contain the data we want to persist.
The first dictionary will be called userName and it will have a key of userName with a value of John99.
The second dictionary will be called location and it will have a key of location and a value NewYork.
"""
import requests
s = requests.Session()

"""
The first dictionary will be called userName and it will have a key of userName with a value of John99.
"""
userName = {'userName': "John99"}
location = {'location': 'NewYork'}

"""
Lastly, before we send the data to the server, we will setup a few urls that will be used in this script.
The first url we will call setCookieUrl and this will be instantiated with the string 'https://httpbin.org/cookies/set'.
This url on httpbin is used to create a new cookie on the server which is where we will store our data.
The second url we will create will be called getCookiesUrl and this will be instantiated with the string 'https://httbing.org/cookies'.
This url will return all the cookies currently setup on the server for our session.
Now that we have the data setup, we can store the data in a cookie on the server using our session object.
As long as this session object is alive, the cookies will persist the data across multiple request.
"""
setCookieUrl = 'http://httpbin.org/cookies/set'
getCookiesUrl = 'https://httpbin.org/cookies'

"""
We are able to use the get method for a session object similarly to sending a get request using the requests library.
We will use our requests session object s and call the get method on that object.
Within the get method, we will add our url setCookieUrl followed by the keyword params set equal to the userName dictionary we created.
"""
s.get(setCookieUrl, params=userName)

"""
We will repeat this process for the location dictionary to setup two new cookies that are placed within our session object.
"""
s.get(setCookieUrl, params=location)

"""
Now, we will declare a response object called r and set this equal to a get request performed on our session objects to the getCookiesUrl which will return all the cookies for our
current session.
To see the results, we will call the text method on the response object r and then print that to the console.
In the console, the response object contains our two new cookies location and UserName within the cookies section of the response body.
As you can see, the session object s persisted the cookies we created on the server through each request we performed, giving up access to the data as long as the session object
is alive.
"""
r = s.get(getCookiesUrl)
print(r.text)


