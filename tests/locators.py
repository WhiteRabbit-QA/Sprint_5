from selenium.webdriver.common.by import By


class TestLocators:
    # Хедер - кнопка "Личный кабинет"
    HEADER_BUTTON_PERSONAL_ACCOUNT = By.CSS_SELECTOR, "nav>a p"

    # Хедер - кнопка "Конструктор"
    HEADER_BUTTON_CONSTR = By.LINK_TEXT, "Конструктор"

    # Хедер - логотип
    HEADER_LOGO = By.CSS_SELECTOR, "nav div a"

    # Главная страница - кнопка "Войти в аккаунт"
    MAIN_BUTTON_LOGIN = By.CSS_SELECTOR, "[class*='button_button']"

    # Главная страница - вкладка "Булки"
    MAIN_TAB_BURGERS = By.XPATH, "//span[text()='Булки']/parent::*"

    # Главная страница - заголовок списка "Булки"
    MAIN_TITLE_BURGERS = By.XPATH, "//h2[contains(@class, 'text') and text()='Булки']"

    # Главная страница - вкладка "Соусы"
    MAIN_TAB_SAUCES = By.XPATH, "//span[text()='Соусы']/parent::*"

    # Главная страница - заголовок списка "Соусы"
    MAIN_TITLE_SAUCES = By.XPATH, "//h2[contains(@class, 'text') and text()='Соусы']"

    # Главная страница - вкладка "Начинки"
    MAIN_TAB_FILLING = By.XPATH, "//span[text()='Начинки']/parent::*"

    # Главная страница - заголовок списка "Начинки"
    MAIN_TITLE_FILLING = By.XPATH, "//h2[contains(@class, 'text') and text()='Начинки']"

    # Страница авторизации - кнопка "Зарегистрироваться"
    AUTH_BUTTON_REGISTR = By.LINK_TEXT, "Зарегистрироваться"

    # Страница авторизации - кнопка "Восстановить пароль"
    AUTH_BUTTON_RESTORE = By.LINK_TEXT, "Восстановить пароль"

    # Форма авторизации - заголовок "Вход"
    AUTH_FORM_TITLE = By.XPATH, "//h2[text()='Вход']"

    # Форма авторизации - поле "Email"
    AUTH_FORM_INPUT_EMAIL = By.CSS_SELECTOR, ".Auth_form__3qKeq.mb-20 input[type='text']"

    # Форма авторизации - поле "Пароль"
    AUTH_FORM_INPUT_PASSWORD = By.CSS_SELECTOR, ".Auth_form__3qKeq.mb-20 input[type='password']"

    # Форма авторизации - кнопка "Войти"
    AUTH_FORM_BUTTON = By.CSS_SELECTOR, ".Auth_form__3qKeq.mb-20 button"

    # Страница регистрации - кнопка "Войти"
    REG_BUTTON_LOGIN = By.XPATH, "//*[contains(@class, 'Auth_link')]"

    # Форма регистрации - заголовок "Регистрация"
    REG_FORM_TITLE = By.XPATH, "//h2[text()='Регистрация']"

    # Форма регистрации - поле "Имя"
    REG_FORM_INPUT_NAME = By.XPATH, "//label[text()='Имя']/following-sibling::input"

    # Форма регистрации - поле "Email"
    REG_FORM_INPUT_EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input"

    # Форма регистрации - поле "Пароль"
    REG_FORM_INPUT_PASSWORD = By.CSS_SELECTOR, "[type='password']"

    # Форма регистрации - кнопка "Зарегистрироваться"
    REG_FORM_BUTTON = By.CSS_SELECTOR, "form button"

    # Форма регистрации - ошибка "Некорректный пароль"
    REG_FORM_TEXT_ERROR_PASSWORD = By.CLASS_NAME, "input__error"

    # Страница восстановления пароля - кнопка "Войти"
    RECOVERY_BUTTON_LOGIN = By.LINK_TEXT, "Войти"

    # Страница аккаунта - кнопка "Оформите заказ"
    ACCOUNT_BUTTON_ORDER = By.CSS_SELECTOR, ".BurgerConstructor_basket__29Cd7.mt-25 button"

    # Страница аккаунта - заголовок "Соберите бургер"
    ACCOUNT_TITLE = By.CSS_SELECTOR, "main section h1"

    # Личный кабинет - кнопка "Профиль"
    PERSONAL_ACCOUNT_BUTTON_PROFILE = By.LINK_TEXT, "Профиль"

    # Личный кабинет - кнопка "Выход"
    PERSONAL_ACCOUNT_BUTTON_LOG_OUT = By.CSS_SELECTOR, "[class*='Account_button']"
