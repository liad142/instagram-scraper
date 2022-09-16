import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from instagram_users import names
print(names)

s = Service("C:\\Users\\liad\\PycharmProjects\\pythonProject\\chromedriver.exe")
browser = webdriver.Chrome(service=s)

browser.get('https://www.instagram.com/')
sleep(3)

#get username and password input
username_input_login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username_input_login.clear()
password.clear()

#send values to the inputs
username_input_login.send_keys("liadiuos")
password.send_keys("liad123456")

#press log in button
log_in = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
#press not now buttons
not_now = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()


for name in names:
    # catching search input
    search_input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    search_input.clear()
    time.sleep(1)
    search_input.send_keys(name)

    count = 0
    while count < 3:
        search_input.send_keys(Keys.ENTER)
        count += 1
        time.sleep(1)

    insta_data = []

    #get username
    profile_username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//h2[contains(text(),'')]"))).text

    #get posts number
    posts = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//header/section[1]/ul[1]/li[1]/div[1]"))).text

    #get followers number
    followers = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//header/section[1]/ul[1]/li[2]/a[1]/div[1]"))).text

    #get following number
    following = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//header/section[1]/ul[1]/li[3]/a[1]/div[1]"))).text

    print(profile_username, posts, followers, following)

    insta_data.append((profile_username, posts, followers, following))

    df = pd.DataFrame(insta_data, columns=['User Name', 'Total Posts', 'Followers Number', 'Following Number'])
    df.to_csv(r"C:\Users\liad\Desktop\save csv\test2.csv")
