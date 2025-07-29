from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = "/usr/bin/librewolf"

service = Service("./geckodriver")
driver = webdriver.Firefox(service=service, options=options)
driver.get("https://demoqa.com/login")

input("Press enter to close the browser")
driver.quit()
