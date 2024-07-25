class Money:
    def __init__(self, dollars_count, cents_count):
        self.dollars_count = dollars_count
        self.cents_count = cents_count
        self.total_cents = dollars_count * 100 + cents_count

    def set_count_dollars(self, dollars_value):
        self.dollars_count = dollars_value
        self.total_cents = dollars_value * 100 + self.cents_count
        return self.total_cents

    def set_count_cents(self, cents_count):
        self.cents_count = cents_count
        self.total_cents = self.dollars_count * 100 + cents_count
        return self.total_cents

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars_count} долларов {self.cents_count} центов'

money = Money(10, 50)
money.set_count_dollars(20)
money.set_count_cents(75)
print(money.__str__())  # Ваше состояние составляет 20 долларов 75 центов
