from selenium import webdriver
import time

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("user-data-dir=/home/petry/.config/chromium/Default")

browser = webdriver.Chrome(options=chrome_opt)

browser.get("https://www.instagram.com/neymarjr")

#xpath to the div where the bio is
userbio = browser.find_element_by_xpath('//div[@class="-vDIg"]')

print(userbio.text)

browser.quit()
