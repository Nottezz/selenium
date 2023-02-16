from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('D:\\Programming\\pythonProject\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

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
print('Click Login Button')

"""INFO Product 1"""

product = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product = product.text
print(value_product)

price_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_product_price = price_product.text
print(value_product_price)

select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product.click()
print('Select Product')

cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print('Enter Cart')

"""INFO Cart Product"""
cart_product = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product = cart_product.text
print(value_cart_product)
assert value_product == value_cart_product
print('Product correct ')

cart_price_product = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_product_price = cart_price_product.text
print(value_cart_product_price)
assert value_product_price == value_cart_product_price
print('Price correct')

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print('Select Button Checkout')

"""Select User INFO"""

first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Nikita')
print('Input First Name')

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Yakovlev')
print('Input Last Name')

zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip_code.send_keys('303-4043')
print('Input Zip Code')

botton_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
botton_continue.click()
print('Select CONTINUE button')

"""INFO Finish Product"""
finish_product = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product = finish_product.text
print(value_finish_product)
assert value_product == value_finish_product
print('Finish product correct ')

finish_price_product = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_product_price = finish_price_product.text
print(value_finish_product_price)
assert value_product_price == value_finish_product_price
print('Finish price correct')

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
value_summary_price = summary_price.text
print(value_summary_price)

item_total = 'Item total: ' + value_finish_product_price
print(item_total)
assert value_summary_price == item_total
print('Total summary price correct')

"""FINISH"""

finish = driver.find_element(By.XPATH, "//button[@id='finish']")
finish.click()
print('TEST COMPLETE')

