import requests
# https://www.youtube.com/watch?v=J77cz4mqolA&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=3
##################################
# Python Requests: Upload a File #
##################################
# https://www.youtube.com/watch?v=J77cz4mqolA&list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV&index=3

"""
The requests library has a simple way of posting multipart encoded files to a server. We would use this feature when there is a file input for a form on website.
When the form is submitted, the file has to be sent to the server as binary data and not url encoded data.
To post a Multipart-Encoded file using the Requests library, we have a little prep to do before we get into the code.

For convenience, I have placed the csv file in the same directory as the python script. In the python script, I will first import the request library.
I will define a variable named url and set this equal to the string https://httpbin.org/post.
url = 'https://httpbin.org/post'
This url provides us a response object where we caneasily view the files we sent to the server.
Next we will define a dictionary named files with the key of 'file' section within the response object shows the information contained in our USCarBrands.csv file we sent
through http post protocol using the requests library.
files = {'file': open('USCardBrands.csv', 'rb')}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

If we wanted to post multiple files to the same url, we can modify the files dictionary.
We will change this dictionary into a list of tuples where each tuple contains an identifier for the image and a nested tuple.
I will call these identifiers copy1 and copy2.
files = [('copy1', ('USBCarBrands.csv', open('USCarBrands.csv', 'rb), 'csv')),
         ('copy2', ('USBCarBrands.csv', open('USCarBrands.csv', 'rb), 'csv')),
]
Within the nested tuple, we will include the filename, the file, and the filetype. For our example, I will enter the same information within the nested tuple for copy1 and copy2.
"""
url = 'https://httpbin.org/post'
# files = {'file': open('USCarBrands.csv', 'rb')}

files = [('copy1', ('USBCarBrands.csv', open('USCarBrands.csv', 'rb'), 'csv')),
         ('copy2', ('USBCarBrands.csv', open('USCarBrands.csv', 'rb'), 'csv'))
]

r = requests.post(url, files=files)
print(r.status_code)
print(r.text)