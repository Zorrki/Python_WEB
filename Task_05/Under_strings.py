def substrings(s):
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield s[start:end]

# Пример использования
input_string = "abc"
print("Все возможные подстроки строки:")
for substring in substrings(input_string):
    print(substring)
