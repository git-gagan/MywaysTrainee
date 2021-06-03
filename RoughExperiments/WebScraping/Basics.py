#Web Scraping : Extracting data from Websites
#Encode: unicode to bytes(utf-8)
#decode : bytes to unicode
#unicode: Set of characters used all over the world
#UTF: Character Encoding Scheme

import requests #more abstract
import urllib.request, urllib.parse, urllib.error

#To get Header Data:
response = requests.get("https://myways.in/student/premium")
print(response.headers,"\n") #response header
print(response.request.headers) #request header

#Stating Data suing dictionaries
user = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36"
}

new_response = requests.get("https://myways.in/student/premium", headers = user)
print(new_response.headers,"\n")
print(new_response.request.headers)

#Scrap Data
url  = urllib.request.urlopen("https://myways.in/student/premium")
print("\n",url)
for line in url:
    print("\n",line.decode().strip(),"\n")

