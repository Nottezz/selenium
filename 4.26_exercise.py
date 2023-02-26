import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


print(
    'Приветствую тебя в нашем интернет магазине!\nВыбери один из следующих товаров и укажи его номер:'
    '\n1 - Sauce Labs Backpack\n2 - Sauce Labs Bike Light\n3 - Sauce Labs Bolt T-Shirt\n4 - Sauce Labs Fleece Jacket\n'
    '5 - Sauce Labs Onesie\n6 - Test.allTheThings() T-Shirt (Red)'
)
product = input()
print(product)

time.sleep(2)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('D:\\Programming\\pythonProject\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

"""Log in"""

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('Input Login')

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('Input Password')

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('Click Login Button\n')

"""Select functions"""
def select_backpack():
    """Sauce Labs Backpack"""

    backpack = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
    value_product = backpack.text
    print(value_product)

    price_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
    value_product_price = price_product.text
    print(value_product_price)

    select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    select_product.click()
    print('Select Product')

    def cart_backpack():
        cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        cart.click()
        print('Enter Cart')

        product_cart = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
        value_product_cart = product_cart.text
        print('Item cart name: ' + value_product_cart)
        assert value_product == value_product_cart
        print('Item Cart name correct')

        price_cart = driver.find_element(By.XPATH,
                                         "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_cart = price_cart.text
        print('It`s cost : ' + value_price_cart)
        assert value_product_price == value_price_cart
        print('Item price correct')

    def checkout():
        """Go to Checkout"""

        checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout.click()
        print('Select Button Checkout\n')

        """Select User INFO"""

        first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
        first_name.send_keys('Carl')
        print('Input First Name')

        last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
        last_name.send_keys('Jonson')
        print('Input Last Name')

        zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        zip_code.send_keys('303-4043')
        print('Input Zip Code')

        botton_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
        botton_continue.click()
        print('Select CONTINUE button\n')

        """Comparison"""

        product_cart = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
        value_product_cart = product_cart.text
        print('Item cart name: ' + value_product_cart)
        assert value_product == value_product_cart
        print('Item Cart name correct')

        price_cart = driver.find_element(By.XPATH,
                                         "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_cart = price_cart.text
        print('It`s cost : ' + value_price_cart)
        assert value_product_price == value_price_cart
        print('Item price correct')

        summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
        value_summary_price = summary_price.text
        print(value_summary_price)

        item_total = 'Item total: ' + value_price_cart
        print(item_total)
        assert value_summary_price == item_total
        print('Total summary price correct')

    cart_backpack()
    checkout()


def select_bike():
    """Sauce Labs Bike Light"""

    labs_bike = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
    value_product = labs_bike.text
    print(value_product)

    price_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
    value_product_price = price_product.text
    print(value_product_price)

    select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
    select_product.click()
    print('Select Product')

    def cart_backpack():
        cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        cart.click()
        print('Enter Cart')

        product_cart = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
        value_product_cart = product_cart.text
        print('Item cart name: ' + value_product_cart)
        assert value_product == value_product_cart
        print('Item Cart name correct')

        price_cart = driver.find_element(By.XPATH,
                                         "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_cart = price_cart.text
        print('It`s cost : ' + value_price_cart)
        assert value_product_price == value_price_cart
        print('Item price correct')

    def checkout():
        """Go to Checkout"""

        checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout.click()
        print('Select Button Checkout\n')

        """Select User INFO"""

        first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
        first_name.send_keys('Carl')
        print('Input First Name')

        last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
        last_name.send_keys('Jonson')
        print('Input Last Name')

        zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        zip_code.send_keys('303-4043')
        print('Input Zip Code')

        botton_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
        botton_continue.click()
        print('Select CONTINUE button\n')

        """Comparison"""

        product_cart = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
        value_product_cart = product_cart.text
        print('Item cart name: ' + value_product_cart)
        assert value_product == value_product_cart
        print('Item Cart name correct')

        price_cart = driver.find_element(By.XPATH,
                                         "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_cart = price_cart.text
        print('It`s cost : ' + value_price_cart)
        assert value_product_price == value_price_cart
        print('Item price correct')

        summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
        value_summary_price = summary_price.text
        print(value_summary_price)

        item_total = 'Item total: ' + value_price_cart
        print(item_total)
        assert value_summary_price == item_total
        print('Total summary price correct')

    cart_backpack()
    checkout()


def select_labs():
    """Sauce Labs Bolt T-Shirt"""

    bolt_t_short = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
    value_product = bolt_t_short.text
    print(value_product)

    price_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
    value_product_price = price_product.text
    print(value_product_price)

    select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    select_product.click()
    print('Select Product')

    def cart_backpack():
        cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        cart.click()
        print('Enter Cart')

        product_cart = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
        value_product_cart = product_cart.text
        print('Item cart name: ' + value_product_cart)
        assert value_product == value_product_cart
        print('Item Cart name correct')

        price_cart = driver.find_element(By.XPATH,
                                         "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_cart = price_cart.text
        print('It`s cost : ' + value_price_cart)
        assert value_product_price == value_price_cart
        print('Item price correct')

    def checkout():
        """Go to Checkout"""

        checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout.click()
        print('Select Button Checkout\n')

        """Select User INFO"""

        first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
        first_name.send_keys('Carl')
        print('Input First Name')

        last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
        last_name.send_keys('Jonson')
        print('Input Last Name')

        zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        zip_code.send_keys('303-4043')
        print('Input Zip Code')

        botton_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
        botton_continue.click()
        print('Select CONTINUE button\n')

        """Comparison"""

        product_cart = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
        value_product_cart = product_cart.text
        print('Item cart name: ' + value_product_cart)
        assert value_product == value_product_cart
        print('Item Cart name correct')

        price_cart = driver.find_element(By.XPATH,
                                         "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_cart = price_cart.text
        print('It`s cost : ' + value_price_cart)
        assert value_product_price == value_price_cart
        print('Item price correct')

        summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
        value_summary_price = summary_price.text
        print(value_summary_price)

        item_total = 'Item total: ' + value_price_cart
        print(item_total)
        assert value_summary_price == item_total
        print('Total summary price correct')

    cart_backpack()
    checkout()


def select_fleece():
    """Sauce Labs Fleece Jacket"""

    fleece_jacket = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
    value_product = fleece_jacket.text
    print(value_product)

    price_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
    value_product_price = price_product.text
    print(value_product_price)

    select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    select_product.click()
    print('Select Product')

    def cart_backpack():
        cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        cart.click()
        print('Enter Cart')

        product_cart = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
        value_product_cart = product_cart.text
        print('Item cart name: ' + value_product_cart)
        assert value_product == value_product_cart
        print('Item Cart name correct')

        price_cart = driver.find_element(By.XPATH,
                                         "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_cart = price_cart.text
        print('It`s cost : ' + value_price_cart)
        assert value_product_price == value_price_cart
        print('Item price correct')

    def checkout():
        """Go to Checkout"""

        checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout.click()
        print('Select Button Checkout\n')

        """Select User INFO"""

        first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
        first_name.send_keys('Carl')
        print('Input First Name')

        last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
        last_name.send_keys('Jonson')
        print('Input Last Name')

        zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        zip_code.send_keys('303-4043')
        print('Input Zip Code')

        botton_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
        botton_continue.click()
        print('Select CONTINUE button\n')

        """Comparison"""

        product_cart = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
        value_product_cart = product_cart.text
        print('Item cart name: ' + value_product_cart)
        assert value_product == value_product_cart
        print('Item Cart name correct')

        price_cart = driver.find_element(By.XPATH,
                                         "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_cart = price_cart.text
        print('It`s cost : ' + value_price_cart)
        assert value_product_price == value_price_cart
        print('Item price correct')

        summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
        value_summary_price = summary_price.text
        print(value_summary_price)

        item_total = 'Item total: ' + value_price_cart
        print(item_total)
        assert value_summary_price == item_total
        print('Total summary price correct')

    cart_backpack()
    checkout()


def select_onesie():
    """Sauce Labs Onesie"""

    labs_onesie = driver.find_element(By.XPATH, "//a[@id='item_2_title_link']")
    value_product = labs_onesie.text
    print(value_product)

    price_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div")
    value_product_price = price_product.text
    print(value_product_price)

    select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
    select_product.click()
    print('Select Product')

    def cart_backpack():
        cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        cart.click()
        print('Enter Cart')

        product_cart = driver.find_element(By.XPATH, "//a[@id='item_2_title_link']")
        value_product_cart = product_cart.text
        print('Item cart name: ' + value_product_cart)
        assert value_product == value_product_cart
        print('Item Cart name correct')

        price_cart = driver.find_element(By.XPATH,
                                         "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_cart = price_cart.text
        print('It`s cost : ' + value_price_cart)
        assert value_product_price == value_price_cart
        print('Item price correct')

    def checkout():
        """Go to Checkout"""

        checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout.click()
        print('Select Button Checkout\n')

        """Select User INFO"""

        first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
        first_name.send_keys('Carl')
        print('Input First Name')

        last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
        last_name.send_keys('Jonson')
        print('Input Last Name')

        zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        zip_code.send_keys('303-4043')
        print('Input Zip Code')

        botton_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
        botton_continue.click()
        print('Select CONTINUE button\n')

        """Comparison"""

        product_cart = driver.find_element(By.XPATH, "//a[@id='item_2_title_link']")
        value_product_cart = product_cart.text
        print('Item cart name: ' + value_product_cart)
        assert value_product == value_product_cart
        print('Item Cart name correct')

        price_cart = driver.find_element(By.XPATH,
                                         "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_cart = price_cart.text
        print('It`s cost : ' + value_price_cart)
        assert value_product_price == value_price_cart
        print('Item price correct')

        summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
        value_summary_price = summary_price.text
        print(value_summary_price)

        item_total = 'Item total: ' + value_price_cart
        print(item_total)
        assert value_summary_price == item_total
        print('Total summary price correct')

    cart_backpack()
    checkout()


def select_allthethings():
    """Test.allTheThings() T-Shirt (Red)"""

    allthethings_t_shirt = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
    value_product = allthethings_t_shirt.text
    print(value_product)

    price_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div")
    value_product_price = price_product.text
    print(value_product_price)

    select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    select_product.click()
    print('Select Product')

    def cart_backpack():
        cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        cart.click()
        print('Enter Cart')

        product_cart = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
        value_product_cart = product_cart.text
        print('Item cart name: ' + value_product_cart)
        assert value_product == value_product_cart
        print('Item Cart name correct')

        price_cart = driver.find_element(By.XPATH,
                                         "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_cart = price_cart.text
        print('It`s cost : ' + value_price_cart)
        assert value_product_price == value_price_cart
        print('Item price correct')

    def checkout():
        """Go to Checkout"""

        checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout.click()
        print('Select Button Checkout\n')

        """Select User INFO"""

        first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
        first_name.send_keys('Carl')
        print('Input First Name')

        last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
        last_name.send_keys('Jonson')
        print('Input Last Name')

        zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        zip_code.send_keys('303-4043')
        print('Input Zip Code')

        botton_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
        botton_continue.click()
        print('Select CONTINUE button\n')

        """Comparison"""

        product_cart = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
        value_product_cart = product_cart.text
        print('Item cart name: ' + value_product_cart)
        assert value_product == value_product_cart
        print('Item Cart name correct')

        price_cart = driver.find_element(By.XPATH,
                                         "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_cart = price_cart.text
        print('It`s cost : ' + value_price_cart)
        assert value_product_price == value_price_cart
        print('Item price correct')

        summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
        value_summary_price = summary_price.text
        print(value_summary_price)

        item_total = 'Item total: ' + value_price_cart
        print(item_total)
        assert value_summary_price == item_total
        print('Total summary price correct')

    cart_backpack()
    checkout()


"""Smoke Test"""
if product == '1':
    select_backpack()
    finish = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish.click()
    print('TEST COMPLETE')
elif product == '2':
    select_bike()
    finish = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish.click()
    print('TEST COMPLETE')
elif product == '3':
    select_labs()
    finish = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish.click()
    print('TEST COMPLETE')
elif product == '4':
    select_fleece()
    finish = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish.click()
    print('TEST COMPLETE')
elif product == '5':
    select_onesie()
    finish = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish.click()
    print('TEST COMPLETE')
elif product == '6':
    select_allthethings()
    finish = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish.click()
    print('TEST COMPLETE')
else:
    print('Неизвестная команда')