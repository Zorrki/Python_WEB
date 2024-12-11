class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height is not None else width  # Если высота не указана, создаём квадрат

    def perimeter(self):
        """Вычисляет периметр прямоугольника"""
        return 2 * (self.width + self.height)

    def area(self):
        """Вычисляет площадь прямоугольника"""
        return self.width * self.height

    def __add__(self, other):
        """Определяет операцию сложения для двух прямоугольников"""
        new_perimeter = self.perimeter() + other.perimeter()
        new_width = new_perimeter // 4
        new_height = new_width  # Для простоты вычисления используем квадрат
        return Rectangle(new_width, new_height)

    def __sub__(self, other):
        """Определяет операцию вычитания одного прямоугольника из другого"""
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_width = new_perimeter // 4
        new_height = new_width  # Для простоты вычисления используем квадрат
        return Rectangle(new_width, new_height)

    def __lt__(self, other):
        """Определяет операцию "меньше" по площади для двух прямоугольников"""
        return self.area() < other.area()

    def __eq__(self, other):
        """Определяет операцию "равно" по площади для двух прямоугольников"""
        return self.area() == other.area()

    def __le__(self, other):
        """Определяет операцию "меньше или равно" по площади для двух прямоугольников"""
        return self.area() <= other.area()

    def __str__(self):
        """Возвращает строковое представление прямоугольника"""
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """Возвращает строковое представление прямоугольника для разработчика"""
        return f"Rectangle({self.width}, {self.height})"


# Примеры работы с классом Rectangle
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

# Вывод периметра и площади
print(f"Периметр rect1: {rect1.perimeter()}")  # Вывод: 30
print(f"Площадь rect2: {rect2.area()}")  # Вывод: 21

# Сравнение прямоугольников по площади
print(f"rect1 < rect2: {rect1 < rect2}")  # Вывод: False
print(f"rect1 == rect2: {rect1 == rect2}")  # Вывод: False
print(f"rect1 <= rect2: {rect1 <= rect2}")  # Вывод: False

# Сложение и вычитание прямоугольников
rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")  # Вывод: 50
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")  # Вывод: 2

# Дополнительный тест для repr и str
print(rect3)  # Вывод: Прямоугольник со сторонами 12 и 12
print(repr(rect4))  # Вывод: Rectangle(2, 2)
