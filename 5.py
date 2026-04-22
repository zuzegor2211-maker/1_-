import random
import string

class PasswordManager:
    @staticmethod
    def is_secure(password):
        """Проверка пароля на безопасность"""
        if len(password) < 10:
            return False
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        return has_upper and has_lower and has_digit

    @staticmethod
    def generate_secure_password(length=12):
        """Генерация безопасного пароля"""
        if length < 10:
            length = 10

        # Гарантируем наличие хотя бы одной заглавной, одной строчной и одной цифры
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits)
        ]

        # Заполняем остальные символы
        all_chars = string.ascii_letters + string.digits
        for _ in range(length - 3):
            password.append(random.choice(all_chars))

        # Перемешиваем
        random.shuffle(password)
        return ''.join(password)


# Демонстрация
if __name__ == "__main__":
    pm = PasswordManager()

    test_passwords = ["weak", "WeakPass1", "StrongPass123", "abcDEF12345"]
    for pwd in test_passwords:
        print(f"'{pwd}': {'безопасный' if pm.is_secure(pwd) else 'ненадёжный'}")

    print("\nСгенерированный безопасный пароль:", pm.generate_secure_password())
    print("Длина:", len(pm.generate_secure_password()))
