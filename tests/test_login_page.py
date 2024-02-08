from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators
import data


class TestLogin:

    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page(self, driver):

        # дождаться кликабельности кнопки "Войти в аккаунт"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.MAIN_BUTTON_LOGIN))

        # нажать кнопку "Войти в аккаунт"
        driver.find_element(*TestLocators.MAIN_BUTTON_LOGIN).click()

        # заполнить поля валидными данными
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM_TITLE))
        driver.find_element(*TestLocators.AUTH_FORM_INPUT_EMAIL).send_keys(data.user_email)
        driver.find_element(*TestLocators.AUTH_FORM_INPUT_PASSWORD).send_keys(data.user_password)

        # нажать кнопку "Войти"
        driver.find_element(*TestLocators.AUTH_FORM_BUTTON).click()

        # должна отображаться кнопка "Оформить заказ"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.ACCOUNT_BUTTON_ORDER))
        assert driver.find_element(*TestLocators.ACCOUNT_BUTTON_ORDER).text == "Оформить заказ"

    # вход через кнопку «Личный кабинет»
    def test_login_from_personal_account(self, driver):

        # дождаться кликабельности кнопки "Личный кабинет"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.HEADER_BUTTON_PERSONAL_ACCOUNT))

        # нажать кнопку "Личный кабинет"
        driver.find_element(*TestLocators.HEADER_BUTTON_PERSONAL_ACCOUNT).click()

        # заполнить поля валидными данными
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM_TITLE))
        driver.find_element(*TestLocators.AUTH_FORM_INPUT_EMAIL).send_keys(data.user_email)
        driver.find_element(*TestLocators.AUTH_FORM_INPUT_PASSWORD).send_keys(data.user_password)

        # нажать кнопку "Войти"
        driver.find_element(*TestLocators.AUTH_FORM_BUTTON).click()

        # должна отображаться кнопка "Оформить заказ"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.ACCOUNT_BUTTON_ORDER))
        assert driver.find_element(*TestLocators.ACCOUNT_BUTTON_ORDER).text == "Оформить заказ"

    # вход через кнопку в форме регистрации
    def test_login_from_register_form(self, driver):

        # перейти на страницу регистрации
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.MAIN_BUTTON_LOGIN))
        driver.find_element(*TestLocators.MAIN_BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.AUTH_BUTTON_REGISTR))
        driver.find_element(*TestLocators.AUTH_BUTTON_REGISTR).click()

        # дождаться кликабельности кнопки "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.REG_BUTTON_LOGIN))

        # нажать на кнопку "Войти
        driver.find_element(*TestLocators.REG_BUTTON_LOGIN).click()

        # заполнить поля валидными данными
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM_TITLE))
        driver.find_element(*TestLocators.AUTH_FORM_INPUT_EMAIL).send_keys(data.user_email)
        driver.find_element(*TestLocators.AUTH_FORM_INPUT_PASSWORD).send_keys(data.user_password)

        # нажать кнопку "Войти"
        driver.find_element(*TestLocators.AUTH_FORM_BUTTON).click()

        # должна отображаться кнопка "Оформить заказ"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.ACCOUNT_BUTTON_ORDER))
        assert driver.find_element(*TestLocators.ACCOUNT_BUTTON_ORDER).text == "Оформить заказ"

    # вход через кнопку в форме восстановления пароля
    def test_login_from_password_recovery_form(self, driver):

        # перейти на страницу восстановления пароля
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.MAIN_BUTTON_LOGIN))
        driver.find_element(*TestLocators.MAIN_BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.AUTH_BUTTON_RESTORE))
        driver.find_element(*TestLocators.AUTH_BUTTON_RESTORE).click()

        # ожидание видимости кнопки "Войти"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.RECOVERY_BUTTON_LOGIN))

        # нажать на кнопку "Войти"
        driver.find_element(*TestLocators.RECOVERY_BUTTON_LOGIN).click()

        # заполнить поля валидными данными
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM_TITLE))
        driver.find_element(*TestLocators.AUTH_FORM_INPUT_EMAIL).send_keys(data.user_email)
        driver.find_element(*TestLocators.AUTH_FORM_INPUT_PASSWORD).send_keys(data.user_password)

        # нажать кнопку "Войти"
        driver.find_element(*TestLocators.AUTH_FORM_BUTTON).click()

        # должна отображаться кнопка "Оформить заказ"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.ACCOUNT_BUTTON_ORDER))
        assert driver.find_element(*TestLocators.ACCOUNT_BUTTON_ORDER).text == "Оформить заказ"
