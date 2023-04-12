import os
import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] += r':/usr/local/bin'
driver = webdriver.Chrome()

COUPON_CODE = "041023_155007_6268_10019"
COUPON_CSS = "promptInput_397048_"
coupon_blocks = COUPON_CODE.split("_")
EMAIL = "user@hotmail.com"
PHONE = "1234567890"
SHORT_WAIT = 1
MEDIUM_WAIT = 4
LONG_WAIT = 60

print("getting the page")
driver.get('https://www.storeopinion.ca')

print("wait for 60 seconds implicitly")
#wait for 60 seconds implicitly
driver.implicitly_wait(LONG_WAIT) 

print("accept cookies")
# accept cookies
clickable_cross = driver.find_element(By.XPATH, '//img[@alt="Remove"]')
clickable_cross.click()

print("entering the coupon code")
for i in range(0, len(coupon_blocks)):
    couponField = driver.find_element(By.ID, COUPON_CSS + str(i))
    couponField.send_keys(coupon_blocks[i])
    time.sleep(SHORT_WAIT)

print("clicking on the next button coupon")
button_nextPageLink = driver.find_element(By.ID, "nextPageLink")
button_nextPageLink.click()

print("wait for 60 seconds implicitly")
#wait for the button to be clickable
driver.implicitly_wait(LONG_WAIT)

WebDriverWait(driver, MEDIUM_WAIT).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Yes"]')))
print("clicking on the yes button")
clickable_yes = driver.find_element(By.XPATH, '//*[text()="Yes"]')
clickable_yes.click()
time.sleep(MEDIUM_WAIT)
print("clicking on the next button age")
clickable_next = driver.find_element(By.ID, "nextPageLink")
clickable_next.click()

print("Purchase Location")
#wait for the button to be clickable
driver.implicitly_wait(LONG_WAIT)

# click on the first radio option
clickable_radio = driver.find_element(By.XPATH, '//*[text()="Shop in the store"]')
clickable_radio.click()
time.sleep(SHORT_WAIT)
print("clicking on the next button Shopping in the store")
clickable_next = driver.find_element(By.ID, "nextPageLink")
clickable_next.click()

print("Type of Purchase")
#wait for the button to be clickable
driver.implicitly_wait(LONG_WAIT)

# click on the first radio option
clickable_radio = driver.find_element(By.XPATH, '//*[text()="use self-checkout for your purchase?"]')
clickable_radio.click()
time.sleep(SHORT_WAIT)
print("clicking on the next button self-checkout")
clickable_next = driver.find_element(By.ID, "nextPageLink")
clickable_next.click()

print("XP Grade")
#wait for the button to be clickable
driver.implicitly_wait(LONG_WAIT)

# click on the first radio option
clickable_radio = driver.find_element(By.XPATH, '//*[text()="10"]')
clickable_radio.click()
time.sleep(SHORT_WAIT)
print("clicking on the next button XP Grade")
clickable_next = driver.find_element(By.ID, "nextPageLink")
clickable_next.click()

print("Overall Satisfaction")
#wait for the button to be clickable
driver.implicitly_wait(LONG_WAIT)

# click on the first radio option
clickable_radio = driver.find_element(By.XPATH, '//*[text()="5"]')
clickable_radio.click()
# time.sleep(SHORT_WAIT)
# print("clicking on the next button Overall Satisfaction")
# clickable_next = driver.find_element(By.ID, "nextPageLink")
# clickable_next.click()



# wait for 60 seconds unconditionally that the page loads or not
time.sleep(500)