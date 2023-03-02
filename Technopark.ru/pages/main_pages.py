from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):
    url = 'https://www.technopark.ru'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators


    # Getters


    # Actions


    # Methods

    def open_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
