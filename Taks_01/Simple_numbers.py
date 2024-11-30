import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(sequence):
    prime_count = 0
    for number in sequence:
        if is_prime(number):
            prime_count += 1
    return prime_count

# Запросить у пользователя количество чисел в последовательности
num_count = int(input("Введите количество чисел: "))
sequence = []

# Запросить у пользователя числа последовательности
for _ in range(num_count):
    number = int(input("Введите число: "))
    sequence.append(number)

# Подсчитать количество простых чисел в последовательности
prime_count = count_primes(sequence)

print(f"Количество простых чисел в последовательности: {prime_count}")
