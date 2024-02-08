import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators
import helpers


class TestRegistration:

    # регистрация с валидными данными
    def test_successful_registration(self, driver):

        # дождаться кликабельности кнопки "Войти в аккаунт"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.MAIN_BUTTON_LOGIN))

        # нажать кнопку "Войти в аккаунт"
        driver.find_element(*TestLocators.MAIN_BUTTON_LOGIN).click()

        # дождаться кликабельности кнопки "Зарегистрироваться"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.AUTH_BUTTON_REGISTR))

        # нажать кнопку "Зарегистрироваться"
        driver.find_element(*TestLocators.AUTH_BUTTON_REGISTR).click()

        # дождаться отображения заголовка страницы "Регистрация"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.REG_FORM_TITLE))

        # заполнить инпут "Имя" валидным значением
        driver.find_element(*TestLocators.REG_FORM_INPUT_NAME).send_keys(helpers.some_name())

        # заполнить инпут "Email" валидным значением
        driver.find_element(*TestLocators.REG_FORM_INPUT_EMAIL).send_keys(helpers.reg_email())

        # заполнить инпут "Пароль" валидным значением
        driver.find_element(*TestLocators.REG_FORM_INPUT_PASSWORD).send_keys(helpers.reg_password())

        # нажать кнопку "Зарегистрироваться"
        driver.find_element(*TestLocators.REG_FORM_BUTTON).click()

        # дождаться, чтобы стал виден заголовок страницы
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM_TITLE))

        # проверить, что URL содержит login
        assert "login" in driver.current_url

    # регистрация с неверным паролем
    @pytest.mark.parametrize(
        'wrong_password',
        [
            pytest.param(' ', id=' '),
            pytest.param('1', id='1'),
            pytest.param('12345', id='12345')
        ]
    )
    def test_registration_wrong_password(self, driver, wrong_password):

        # дождаться кликабельности кнопки "Войти в аккаунт"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.MAIN_BUTTON_LOGIN))

        # нажать кнопку "Войти в аккаунт"
        driver.find_element(*TestLocators.MAIN_BUTTON_LOGIN).click()

        # дождаться кликабельности кнопки "Зарегистрироваться"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.AUTH_BUTTON_REGISTR))

        # нажать кнопку "Зарегистрироваться"
        driver.find_element(*TestLocators.AUTH_BUTTON_REGISTR).click()

        # заполнить инпут "Имя" валидным значением
        driver.find_element(*TestLocators.REG_FORM_INPUT_NAME).send_keys(helpers.some_name())

        # заполнить инпут "Email" валидным значением
        driver.find_element(*TestLocators.REG_FORM_INPUT_EMAIL).send_keys(helpers.reg_email())

        # заполнить инпут "Пароль" невалидным значением
        driver.find_element(*TestLocators.REG_FORM_INPUT_PASSWORD).send_keys(wrong_password)

        # нажать кнопку "Зарегистрироваться"
        driver.find_element(*TestLocators.REG_FORM_BUTTON).click()

        # дождаться, чтобы стал виден заголовок страницы
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.REG_FORM_TITLE))

        # проверить, что появилась ошибка
        assert driver.find_element(*TestLocators.REG_FORM_TEXT_ERROR_PASSWORD).text == "Некорректный пароль"
