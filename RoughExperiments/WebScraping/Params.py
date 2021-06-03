#Passing data in URL's query string, particularly used for URL redirect
import requests

param = {
    "v":"8ext9G7xspg"
}

response = requests.get("https://www.youtube.com", params = param)

print(response.url)