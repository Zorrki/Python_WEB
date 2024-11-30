import random
import string

def generate_password(length):
    # Определяем набор символов для пароля
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Генерируем случайный пароль
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Запросить у пользователя длину пароля
length = int(input("Введите длину пароля: "))

# Генерируем и выводим пароль
generated_password = generate_password(length)
print(f"Сгенерированный пароль: {generated_password}")
