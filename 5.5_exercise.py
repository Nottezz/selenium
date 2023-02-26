import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('D:\\Study\\Selenium\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_password = 'secret_sauce'


def standart_user():
    login = 'standard_user'

    user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
    user_name.send_keys(login)
    print('Input Login')

    password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
    password.send_keys(login_password)
    print('Input Password')

    button_login = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
    button_login.click()
    print('Click Login Button')


def locked_out_user():
    login = 'locked_out_user'

    user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
    user_name.send_keys(login)
    print('Input Login')

    password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
    password.send_keys(login_password)
    print('Input Password')

    button_login = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
    button_login.click()
    print('Click Login Button')


def problem_user():
    login = 'problem_user'

    user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
    user_name.send_keys(login)
    print('Input Login')

    password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
    password.send_keys(login_password)
    print('Input Password')

    button_login = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
    button_login.click()
    print('Click Login Button')


def performance_glitch_user():
    login = 'performance_glitch_user'

    user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
    user_name.send_keys(login)
    print('Input Login')

    password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
    password.send_keys(login_password)
    print('Input Password')

    button_login = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
    button_login.click()
    print('Click Login Button')


print('Start Test - Standart user')
standart_user()
text_products = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
value_text_products = text_products.text
assert value_text_products == 'PRODUCTS'
print('Test success!\n')

menu = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
menu.click()
print('Click Menu Button\n')
log_out = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
log_out.click()
time.sleep(3)

print('Start Test - Locked out user')
locked_out_user()
text_error = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//h3[@data-test='error']")))
value_text_error = text_error.text
assert value_text_error == 'Epic sadface: Sorry, this user has been locked out.'
print('Test success!\n')

driver.refresh()
time.sleep(3)

print('Start Test - Problem_user')
problem_user()
text_products = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
value_text_products = text_products.text
assert value_text_products == 'PRODUCTS'
print('Test success!\n')

menu = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
menu.click()
print('Click Menu Button\n')
log_out = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
log_out.click()
time.sleep(3)

print('Start Test - Performance glitch user')
performance_glitch_user()
text_products = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
value_text_products = text_products.text
assert value_text_products == 'PRODUCTS'
print('Test success!\n')

driver.close()
print('All users checked')