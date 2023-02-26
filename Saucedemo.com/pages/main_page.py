from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_product_backpack = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_bike = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_t_shot = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    burger_menu = "//button[@id='react-burger-menu-btn']"
    about_link = "//a[@id='about_sidebar_link']"

    # Getters

    def get_select_product_backpack(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_backpack)))

    def get_select_product_bike(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_bike)))

    def get_select_product_t_shot(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_t_shot)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu)))

    def get_about_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_link)))

    # Actions

    def click_select_product_backpack(self):
        self.get_select_product_backpack().click()
        print('Click select product Sauce Labs Backpack')

    def click_select_product_bike(self):
        self.get_select_product_bike().click()
        print('Click select product Sauce Labs Bike Light')

    def click_select_product_t_shot(self):
        self.get_select_product_t_shot().click()
        print('Click select product Sauce Labs Bolt T-Shirt')

    def click_cart(self):
        self.get_cart().click()
        print('Go to Cart')

    def click_burger_menu(self):
        self.get_burger_menu().click()
        print('Click to drop-down menu')

    def click_about_link(self):
        self.get_about_link().click()
        print('Go to about page')


    # Methods

    def select_product_1(self):
        self.get_current_url()
        self.click_select_product_backpack()
        self.click_cart()

    def select_product_2(self):
        self.get_current_url()
        self.click_select_product_bike()
        self.click_cart()

    def select_product_3(self):
        self.get_current_url()
        self.click_select_product_t_shot()
        self.click_cart()


    def select_menu_about(self):
        self.get_current_url()
        self.click_burger_menu()
        self.click_about_link()
        self.asser_url('https://saucelabs.com/')
        self.get_screenshot()
