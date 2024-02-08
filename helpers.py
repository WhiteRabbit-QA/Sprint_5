import random
import string
from faker import Faker


# рандомное имя для регистрации
def some_name():
    faker = Faker('en_US')
    name = faker.first_name()
    return name


# рандомный валидный email для регистрации
def reg_email():
    allowed_chars = string.ascii_letters + string.digits
    login = "kategrinchenko5" + str(random.randint(100, 999))
    domain = f"@{''.join(random.choice(allowed_chars) for _ in range(6))}.{random.choice(['net', 'com', 'ua', 'ru'])}"
    email = login + domain
    return email


# рандомный валидный пароль для регистрации
def reg_password():
    min_allowed_len = 6  # password length
    allowed_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(allowed_chars) for _ in range(min_allowed_len))
    return password
