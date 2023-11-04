import requests

################
# get requests #
################
# First syntax
r = requests.get("https://httpbin.org/get?firstName=John&lastName=Smith")

# Second syntax
payload = {"firstName": "John", "lastName": "Smith"}
r = requests.get("https://httpbin.org/get", params=payload)
print(f"It returns the url: {r.url}")
print(f"It returns the status code: {r.status_code}")
print(f"It returns the site content at the url used above: \n{r.content}")

#################
# post requests #
#################
"""
+ Submitting data from an html form
+ Uploading Files: jpg, psd, mp4, png, html, css, js, pdf, ai, id, php, tiff
Allows larger amounts of resources to be sent in a single request

To convert our get request to a post request there just a few changes that need to be made.
    + First, we will change the function from get to post.
    + Then, within the post function we will change our url to 'https://httpbin.org/post' which is an endpoint setup by httpbin to receive data from a form or a file.
    + Finally, we will change the params keyword to the keyword data which will convert our payload dictionary to send to our url.
"""
