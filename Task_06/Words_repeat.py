def count_words(words_list):
    # Шаг 1: Создание пустого словаря
    word_count = {}
    
    # Шаг 2: Проход через каждый элемент (слово) в списке
    for word in words_list:
        # Шаг 3: Использование метода get() для получения текущего значения по ключу
        current_count = word_count.get(word, 0)
        # Шаг 4: Обновление количества повторений слова в словаре
        word_count[word] = current_count + 1
    
    return word_count

# Пример использования функции
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(count_words(words))
