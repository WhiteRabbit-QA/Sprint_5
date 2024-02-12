from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import TestLocators


class TestConstructor:

    # Переход из личного кабинета в конструктор по клику на кнопку «Конструктор»
    def test_open_from_personal_account_with_button(self, driver, open_personal_account):

        # дождаться кликабельности кнопки "Конструктор"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.HEADER_BUTTON_CONSTR))

        # нажать кнопку "Конструктор"
        driver.find_element(*TestLocators.HEADER_BUTTON_CONSTR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.ACCOUNT_TITLE))

        # должен отображаться заголовок "Соберите бургер"
        assert driver.find_element(*TestLocators.ACCOUNT_TITLE).text == "Соберите бургер"

    # Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_open_from_personal_account_with_logo(self, driver, open_personal_account):

        # дождаться видимости логотипа
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_LOGO))

        # нажать на логотип
        driver.find_element(*TestLocators.HEADER_LOGO).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.ACCOUNT_TITLE))

        # должен отображаться заголовок "Соберите бургер"
        assert driver.find_element(*TestLocators.ACCOUNT_TITLE).text == "Соберите бургер"

    # Переход к разделу: «Булки»
    def test_scroll_to_burgers(self, driver):

        # нажать на вкладку "Соусы"
        driver.find_element(*TestLocators.MAIN_TAB_SAUCES).click()

        # скролл формы до заголовка "Булки"
        title = driver.find_element(*TestLocators.MAIN_TITLE_BURGERS)
        driver.execute_script("arguments[0].scrollIntoView();", title)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.MAIN_TAB_FILLING))

        # вкладка "Булки" должна быть выделена
        assert 'type_current' in driver.find_element(*TestLocators.MAIN_TAB_BURGERS).get_attribute('class')

    # Переход к разделу: «Соусы»
    def test_scroll_to_sauces(self, driver):

        # скролл формы до заголовка "Соусы"
        title = driver.find_element(*TestLocators.MAIN_TITLE_SAUCES)
        driver.execute_script("arguments[0].scrollIntoView();", title)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.MAIN_TAB_FILLING))

        # вкладка "Соусы" должна быть выделена
        assert 'type_current' in driver.find_element(*TestLocators.MAIN_TAB_SAUCES).get_attribute('class')

    # Переход к разделу: «Начинки»
    def test_scroll_to_filling(self, driver):

        # скролл формы до заголовка "Начинки"
        title = driver.find_element(*TestLocators.MAIN_TITLE_FILLING)
        driver.execute_script("arguments[0].scrollIntoView();", title)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.MAIN_TAB_SAUCES))

        # вкладка "Начинки" должна быть выделена
        assert 'type_current' in driver.find_element(*TestLocators.MAIN_TAB_FILLING).get_attribute('class')
