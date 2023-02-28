import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('D:\\Programming\\pythonProject\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()


new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()
time.sleep(5)
future_date = datetime.datetime.today() - datetime.timedelta(days=10)
date = future_date.strftime('%m/%d/%Y')
print(date)

today = driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]")
today.click()
new_date.send_keys(Keys.BACKSPACE*10)
time.sleep(2)
new_date.send_keys(date)
new_date.click()
print('The test is completed')
