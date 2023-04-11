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

driver.get('https://www.inmoment.com/websurvey/2/execute?_g=MTMxNjA%3DQ&_s=82c7fcc6-bd35-46bd-ba4e-8cb57db02c0a#!/1')


driver.implicitly_wait(60)

# accept cookies
clickable_cross = driver.find_element(By.XPATH, '//img[@alt="Remove"]')
clickable_cross.click()

# insert coupon code
for i in range(0, len(coupon_blocks)):
    couponField = driver.find_element(By.ID, COUPON_CSS + str(i))
    couponField.send_keys(coupon_blocks[i])

# wait for button to be clickable (goto next page)
driver.implicitly_wait(60)
button_nextPageLink = driver.find_element(By.ID, "nextPageLink")
button_nextPageLink.click()




# wait for 60 seconds unconditionally that the page loads or not
time.sleep(500)