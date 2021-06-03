from bs4.builder import HTML
import requests
"""
url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
response  = requests.get(url)

#.content returns data in form of bytes, .text returns in form of unicode
#Download the content (Google Image)
#copy image address
f = open("Image.png","wb")
f.write(response.content)
f.close()
"""
#Filtering Data
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://www.updateland.com/best-free-movie-streaming-sites-no-sign-up/")

soup = BeautifulSoup(response.content, "lxml") #Gives us an easily traversable XMl structure
tag = soup.find("div").find_all("h3")
"""h3 = soup.find_all("h3")
for title in h3[:-2]:
    print(title.text)"""
#print(tag)

#Write to CSV
import csv

with open("Data.csv","w") as file:
    #call the csv writer object
    writer = csv.writer(file)
    writer.writerows(tag)

