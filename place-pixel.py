from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
import pyautogui

# Reddit Credentials
username = "worker-1802149"
password = "<PASSWORD>"

# initialize the Chrome driver
# driver = webdriver.Safari()
driver = webdriver.Chrome()
# head to github login page
driver.get("https://www.reddit.com/login")
# find username/email field and send the username itself to the input field
driver.find_element("id", "loginUsername").send_keys(username)
# find password input field and insert password as well
driver.find_element("id", "loginPassword").send_keys(password)
# click login button
driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button").click()
# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")
time.sleep(3)    

# -----------------------------------r/place----------------------------------- #
driver.get("https://www.reddit.com/r/place/?screenmode=fullscreen&cx=-921&cy=836&px=8")
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] r/place failed")
else:
    print("[+] r/place successful")
time.sleep(4)    
# -----------------------------------r/place----------------------------------- #
driver.get("https://www.reddit.com/r/place/?screenmode=fullscreen&cx=-771&cy=302&px=8")
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] r/place failed")
else:
    print("[+] r/place successful")
time.sleep(4)    

# -----------------------------------Button place----------------------------------- #
pyautogui.click(623, 985)

error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")

if any(error_message in e.text for e in errors):
    print("[!] Button place failed")
else:
    print("[+] Button successful")
time.sleep(5)    
# -----------------------------------Button Color YELLOW----------------------------------- #
pyautogui.click(383, 911)

error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")

if any(error_message in e.text for e in errors):
    print("[!] YELLOW place failed")
else:
    print("[+] YELLOW successful")
time.sleep(2)    
# -----------------------------------Button Accept----------------------------------- #
pyautogui.click(759, 980)

error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")

if any(error_message in e.text for e in errors):
    print("[!] Accept place failed")
else:
    print("[+] Accept successful")
time.sleep(3)    
driver.close()
