from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Smartphone_page(Base):
    url = 'https://www.technopark.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog = "//button[@class='header-catalog-button header-catalog__btn']"
    catalog_smartphone = "//a[@data-id='6209']"
    smartphone = "//a[@to='/smartfony/']"
    filter_only_available = "//*[@id='__layout']/div/div[2]/div/div[1]/div/aside/div/div/div/div[2]/div[2]/div[2]/div/div[1]/label/span[2]"  # Только в наличие
    filter_from = "//*[@id='__layout']/div/div[2]/div/div[1]/div/aside/div/div/div/div[2]/div[4]/div[1]/div[2]/div[1]/input"  # Цена от
    filter_before = "//*[@id='__layout']/div/div[2]/div/div[1]/div/aside/div/div/div/div[2]/div[4]/div[1]/div[2]/div[2]/input"  # Цена до
    filter_memory = "//*[@id='__layout']/div/div[2]/div/div[1]/div/aside/div/div/div/div[2]/div[12]"  # Открыть Встроенную память
    filter_memory_box = "//*[@id='__layout']/div/div[2]/div/div[1]/div/aside/div/div/div/div[2]/div[12]/div[2]/div/div[2]/label/span[2]"  # Выбираем 256 гб
    filter_battery = "//*[@id='__layout']/div/div[2]/div/div[1]/div/aside/div/div/div/div[2]/div[21]/div[1]/div/div"  # Открыть Ёмкость аккумулятора
    filter_battery_box = "//*[@id='__layout']/div/div[2]/div/div[1]/div/aside/div/div/div/div[2]/div[21]/div[2]/div/div[1]/label/span[2]"  # Выбираем от 5000 мАч ёмкость
    button_items = "//*[@id='__layout']/div/div[2]/div/div[1]/div/aside/div/div/div/div[1]/button[1]"  # Кнопка показать товар
    phone = "//a[@title='Смартфон Samsung Galaxy M53 5G 256 ГБ зелёный']"  # Выбор самого телефона

    button_cart = "//button[@data-test-id='add-to-cart-button']"
    button_shopping_cart = "//a[@data-test-id='upsale-to-cart']"
    phone_code = "//a[@class='checkout-cart-product-item__title']"

    # Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_catalog_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_smartphone)))

    def get_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphone)))

    def get_filter_only_available(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_only_available)))

    def get_filter_from(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_from)))

    def get_filter_before(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_before)))

    def get_filter_memory(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_memory)))

    def get_filter_memory_box(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_memory_box)))

    def get_filter_battery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_battery)))

    def get_filter_battery_box(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_battery_box)))

    def get_button_items(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_items)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_shopping_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_shopping_cart)))

    def get_phone_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_code)))

    # Actions

    def click_catalog(self):
        self.get_catalog().click()
        print('Click to Catalog')

    def click_catalog_smartphone(self):
        self.get_catalog_smartphone().click()
        print('Click to Catalog again')

    def click_smartphone(self):
        self.get_smartphone().click()
        print('Open catalog with smartphone')

    def click_filter_only_availableg(self):
        self.get_filter_only_available().click()
        print('Click to available only filter')

    def click_filter_from(self):
        self.get_filter_from().click()
        print('Click to price from filter')

    def clear_filet_from(self):
        self.get_filter_from().send_keys(Keys.BACKSPACE * 10)
        print('Clear filter price FROM')

    def input_filter_from(self, from_price):
        self.get_filter_from().send_keys(from_price)
        print('Input price from')

    def click_filter_before(self):
        self.get_filter_before().click()
        print('Click to price before filter')

    def clear_filet_before(self):
        self.get_filter_before().send_keys(Keys.BACKSPACE * 10)
        print('Clear filter price BEFORE')

    def input_filter_before(self, before_price):
        self.get_filter_before().send_keys(before_price)
        print('Input price before')

    def click_filter_memory(self):
        self.get_filter_memory().click()
        print('Click to memory filter')

    def click_filter_memory_box(self):
        self.get_filter_memory_box().click()
        print('Choosing memory')

    def click_filter_battery(self):
        self.get_filter_battery().click()
        print('Click to battery filter')

    def click_filter_battery_box(self):
        self.get_filter_battery_box().click()
        print('Choosing battery')

    def click_button_items(self):
        self.get_button_items().click()
        print('Looking at the selected list')

    def click_phone(self):
        self.get_phone().click()
        print('Choosing smartphone')

    def click_button_cart(self):
        self.get_button_cart().click()
        print('Click to button cart')

    def click_shopping_cart(self):
        self.get_shopping_cart().click()
        print('Go to cart')

    # Methods

    def choosing_smartphone(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_catalog()
        self.click_catalog_smartphone()
        self.click_smartphone()
        self.click_filter_only_availableg()
        self.driver.execute_script('window.scrollTo(0,700)')
        self.click_filter_from()
        self.clear_filet_from()
        self.input_filter_from(20000)
        self.click_filter_before()
        self.clear_filet_before()
        self.input_filter_before(80000)
        self.click_filter_memory()
        self.click_filter_memory_box()
        self.click_filter_battery()
        self.click_filter_battery_box()
        self.click_button_items()
        self.click_phone()
        self.click_button_cart()
        self.click_shopping_cart()
        self.assert_word(self.get_phone_code().text, 'Samsung Galaxy M53 5G 256 ГБ зелёный')
        self.get_screenshot()
