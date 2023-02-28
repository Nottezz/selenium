import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.laptop_pages import Laptop_page

def test_copparison_laptop():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\\Study\\Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('Start Test')

    lp = Laptop_page(driver)
    lp.comparison_laptop()

    driver.close()
    print('Finish Test')
