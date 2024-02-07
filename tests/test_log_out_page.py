from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators


class TestLogOut:

    # выход по кнопке «Выйти» в личном кабинете
    def test_log_out_from_personal_account(self, driver, open_personal_account):

        # дождаться кликабельности кнопки "Выход"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOG_OUT))

        # нажать кнопку "Выход"
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_LOG_OUT).click()

        # отображается заголовок формы авторизации
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM_TITLE))
        assert driver.find_element(*TestLocators.AUTH_FORM_TITLE).text == "Вход"
