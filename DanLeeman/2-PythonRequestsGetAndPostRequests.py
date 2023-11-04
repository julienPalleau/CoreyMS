# https://www.youtube.com/playlist?list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV
# https://www.youtube.com/watch?v=qriL9Qe8pJc&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=2
import requests

##########################################
# Python Requests: Get and Post Requests #
##########################################

# get requests
"""
Http Get Request are used for retrieving data from a specified resource.
The content received from a get request could be used for rendering a list of data retrieved from an API or for filtering a list of products based on a query string.

    + Render a list of data
    
?search=camera  <--- Filter based on query string

Get requests should not be used for sensitive information

To make an http get request using the python requests library, we first must import requests. We will then declare a response object called r and set this object equal to
request.get().
In the get function, we will pass a string containing the url for the get request. The url we will use is "https://httbin.org/get". When the request to this url is made, our
response object r will contain the information received from the url.
We will be using httpbin because it provides us with a quick, simple way to send and receive well formatted responses from a server.
Httbin acts much like an API from google or twitter, however httpbin is an option to quickly test our http requests without needing authentication.

As you can see, we have entered the base URL httbing.org and appended /get to the end of the base URL which will send an http request to the get as noted in the documentation.
In addition, we can pass url parameters through the requests get function.
URL parameters are declared as a query string in the url and are a way to dynamically send additional information to a page. 

https://httpbin.org/get?
To indicate a query string, a question mark is placed after the domain name and path which indicates the query string has started and the following text is parameter 
names and values written in pairs.
                                Parameter Names
                        ---------      --------
https://httpbin.org/get?firstName=John&lastName=Smith
                                  ----          -----
                                        Values
                                        
After the parameter name is declared, an equals sign will be appended to the query string to assign a value to the parameter. To add multiple parameters with corresponding values,
we'll use and '&' after each value and before the next parameter name.

payload = {"firstName": "John", "lastName": "Smith"}
r = requests.get("https://httpbin.org/get", params=payload)

To add URL parameters to our get requests, we will declare a dictionary above the response object called 'payload' with two parameters named 'firstName' and 'lastName' with
values of 'John and 'Smith respectively.

Within the get function, we will add a second parameter called params and set this equal to the payload we just created.
The keyword params will convert the payload dictionary we just created into a query string which can be sent to the specified url.

print(r.url)
Printing the r.url to the console will reveal the full url and after the question mark indicating the start of a query string, we can see keys and values from the payload
dictionary have been url encoded.
We can view the http response code by calling the status_code function on the response object.
An http response code of 200 indicates a successful request has been made.
To view the response content from our url, we have a couple options.
    + The first option is to call the content function on the response object r. 
        print(r.content)
    + Another option is to used r.text. This function will return the response body that is decoded by the request libray based on the http headers passed in the http request.
    Within the args object of the response body, we see our parameters that we passed through the get request
        print(r.text)
"""

# First syntax with parameters within URL
r = requests.get("https://httpbin.org/get?firstName=John&lastName=Smith")
print(r.text)

# Second syntax using params that takes parameters under the form of a dictionary
payload = {"firstName": "John", "lastName": "Smith"}
r = requests.get("https://httpbin.org/get", params=payload)
print(f"It returns the url: {r.url}")
print(f"It returns the status code: {r.status_code}")
print(f"It returns the site content at the url used above: \n{r.content}")


# post requests
"""
Post requests are used most often when:
+ Submitting data from an html form
+ Uploading Files: jpg, psd, mp4, png, html, css, js, pdf, ai, id, php, tiff
Allows larger amounts of resources to be sent in a single request

r = requests.post("https://httbin.org/post", data=payload)
To convert our get request to a post request there just a few changes that need to be made.
    + First, we will change the function from get to post.
    + Then, within the post function we will change our url to 'https://httpbin.org/post' which is an endpoint setup by httpbin to receive data from a form or a file.
    + Finally, we will change the params keyword to the keyword data which will convert our payload dictionary to send to our url. Note that '/post/ rout on httpbin is expecting
    a form or file in the post request so the data keyword will handle the conversion of the payload dictionary.

Now we are able to run the script and this time send a post request instead of a get request.
Notice that the URL property of the response object is now the same url that we passed in the post function.
This is because when we use the http post protocol, the parameters are not url encoded like in the get request.
The dictionary passed through the post request is submitted to our server and is shown in the form object within the response body.
"""
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
