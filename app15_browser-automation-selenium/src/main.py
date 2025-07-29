from os import getenv
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
MY_USERNAME = getenv("USERNAME")
MY_PASSWORD = getenv("PASSWORD")

# Driver, options and service
options = Options()
options.binary_location = "/usr/bin/librewolf"
options.add_argument("--disable-search-engine-choice-screen")

service = Service("./geckodriver")
driver = webdriver.Firefox(service=service, options=options)
driver.get("https://demoqa.com/login")

# Locate username, password and login button
usrname_field = WebDriverWait(driver, 10).until \
    (EC.visibility_of_element_located((By.ID, 'userName')))

psswd_field = WebDriverWait(driver, 10).until \
    (EC.visibility_of_element_located((By.ID, 'password')))

login_button = driver.find_element(By.ID, 'login')

# Fill in username and password
usrname_field.send_keys(MY_USERNAME)
psswd_field.send_keys(MY_PASSWORD)
driver.execute_script("arguments[0].click();", login_button)


input("Press enter to close the browser")
driver.quit()
