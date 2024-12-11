import os
import csv

class Student:
    def __init__(self, name, subjects_file):
        # Устанавливаем ФИО с помощью дескриптора
        self.__setattr__('name', name)
        self.subjects = {}
        # Загружаем предметы из файла
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        # Проверяем ФИО на правильность
        if name == 'name':
            if not (value and value[0].isupper() and value.replace(" ", "").isalpha()):
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        # Возвращаем предмет из словаря, если он существует
        if name in self.subjects:
            return self.subjects[name]
        raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        # Формируем строковое представление студента и его предметов
        subject_list = ', '.join(self.subjects.keys())
        return f"Студент: {self.name}\nПредметы: {subject_list}"

    def load_subjects(self, subjects_file):
        try:
            # Читаем предметы из файла CSV
            print(f"Текущая рабочая директория: {os.getcwd()}")
            with open(subjects_file, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    subjects = [subject.strip() for subject in row]
                    for subject in subjects:
                        if subject:
                            self.subjects[subject] = {'grades': [], 'test_scores': []}
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {subjects_file} не найден")

    def add_grade(self, subject, grade):
        # Добавляем оценку по предмету с проверкой корректности
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return
        if not (isinstance(grade, int) and 2 <= grade <= 5):
            print("Оценка должна быть целым числом от 2 до 5")
            return
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        # Добавляем результат теста по предмету с проверкой корректности
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return
        if not (isinstance(test_score, int) and 0 <= test_score <= 100):
            print("Результат теста должен быть целым числом от 0 до 100")
            return
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        # Возвращаем средний балл по тестам для заданного предмета
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return None
        scores = self.subjects[subject]['test_scores']
        if not scores:
            return 0.0
        return sum(scores) / len(scores)

    def get_average_grade(self):
        # Возвращаем средний балл по всем предметам
        all_grades = [grade for sub in self.subjects.values() for grade in sub['grades']]
        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)


# Пример использования
if __name__ == "__main__":
    # Создаем экземпляр студента, загружаем предметы из файла subjects.csv
    student = Student("Иван Иванов", "subjects.csv")
    # Добавляем оценки и результаты тестов
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)
    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    student.add_grade("Физика", 3)
    student.add_test_score("Физика", 78)
    student.add_grade("Литература", 5)
    student.add_test_score("Литература", 88)
    student.add_grade("Биология", 4)
    student.add_test_score("Биология", 95)
    student.add_grade("Химия", 2)
    student.add_test_score("Химия", 68)
    student.add_grade("География", 3)
    student.add_test_score("География", 74)
    student.add_grade("Информатика", 5)
    student.add_test_score("Информатика", 92)

    # Получаем средний балл и результат по тестам
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")
    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")
    # Выводим информацию о студенте
    print(student)
