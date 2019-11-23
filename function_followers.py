from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random

# which username should i get the follower
username = input("Username: ")

# load Cookies so you dont need to login every time
# check where are your cookies in chrome://version/ at Profile Path parameter
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("user-data-dir=/home/petry/.config/chromium/Default")

# opens browser
browser = webdriver.Chrome(options=chrome_opt)

# enters username instagrem profile
browser.get("https://www.instagram.com/" + username)

# check the total followers username has
totalfollowers = int(browser.find_element_by_xpath('//a[@href="/' + username + '/followers/"]/span').get_attribute("title"))

print("Followers: " + str(totalfollowers))

# open followers
try:
    userbio = browser.find_element_by_xpath('//a[@href="/' + username + '/followers/"]/span').click()
except:
    print("Error: could not find element to open followers")

# timer to wait loading everything
time.sleep(5)

# check how many followers loaded, so we can scroll down until all followers are loaded
# xpath to the div where all followers are
try:
    FList = browser.find_element_by_xpath('//div[@role="dialog"]/div/ul/div')
except:
    print("Error: could not find element of followes loaded")

numberOfFollowersInList = len(FList.find_elements_by_css_selector('li'))

# load all followers

actionChain = webdriver.ActionChains(browser)
time.sleep(random.randint(2,4))

# send two TABs key so element is selected and we can send SPACE keys to scroll down element and load all followers
actionChain.send_keys(Keys.TAB)
actionChain.send_keys(Keys.TAB)

# loop for pressing SPACE key until all followers are loaded
while (numberOfFollowersInList < totalfollowers):
    actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()        
    actionChain.send_keys(Keys.SPACE)
    time.sleep(2)
    numberOfFollowersInList = len(FList.find_elements_by_css_selector('li'))
    time.sleep(0.4)
    print("Loaded followers: " + str(numberOfFollowersInList))
    actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()            
    time.sleep(1)

# loop for printing followers
# change for saving in a file!

printed = 1
while (printed < totalfollowers):
    print(FList.find_element_by_xpath('(//div[@class="d7ByH"])[' + str(printed)+ ']').text)
    printed = printed + 1



browser.quit()