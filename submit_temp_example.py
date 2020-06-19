'''
Use of selenium to submit your temperature automatically for 100% compliance

You obviously need to do your own testing and change your variables and also work location.
Now it is only set for CCF Expo
'''


import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import os

'''
SET YOUR DETAILS HERE
'''
NRIC = 'S1234567Z'  # TODO KEY YOUR IC HERE
EMAIL = 'example@example.com'  # TODO KEY YOUR EMAIL HERE
WORKDAY = [0,1,3,4] # TODO Key your workdays, Mon = 0, Tues = 1 and so on... sun = 6

'''
Start Selenium settings
'''

options = Options()
options.headless = True  # TODO you can set this to False, to see the outcome before submission

cwd = os.getcwd()
driverpath = os.path.join(cwd, "chromedriver.exe")

driver = webdriver.Chrome(driverpath, options=options, port=8080)
driver.get("https://form.gov.sg/#!/5e37870c73a1e90011942e50")

# create a function to key value in the element by id
def key_value_into_element_by_id(id, value):
    elem = driver.find_element_by_id(id)
    elem.send_keys(value)

#scroll
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(1)
# Key in the form
key_value_into_element_by_id('5e353dd16509040011d0333a', NRIC)
temp_today = str((random.randint(360, 374))/10)
key_value_into_element_by_id('5e3541216509040011d0338b', temp_today)

# duty
driver.find_element(By.XPATH, '//*[@id="5e353ed27146b10011d4b660"]/div[1]/input').click()
day = datetime.datetime.today().weekday()
if day in WORKDAY:
    driver.find_element(By.XPATH, '//*[@id="5e353ed27146b10011d4b660"]/div[2]/div/div/div[2]/div').click() # on duty
else:
    driver.find_element(By.XPATH, '//*[@id="5e353ed27146b10011d4b660"]/div[2]/div/div/div[3]/div').click() # off duty

#location
driver.find_element(By.XPATH, '//*[@id="5e3542a35cff5300119a8ec6"]/div[1]/input').click()
active_ele = driver.switch_to.active_element
active_ele.send_keys("CCF")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="5e3542a35cff5300119a8ec6"]/div[2]/div/div/div[2]/div').click()

key_value_into_element_by_id('5e9c3467d273ec0011e23a94', EMAIL)

#submit
driver.find_element(By.XPATH, '//*[@id="form-submit"]/div/button').click()  # TODO you can comment this out to see the outcome before submission

#end
driver.quit()

