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


class WebAutomation:
    def __init__(self):
        options = Options()
        options.binary_location = "/usr/bin/librewolf"
        options.add_argument("--disable-search-engine-choice-screen")
        # options.set_preference("browser.download.folderList", 2)
        # options.set_preference("browser.download.dir", "./downloads/")
        # options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        # options.set_preference("pdfjs.disabled", True)

        service = Service("./geckodriver")
        self.driver = webdriver.Firefox(service=service, options=options)

    def login(self, username, password):
        self.driver.get("https://demoqa.com/login")
        # Locate username, password and login button
        usrname_field = WebDriverWait(self.driver, 10).until \
        (EC.visibility_of_element_located((By.ID, 'userName')))

        psswd_field = WebDriverWait(self.driver, 10).until \
        (EC.visibility_of_element_located((By.ID, 'password')))

        login_button = self.driver.find_element(By.ID, 'login')

        # Fill in username and password
        usrname_field.send_keys(username)
        psswd_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Locate the elements dropdown
        elements = WebDriverWait(self.driver, 10).until \
            (EC.visibility_of_element_located((By.XPATH, 
            '/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()

        text_box = WebDriverWait(self.driver, 10).until \
            (EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Locate the form fields and submit button
        fullname_field = WebDriverWait(self.driver, 10).until \
        (EC.visibility_of_element_located((By.ID, 'userName')))
        
        email_field = WebDriverWait(self.driver, 10).until \
        (EC.visibility_of_element_located((By.ID, 'userEmail')))
        
        current_adress_field = WebDriverWait(self.driver, 10).until \
        (EC.visibility_of_element_located((By.ID, 'currentAddress')))
        
        permanent_adress_field = WebDriverWait(self.driver, 10).until \
        (EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_adress_field.send_keys(current_address)
        permanent_adress_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # Locate the upload and download section and the downlaod button
        upload_download = WebDriverWait(self.driver, 10).until \
            (EC.visibility_of_element_located((By.ID, 'item-7')))
        upload_download.click()
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    web_automation = WebAutomation()
    web_automation.login(MY_USERNAME, MY_PASSWORD)
    web_automation.fill_form("John Smith", "john@gmail.com", 
                             "John Street 100", "John Street 100")
    web_automation.download()
    web_automation.close()
