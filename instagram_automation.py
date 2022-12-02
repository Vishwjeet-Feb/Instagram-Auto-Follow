# Read This Before Run
# In Line 21 Please enter your username in " ".
# In Line 25 Please enter your Password in " ".
# In line 49 Please enter a numerical value to loop please remeber it is numerical value without " ".

# Import All Library for Instagram Auto Follower
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By

# Object instansation
browser =  webdriver.Chrome()

# Open URL Instagram
browser.get("https://www.instagram.com")  

#wait for 3 sec to fully load the page
time.sleep (3)


#identify user field and send username
username_input = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys("Enter Your User Name Here")
#identify password field and send password
password_input = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys("Enter Your Password Here")

#find and click submit
login_button = browser.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep (3)


# click on notNow button 
notNowButton = WebDriverWait(browser, 15).until(
    lambda d: d.find_element(By.XPATH,'//button[text()="Not Now"]'))
notNowButton.click()

# click on NotNow Notification button 
NotificationNotNow = WebDriverWait(browser, 15).until(
    lambda d: d.find_element(By.XPATH,'//button[text()="Not Now"]'))
NotificationNotNow.click()
time.sleep (3)

# See all
seeall = browser.find_element(By.XPATH, '//div[text()="See All"]').click()
time.sleep (3)

#loop
for i in range ("enter How Much People you want to Follow"):
    browser.find_element(By.XPATH, '//div[text()="Follow"]').click()
    time.sleep (3)
    browser.refresh()
    time.sleep (7)