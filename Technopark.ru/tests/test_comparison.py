

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import undetected_chromedriver as uc

from pages.catalog_pages import Catalog_page
from pages.laptop_pages import Laptop_page


def test_comparison_laptop():

    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # g = Service('D:\\Study\\Selenium\\chromedriver.exe')
    # driver = webdriver.Chrome(options=options, service=g)

    driver = uc.Chrome()
    driver.get('https://www.technopark.ru')

    print('Start Test')

    cp = Catalog_page(driver)
    cp.transition_to_laptop()

    lp = Laptop_page(driver)
    lp.comparison_laptop()

    driver.close()
    print('Finish Test')
