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
print('Click Login Button\n')

"""INFO Product 1"""

product_t_shot = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
t_shot_value_product = product_t_shot.text
print('Selected T-shot: ' + t_shot_value_product)

t_shot_price_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
t_shot_value_product_price = t_shot_price_product.text
print('It`s cost : ' + t_shot_value_product_price)

select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
select_product.click()
print('Select Product\n')

"""INFO Product 2"""

jacket_product = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
jacket_value_product = jacket_product.text
print('Selected Jacket: ' + jacket_value_product)

jacket_price_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
jacket_value_product_price = jacket_price_product.text
print('It`s cost: ' + jacket_value_product_price)

select_product = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
select_product.click()
print('Select Product\n')

"""Check cart info"""

cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print('Enter Cart')

product_t_shot_cart = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
t_shot_value_product_cart = product_t_shot_cart.text
print('T-shot cart name: ' + t_shot_value_product_cart)
assert t_shot_value_product == t_shot_value_product_cart
print('T-Shot Cart name correct')

t_shot_price_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
t_shot_value_price_cart = t_shot_price_cart.text
print('It`s cost : ' + t_shot_value_price_cart)
assert t_shot_value_product_price == t_shot_value_price_cart
print('T-Shot price correct')

jacket_product_cart = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
jacket_value_product_cart = jacket_product_cart.text
print('Selected Jacket: ' + jacket_value_product_cart)
assert jacket_value_product == jacket_value_product_cart
print('Jacket Cart name correct')

jacket_price_product_cart = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
jacket_value_price_cart = jacket_price_product_cart.text
print('It`s cost: ' + jacket_value_price_cart)
assert jacket_value_product_price == jacket_value_price_cart
print('Jacket price correct\n')

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

"""INFO Finish Product T-Shot"""
t_shot_finish_product = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
t_shot_value_finish_product = t_shot_finish_product.text
print(t_shot_value_finish_product)
assert t_shot_value_product == t_shot_value_finish_product
print('Finish name product correct ')

t_shot_finish_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
t_shot_value_finish_price = t_shot_finish_price.text
print(t_shot_value_finish_price)
assert t_shot_value_product_price == t_shot_value_finish_price
print('Finish price T-shot correct')

"""INFO Finish Product Jacket"""

jacket_finish_product = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
jacket_value_finish = jacket_finish_product.text
print(jacket_value_finish)
assert jacket_value_product == jacket_value_finish
print('Finish product correct ')

jacket_finish_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
jacket_value_finish_price = jacket_finish_price.text
print(jacket_value_finish_price)
assert jacket_value_product_price == jacket_value_finish_price
print('Finish price correct\n')

"""Summ Items"""

t_shots = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
jacket = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")

t_shots_price = t_shots.text
jacket_price = jacket.text
t_shots_res_str = float(t_shots_price.replace('$', ''))
jacket_res_str = float(jacket_price.replace('$', ''))

price = t_shots_res_str + jacket_res_str
print('Total amount: ' + str(price))

"""Summary price"""

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
value_summary_price = summary_price.text
print('\n' + value_summary_price)

item_total = 'Item total: $' + str(price)
print(item_total)
assert value_summary_price == item_total
print('Total summary price correct\n')

"""FINISH"""

finish = driver.find_element(By.XPATH, "//button[@id='finish']")
finish.click()
print('TEST COMPLETE')

