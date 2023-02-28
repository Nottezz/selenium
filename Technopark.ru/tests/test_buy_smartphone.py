import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.smartphone_pages import Smartphone_page

def test_buy_smartphone():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\\Study\\Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('Start Test')

    sp = Smartphone_page(driver)
    sp.choosing_smartphone()

    driver.close()
    print('Finish Test')
