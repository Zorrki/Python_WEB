def triangle_type(a, b, c):
    # Проверка существования треугольника
    if a + b > c and a + c > b and b + c > a:
        # Проверка типа треугольника
        if a == b == c:
            return "Треугольник равносторонний"
        elif a == b or a == c or b == c:
            return "Треугольник равнобедренный"
        else:
            return "Треугольник разносторонний"
    else:
        return "Треугольник с такими сторонами не существует"

# Запросить у пользователя длины сторон треугольника
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

result = triangle_type(a, b, c)
print(result)
