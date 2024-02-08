import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators
import data

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def log_in(driver):
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.MAIN_BUTTON_LOGIN))
    driver.find_element(*TestLocators.MAIN_BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM_TITLE))
    driver.find_element(*TestLocators.AUTH_FORM_INPUT_EMAIL).send_keys(data.user_email)
    driver.find_element(*TestLocators.AUTH_FORM_INPUT_PASSWORD).send_keys(data.user_password)
    driver.find_element(*TestLocators.AUTH_FORM_BUTTON).click()

@pytest.fixture
def open_personal_account(driver, log_in):
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.HEADER_BUTTON_PERSONAL_ACCOUNT))
    driver.find_element(*TestLocators.HEADER_BUTTON_PERSONAL_ACCOUNT).click()
