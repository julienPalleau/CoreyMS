# https://www.youtube.com/watch?v=Km28G1Sl1fY&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=6
import requests
###########################
# Python Requests Cookies #
###########################
"""
The Requests library gives us a way to create and read http cookies from the server.
According to the MDN documentation, a cookie is, "a small piece of data that a server sends to the user's web browser."
The cookie can be stored in the browser and it can be sent back to the server.
Cookies typically serve one of three purposes: Session Management for login or shopping carts, User Personalization, or Tracking user behavior
Uses for HTTP Cookies
    + Session Management
    + User Personalization
    + Tracking User Behavior
https://developer.mozilla.org/en-US/docs/web/HTTP/cookies

To send and receive cookies with the Requests library, we will start by importing requests.
Following the import, we will set a variable named url to the string 'https://httpbin.org/cookies'.
We will be using this url because it provides us with a simple response body to see the cookie information we sent to the server.
Let's say that we want to customize our user experience based on a users location.
This way we can provide shipping estimates for our products without the user having to enter an address.
To do this, we will request to know the user's location in the cookie and if they agree, the information will be stored in a cookie.
To mimic the content received in this event, we will declare a dictionary called cookies below our url variable with the key of location and a value of NewYork.
"""
url = "https://httpbin.org/cookies"
cookies = {'location': 'New York'}
"""
Next we will declare our response object r and set it equal to requests.get().
Within the get method, we will enter our url variable as the first parameter followed by the cookies keyword that will be set equal to our cookies dictionary from above.
Now that the request is setup, we can print the text from the response object using r.text
To receive a cookie from a server, we will use a cookie that is already setup on the google website.
We will declare a second response object named r and set this equal to requests.get().
Within the get method, we will enter our url variable as the first parameter followed by the cookies keyword that will be set equal to our cookies dictionary from above.
Now that the request is setup, we can print the text from the response object using r.text. When the script is run, we can see the cookie we just sent within the response body.
To receive a cookie from a server, we will use a cookie that is already setup on the google website.
We will declare a second response object named r2 and set this equal to requests.get().
Within the get method we will pass the string 'https://google.com'
Within this request, there is a cookie already created on the google server called 1P_JAR. (this cookies doesn't exist anymore to get the list of existing cookie use
print(r2.cookies.get_dict()).
To access the value of this cookie, we will call the cookies() function on the response object which returns special type of dictionary called the RequestsCookieJar.
To access the cookie in the response body from google.com, we will use square brackets to reference the name of the cookie we would like to see.
In this case we will pass the string '1P_JAR' within the square brackets. When we run the script, we will see the value of this cookie printed to the console.
As mentioned before, the Requests CookikeJar is a special form of dictionary that allows us to customize where we send our cookies. To demonstrate this, we will declare a new
RequestsCookieJar named requestsJar and instantiate it using requests.cookies.RequestsCookieJar().
To add a cookie to the requestsJar we will use the set function.
Within the set function, we will pass the name of our cookies as a string: 'userId' followed by the value of our cookie as a string: 'John99'. Using the domain and path keywords,
we can decide where each cookie where our new cookie information will be sent.
We will set the domain keyword to 'httpbin.org' and the path will be set to '/cookies'.
Next, we will copy and paste this line and change the cookie name to 'cartItem' with a value of 'laptop' and a path of '/cart'.
Now, we will create a get request to the same url as before and set the cookies keyword equal to the requestJar defined earlier which now contains two cookies.
When we print the value of r.text after this get request we receive only the userId cookie because the cartItem cookie was sent to the '/cart' path and not the '/cookies'
"""
r = requests.get(url, cookies=cookies)
print(r.text)

r2 = requests.get('https://google.com')
print(r2.cookies.get_dict())
print(r2.cookies['AEC'])
requestsJar = requests.cookies.RequestsCookieJar()
requestsJar.set("userId", "John99", domain="httpbin.org", path="/cookies")
requestsJar.set("cartItem", "laptop", domain="httpbin.org", path="/cart")
r3 = requests.get(url, cookies=requestsJar)
print(r3.text)