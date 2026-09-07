# Наша тестируемая функция
def is_email_valid(email):
    if "@" in email and "." in email:
        return True
    return False

# Тест 1: Проверяем валидный email (должен вернуть True)
def test_valid_email():
    result = is_email_valid("user@example.com")
    assert result == True

# Тест 2: Проверяем невалидный email без собачки (должен вернуть False)
def test_invalid_email_without_at():
    result = is_email_valid("userexample.com")
    assert result == False