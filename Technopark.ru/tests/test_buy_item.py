
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import undetected_chromedriver as uc

from pages.main_pages import Main_page
from pages.catalog_pages import Catalog_page
from pages.smartphone_pages import Smartphone_page
from pages.laptop_pages import Laptop_page
from pages.cart_pages import Cart_page


def test_buy_smartphone():

    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # g = Service('D:\\Сhrome_driver\\chromedriver.exe')
    # driver = webdriver.Chrome(options=options, service=g)

    driver = uc.Chrome()
    driver.get('https://www.technopark.ru')

    print('Start Test')

    mp = Main_page(driver)
    # mp.open_page()


    cp = Catalog_page(driver)
    cp.transition_to_phone()

    sp = Smartphone_page(driver)
    sp.choosing_smartphone_1()

    cr = Cart_page(driver)
    cr.cart_smartphone()

    # driver.close()
    print('Finish Test')


def test_byu_laptop():

    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # g = Service('D:\\Сhrome_driver\\chromedriver.exe')
    # driver = webdriver.Chrome(options=options, service=g)

    driver = uc.Chrome()
    driver.get('https://www.technopark.ru')

    print('Start Test')

    mp = Main_page(driver)
    # mp.open_page()

    cp = Catalog_page(driver)
    cp.transition_to_laptop()

    lp = Laptop_page(driver)
    lp.buy_laptop()

    cr = Cart_page(driver)
    cr.cart_laptop()

    print('Finish Test')
