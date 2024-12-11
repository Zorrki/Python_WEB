class Animal:
    def __init__(self, name: str):
        self.name = name

class Bird(Animal):
    def __init__(self, name: str, wingspan: float):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self) -> float:
        """Возвращает длину крыла птицы (половина размаха крыльев)."""
        return self.wingspan / 2

class Fish(Animal):
    def __init__(self, name: str, max_depth: float):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self) -> str:
        """Возвращает категорию глубины рыбы в зависимости от значения max_depth."""
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"

class Mammal(Animal):
    def __init__(self, name: str, weight: float):
        super().__init__(name)
        self.weight = weight

    def category(self) -> str:
        """Возвращает категорию млекопитающего в зависимости от веса."""
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        else:
            return "Обычный"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str, *args) -> Animal:
        """Создаёт экземпляр животного заданного типа с переданными параметрами."""
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            raise ValueError('Недопустимый тип животного')

# Пример использования:
bird = AnimalFactory.create_animal('Bird', 'Попугай', 1.0)
fish = AnimalFactory.create_animal('Fish', 'Карп', 15)
mammal = AnimalFactory.create_animal('Mammal', 'Слон', 250)

print(f"{bird.name}: длина крыла {bird.wing_length()} м")
print(f"{fish.name}: категория {fish.depth()}")
print(f"{mammal.name}: категория {mammal.category()}")
