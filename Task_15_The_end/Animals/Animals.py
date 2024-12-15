import os
import logging
import argparse
import json
from datetime import datetime

# Настройка логирования
script_dir = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger('animal_logger')
logger.setLevel(logging.DEBUG)

# Форматтер для сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Обработчики логов
debug_info_handler = logging.FileHandler(os.path.join(script_dir, 'debug_info.log'), encoding='utf-8')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)

warnings_errors_handler = logging.FileHandler(os.path.join(script_dir, 'warnings_errors.log'), encoding='utf-8')
warnings_errors_handler.setLevel(logging.WARNING)
warnings_errors_handler.setFormatter(formatter)

logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

# Класс-декоратор для логирования
class LoggerDecorator:
    def __init__(self, logger):
        self.logger = logger

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            self.logger.info(f"Выполнение {func.__name__} с параметрами args: {args}, kwargs: {kwargs}")
            try:
                result = func(*args, **kwargs)
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()
                self.logger.info(f"{func.__name__} выполнено успешно за {duration} секунд. Результат: {result}")
                return result
            except Exception as e:
                self.logger.error(f"Ошибка в {func.__name__}: {e}", exc_info=True)
                raise
        return wrapper

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def to_dict(self):
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        return data

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
    @LoggerDecorator(logger)
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

# Список для хранения всех созданных животных
all_animals = []

def save_animals():
    with open(os.path.join(script_dir, 'animals.json'), 'w', encoding='utf-8') as f:
        json.dump([animal.to_dict() for animal in all_animals], f, ensure_ascii=False, indent=4)

def load_animals():
    if os.path.exists(os.path.join(script_dir, 'animals.json')):
        with open(os.path.join(script_dir, 'animals.json'), 'r', encoding='utf-8') as f:
            animal_dicts = json.load(f)
            for animal_dict in animal_dicts:
                animal_type = animal_dict.pop('__class__')
                if animal_type == 'Bird':
                    all_animals.append(Bird(**animal_dict))
                elif animal_type == 'Fish':
                    all_animals.append(Fish(**animal_dict))
                elif animal_type == 'Mammal':
                    all_animals.append(Mammal(**animal_dict))

def main():
    parser = argparse.ArgumentParser(description='Создание животных и сохранение данных.')
    parser.add_argument('-F', '--all', action='store_true', help='Вывод всех данных о животных')
    parser.add_argument('animal_type', nargs='?', type=str, choices=['Bird', 'Fish', 'Mammal'], help='Тип животного')
    parser.add_argument('name', nargs='?', type=str, help='Имя животного')
    parser.add_argument('param', nargs='?', type=float, help='Дополнительный параметр животного (размах крыльев, глубина или вес)')
    args = parser.parse_args()

    if args.all:
        print("\nВсе созданные животные:")
        for ani in all_animals:
            if isinstance(ani, Bird):
                print(f"Bird: {ani.name}, длина крыла {ani.wing_length()} м")
            elif isinstance(ani, Fish):
                print(f"Fish: {ani.name}, категория {ani.depth()}")
            elif isinstance(ani, Mammal):
                print(f"Mammal: {ani.name}, категория {ani.category()}")
    elif args.animal_type and args.name and args.param is not None:
        animal = AnimalFactory.create_animal(args.animal_type, args.name, args.param)
        all_animals.append(animal)
        save_animals()

        if args.animal_type == 'Bird':
            print(f"{animal.name}: длина крыла {animal.wing_length()} м")
        elif args.animal_type == 'Fish':
            print(f"{animal.name}: категория {animal.depth()}")
        elif args.animal_type == 'Mammal':
            print(f"{animal.name}: категория {animal.category()}")
        
        # Генерация предупреждения для тестирования
        if args.param > 200:
            logger.warning(f"Значение параметра {args.param} превышает 200")
    else:
        parser.print_help()

if __name__ == '__main__':
    load_animals()
    main()
