from fractions import Fraction

def process_fractions(fraction1, fraction2):
    # Разделяем строки на числитель и знаменатель
    num1, denom1 = map(int, fraction1.split('/'))
    num2, denom2 = map(int, fraction2.split('/'))

    # Создаем объекты Fraction
    frac1 = Fraction(num1, denom1)
    frac2 = Fraction(num2, denom2)

    # Находим сумму и произведение дробей
    sum_fractions = frac1 + frac2
    product_fractions = frac1 * frac2

    return sum_fractions, product_fractions

# Запросить у пользователя две дроби
fraction1 = input("Введите первую дробь (например, 3/4): ")
fraction2 = input("Введите вторую дробь (например, 5/6): ")

# Обработать дроби
sum_fractions, product_fractions = process_fractions(fraction1, fraction2)

print(f"Сумма дробей: {sum_fractions}")
print(f"Произведение дробей: {product_fractions}")
