class BankAccount:
    def __init__(self, owner, balance, pin):
        self.__owner = owner
        self.__balance = balance
        self.__pin = pin
    def __validate_pin(self, pin):
        return self.__pin == pin
    def __is_positive(self, amount):
        return amount > 0
    def deposit(self, amount, pin):
        if not self.__validate_pin(pin):
            return "Неверный пин-код"
        if not self.__is_positive(amount):
            return "Сумма должна быть положительной"
        self.__balance += amount
        return f"Пополнено на {amount}. Новый баланс: {self.__balance}"
    def withdraw(self, amount, pin):
        if not self.__validate_pin(pin):
            return "Неверный пин-код"
        if not self.__is_positive(amount):
            return "Сумма должна быть положительной"
        if amount > self.__balance:
            return "Недостаточно средств"
        self.__balance -= amount
        return f"Снято {amount}. Остаток: {self.__balance}"
    def get_balance(self, pin):
        if self.__validate_pin(pin):
            return self.__balance
        return None