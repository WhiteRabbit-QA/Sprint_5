**ЯндексПрактикум. Курс "Автоматизатор тестирования на Python".** 
---
**Спринт 5 "UI-тестрование"**
***
В проекте реализованы автотесты на Python для сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/).

### Автотесты созданы для разделов сайта:

****Регистрация (class TestRegistration)****
* `test_successful_registration` - регистрация с валидными данными
* `test_registration_wrong_password` (параметризованный) - регистрация с неверным паролем

***Авторизация (class TestLogin)***
* `test_login_from_main_page` - вход по кнопке «Войти в аккаунт» на главной странице
* `test_login_from_personal_account` - вход через кнопку «Личный кабинет»
* `test_login_from_register_form` - вход через кнопку в форме регистрации
* `test_login_from_password_recovery_form` - вход через кнопку в форме восстановления пароля

***Выход из аккаунта (class TestLogOut)***
* `test_log_out_from_personal_account` - выход по кнопке «Выйти» в личном кабинете

***Личный кабинет (class TestAccount)***
* `test_successful_open_personal_account` - переход в личный кабинет по клику на кнопку «Личный кабинет»

***Раздел конструктор (class TestConstructor)***
* `test_open_from_personal_account_with_button` - переход из личного кабинета в конструктор по клику на кнопку «Конструктор»
* `test_open_from_personal_account_with_logo` - переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
* `test_scroll_to_burgers` - переход к разделу «Булки»
* `test_scroll_to_sauces` - переход к разделу «Соусы»
* `test_scroll_to_filling` - переход к разделу «Начинки»
***
### Структура проекта
В директории tests/ хранятся:
* модули с тестами
* описание локаторов `locators.py`

В модуле `conftest.py` реализованы фикстуры:

* driver - инициализация Google Chrome и получение URL сайта
* log_in - успешная авторизация
* open_personal_account - переход в личный кабинет

Тестовые данные хранятся в модулях:
* `data.py` - для авторизации
* `helpers.py` - для регистрации
***
### Для запуска тестов
* Подключить Selenium
```
pip install selenium
```
* Для автоматической установки и обновления веб-драйвера установить Webdriver Manager
```
pip install webdriver_manager
```
* Для генерации случайных данных установить библиотеку Faker
```
pip install Faker
```
* Установить pytest
```
pip install pytest
```
* Запуск всех тестов
```
pytest -vs
```
