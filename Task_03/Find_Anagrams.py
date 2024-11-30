def are_anagrams(word1, word2):
    # Сначала проверяем, равна ли длина слов
    if len(word1) != len(word2):
        return False

    # Создаем два словаря для хранения частоты символов
    char_count1 = {}
    char_count2 = {}

    # Подсчитываем частоту символов в первом слове
    for char in word1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    # Подсчитываем частоту символов во втором слове
    for char in word2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    # Сравниваем оба словаря
    return char_count1 == char_count2

# Запросим у пользователя два слова
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

# Проверяем, являются ли слова анаграммами
if are_anagrams(word1, word2):
    print("Слова являются анаграммами.")
else:
    print("Слова не являются анаграммами.")
