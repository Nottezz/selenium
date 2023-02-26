import pytest


@pytest.fixture()
def set_up():
    print('\nStart Test')
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # g = Service('D:\\Study\\Selenium\\chromedriver.exe')
    # driver = webdriver.Chrome(options=options, service=g)
    # url = 'https://www.saucedemo.com/'
    # self.driver.get(self.url)
    # self.driver.maximize_window()

    yield

    # driver.quit()
    print('\nFinish Test')


@pytest.fixture(scope='module')
def set_group():
    print('Enter system')
    yield
    print('Exit system')
