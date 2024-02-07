from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators


class TestAccount:

    # переход в личный кабинет по клику на кнопку "Личный кабинет"
    def test_successful_open_personal_account(self, driver, log_in):

        # дождаться кликабельности кнопки "Личный кабинет"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.HEADER_BUTTON_PERSONAL_ACCOUNT))

        # нажать кнопку "Личный кабинет"
        driver.find_element(*TestLocators.HEADER_BUTTON_PERSONAL_ACCOUNT).click()

        # должна отображаться кнопка "Профиль"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON_PROFILE))
        assert driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_PROFILE).text == "Профиль"
