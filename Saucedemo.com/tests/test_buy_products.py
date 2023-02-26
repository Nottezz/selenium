import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page

@pytest.mark.run(order=3)
def test_buy_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\\Study\\Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('Start Test 1')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_1()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    time.sleep(5)
    print('Finish Test 1')
    driver.quit()


@pytest.mark.run(order=1)
def test_buy_product_2():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\\Study\\Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('Start Test 2')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_2()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    time.sleep(5)
    print('Finish Test 2')
    driver.quit()

@pytest.mark.run(order=2)
def test_buy_product_3():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\\Study\\Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('Start Test 3')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_3()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    time.sleep(5)
    print('Finish Test 3')
    driver.quit()
