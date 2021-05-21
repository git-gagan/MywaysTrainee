"""
Target :- Login to Twitter and tweet using selenium
"""

#Import Webdriver from selenium
from selenium import webdriver
import time

#get chrome 
driver  = webdriver.Chrome()    #specify executable_path as a param if chrome driver is not added to PATH

#Opening a URL
#Go to Google.com
driver.get("https://www.google.com")
driver.refresh()

time.sleep(1)

#Go to Twitter.com
driver.get("https://www.twitter.com")
driver.maximize_window()    #for full screen

time.sleep(2)

#navigation
driver.back()
driver.forward()

time.sleep(2)

#Clicking on button or link item
but = driver.find_element_by_link_text("Log in")
but.click()

time.sleep(2)
#Filling search boxes after locating them
searchbox1 = driver.find_element_by_name("session[username_or_email]")
searchbox1.send_keys("__gaganraj__")

time.sleep(1)

searchbox2 = driver.find_element_by_name("session[password]")
searchbox2.send_keys("***********")

#logging in using xpath
#xpath is a slow but very popular locator which works by navigating the DOM and uses xml path
button = driver.find_element_by_xpath("//span[@class = 'css-901oao css-16my406 css-bfa6kz r-poiln3 r-bcqeeo r-qvutc0']")
button.click()

time.sleep(3)
#Making a tweet by writing on box and clicking button
content = driver.find_element_by_xpath("//div[@class = 'public-DraftStyleDefault-block public-DraftStyleDefault-ltr' ]")
content.send_keys("This is tweeted using automation with the help of selenium and Python! #Automation #Selenium #Python\n")
time.sleep(1)
tweet = driver.find_element_by_xpath("//div[@class = 'css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-19u6a5r r-ero68b r-1gg2371 r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr']")
tweet.click()

#navigation and exit
time.sleep(3)
driver.quit()


'''
In order to get multiple text from the site
use:
driver.find_elements_by_name or others, This returns a list which can be iterated upon and the data can be checked using .text attribute

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")
time.sleep(5)
inp = driver.find_element_by_id("twotabsearchtextbox")
inp.send_keys("Phones")

search = driver.find_element_by_id("nav-search-submit-text")
search.click()

time.sleep(3)
list = driver.find_elements_by_xpath("//span[@class = 'a-size-medium a-color-base a-text-normal']")
for i in list:
    print(i.text)
'''












