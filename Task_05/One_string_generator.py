names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

result = {name: round(sal * float(bon.strip('%')) / 100, 2) for name, sal, bon in zip(names, salary, bonus)}

print(result)
