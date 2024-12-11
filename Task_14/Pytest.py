import pytest

class InsufficientFundsError(Exception):
    """Исключение, выбрасываемое при попытке снять больше средств, чем доступно на счете."""
    def __init__(self):
        super().__init__("Недостаточно средств на счете.")

class BankAccount:
    """Класс для управления балансом счета."""
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError()
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Текущий счет: {self.balance}"

# Тесты для BankAccount с использованием pytest
@pytest.fixture
def bank_account():
    """Фикстура для подготовки тестового состояния."""
    return BankAccount(100)  # Начальный баланс 100

def test_initial_balance(bank_account):
    """Проверка начального баланса."""
    assert bank_account.get_balance() == 100

def test_deposit(bank_account):
    """Проверка депозита."""
    bank_account.deposit(50)
    assert bank_account.get_balance() == 150

def test_withdraw(bank_account):
    """Проверка снятия средств."""
    bank_account.withdraw(30)
    assert bank_account.get_balance() == 70

def test_withdraw_insufficient_funds(bank_account):
    """Проверка снятия больше средств, чем доступно."""
    with pytest.raises(InsufficientFundsError):
        bank_account.withdraw(200)

def test_deposit_negative_amount(bank_account):
    """Проверка депозита отрицательной суммы."""
    with pytest.raises(ValueError):
        bank_account.deposit(-10)

# Запуск программы для проверки работы класса (опционально)
if __name__ == "__main__":
    # Пример использования класса BankAccount
    account = BankAccount(100)
    print(account)

    account.deposit(50)
    print(f"После депозита 50: {account.get_balance()}")

    try:
        account.withdraw(200)
    except InsufficientFundsError as e:
        print(e)

    print(f"После снятия 30: {account.withdraw(30)}")
    print(account)
