from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebDriverSetup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(5)
    driver.maximize_window()