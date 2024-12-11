class BookNotFoundError(Exception):
    """Исключение, выбрасываемое при попытке удалить книгу, которой нет в библиотеке."""
    def __init__(self):
        super().__init__("Книга не найдена в библиотеке.")

class Library:
    """Класс для управления библиотекой книг."""
    def __init__(self):
        self.books = set()

    def add_book(self, title):
        """Добавляет книгу в библиотеку."""
        self.books.add(title)

    def remove_book(self, title):
        """Удаляет книгу из библиотеки."""
        if title not in self.books:
            raise BookNotFoundError()
        self.books.remove(title)

    def list_books(self):
        """Возвращает список всех книг в библиотеке."""
        return list(self.books)

# Код тестирования:
import unittest

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("1984")
        self.assertIn("1984", self.library.list_books())

    def test_remove_book(self):
        self.library.add_book("Brave New World")
        self.library.remove_book("Brave New World")
        self.assertNotIn("Brave New World", self.library.list_books())

    def test_remove_nonexistent_book(self):
        with self.assertRaises(BookNotFoundError):
            self.library.remove_book("Nonexistent Book")

    def test_list_books(self):
        self.library.add_book("1984")
        self.library.add_book("Brave New World")
        books = self.library.list_books()
        self.assertIn("1984", books)
        self.assertIn("Brave New World", books)

    def test_remove_book_updates_list(self):
        self.library.add_book("1984")
        self.library.add_book("Brave New World")
        self.library.remove_book("1984")
        books = self.library.list_books()
        self.assertNotIn("1984", books)
        self.assertIn("Brave New World", books)

if __name__ == '__main__':
    unittest.main()
