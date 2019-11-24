from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random

### NOT WORKING!!

# which username should i get following users
photolink = input("Enter photo URL: ")

# load Cookies so you dont need to login every time
# check where are your cookies in chrome://version/ at Profile Path parameter
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("user-data-dir=/home/petry/.config/chromium/Default")

# opens browser
browser = webdriver.Chrome(options=chrome_opt)

# enters username instagram profile
browser.get(photolink)


# timer to wait loading everything
time.sleep(5)

# check how many following loaded, so we can scroll down until all following users are loaded
# xpath to the div where all followings are

exists = 1
while exists:
    try:
        #xpath to button to load more comments
        browser.find_elements_by_xpath('//span[contains(@aria-label, "Load more comments")]').click()
        time.sleep(2)
    except:
        try:
            browser.find_elements_by_xpath('//span[contains(@aria-label, "Load more comments")]').click()
            time.sleep(2)
        except:
            print("No more buttons to load more comments")
            exists = 0

#xpath to username of commenters
try:
    FList = browser.find_element_by_xpath('
    
    //h3[@class="_6lAjh"]/a')
except:
    print("Error: could not find element of following loaded")

total_comments = len(FList)

print("Total comments loaded: " + str(total_comments))

browser.quit()