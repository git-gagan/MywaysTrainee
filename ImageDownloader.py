#To search for an image interactively and download it as and when required
#using web scraping
import requests
from bs4 import BeautifulSoup
import re
import lxml
import os

def get_images(number, user_search):
    image_list = []
    for i in range(2,number + 3):
        pattern = "https://.*CAU"
        image = str(images[i])
        link = re.findall(pattern, image)
        if link:
            image_list.append(link[0])
    if not os.path.exists(user_search):
        os.mkdir(user_search)
        os.chdir(user_search)
    else:
        os.chdir(user_search)
    i = 0
    for image_url in image_list:
        image = requests.get(image_url).content
        with open(f"{user_search}{i}.jpg", "wb") as file:
            file.write(image)
        i += 1

if __name__ == "__main__":
    user_agent = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36"
    }

    user_search = input("Enter the image name you want to search : ")

    url = f"https://www.google.com/search?q={user_search}&sxsrf=ALeKk01jhwff1q4AzczSZGSvRJEmVA-ipA:1622654754449&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiElO2BvPnwAhWf63MBHTGQDhcQ_AUoAXoECAEQAw&biw=1536&bih=762"
    response = requests.get(url, headers = user_agent)

    soup = BeautifulSoup(response.text, "lxml")
    images = soup.find_all("img",{"class" : "rg_i Q4LuWd"})
    print("Total number of images : ",len(images))
    number = int(input("Enter the number of images you want : "))
    while number > len(images):
        print("You are asking for too much!")
        number = int(input("Enter again :"))
    get_images(number, user_search)
    print("Thanks for using, your images have been downloaded!")

