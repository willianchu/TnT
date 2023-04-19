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
SHORT_WAIT = 2
MEDIUM_WAIT = 4
LONG_WAIT = 6

def next_page():
    time.sleep(SHORT_WAIT)
    print("clicking on the next page button >>>")
    button_nextPageLink = driver.find_element(By.ID, "nextPageLink")
    button_nextPageLink.click()

def wait_page_load():
    print("wait for the page to load")
    time.sleep(LONG_WAIT)

def find_and_click(xpath):
    clickable = driver.find_element(By.XPATH, xpath)
    clickable.click()

print("getting the page")
driver.get('https://www.storeopinion.ca')

time.sleep(SHORT_WAIT) # ajustment for the page to load

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



WebDriverWait(driver, MEDIUM_WAIT).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Yes"]')))
print("clicking on the yes button")
clickable_yes = driver.find_element(By.XPATH, '//*[text()="Yes"]')
clickable_yes.click()

next_page()


print("Purchase Location")
wait_page_load()
# click on the first radio option
clickable_radio = driver.find_element(By.XPATH, '//*[text()="Shop in the store"]')
clickable_radio.click()
next_page()

print("Type of Purchase")

# click on the first radio option
clickable_radio = driver.find_element(By.XPATH, '//*[text()="use self-checkout for your purchase?"]')
clickable_radio.click()
next_page()

print("XP Grade")

# click on the first radio option
clickable_radio = driver.find_element(By.XPATH, '//*[text()="10"]')
clickable_radio.click()
next_page()

print("Overall Satisfaction")

click_on_5 = driver.find_element(By.XPATH, '//*[text()="5"]')
click_on_5.click()

time.sleep(SHORT_WAIT)
# search textarea#commentArea_441261
search_by_id = driver.find_element(By.ID, "commentArea_441261")
search_by_id.send_keys("I love the imported products, quality and freshness of the products. It is great to have food ready to take out and eat. I feel inspired to cook and learn more about asian food.")

next_page()

find_and_click('//*[text()="Yes, continue with the survey for entry into the draw!"]')
next_page()

wait_page_load()
find_and_click('//*[text()="To buy a specific item or product"]')
next_page()

find_child_from_parent = driver.find_element(By.XPATH, '//label[@for="option_827008_373202"]').find_element(By.XPATH, './/*[@aria-label="Neither Agree nor Disagree"]')
find_child_from_parent.click()

find_child_from_parent = driver.find_element(By.XPATH, '//label[@for="option_827014_373203"]').find_element(By.XPATH, './/*[@aria-label="Neither Agree nor Disagree"]')
find_child_from_parent.click()


# wait for 60 seconds unconditionally that the page loads or not
time.sleep(500)