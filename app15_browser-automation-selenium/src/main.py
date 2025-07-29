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
# options.set_preference("browser.download.folderList", 2)
# options.set_preference("browser.download.dir", "./downloads/")
# options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
# options.set_preference("pdfjs.disabled", True)

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


# Locate the elements dropdown
elements = WebDriverWait(driver, 10).until \
    (EC.visibility_of_element_located((By.XPATH, 
    '/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()

text_box = WebDriverWait(driver, 10).until \
    (EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()


# Locate the form fields and submit button
fullname_field = WebDriverWait(driver, 10).until \
    (EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until \
    (EC.visibility_of_element_located((By.ID, 'userEmail')))
current_adress_field = WebDriverWait(driver, 10).until \
    (EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_adress_field = WebDriverWait(driver, 10).until \
    (EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')


# Fill in the form fields
fullname_field.send_keys("John Smith")
email_field.send_keys("john@gmail.com")
current_adress_field.send_keys("John Street 100")
permanent_adress_field.send_keys("John Stree 100")
driver.execute_script("arguments[0].click();", submit_button)


# Locate the upload and download section and the downlaod button
upload_download = WebDriverWait(driver, 10).until \
    (EC.visibility_of_element_located((By.ID, 'item-7')))
upload_download.click()
download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button)


input("Press enter to close the browser")
driver.quit()
