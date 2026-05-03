from faker import Faker

fake = Faker()

def generate_created_user_dict():
    return {
        "name": fake.user_name(),
        "email": fake.email(),
        "password": fake.password()
        }

def generate_user_credentials():
    """Генерация случайных учетных данных для входа"""
    return {
        "email": fake.email(),
        "password": fake.password()
        }
