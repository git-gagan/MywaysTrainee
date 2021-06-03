import requests

response = requests.post("https://httpbin.org/post", data = {"k1":"v1","k2":"v2"})
#Data will be posted in a form encoded form, much like in HTML ones, just pass dictionary to data argument or list of tuples.
print(response.text)