class DeliveryCalculator:
    def calculate(self, total):
        if total < 0:
            raise ValueError("Сума замовлення не може бути від'ємною")
        if total >= 1000:
            return 0
        return 50


if __name__ == "__main__":
    calculator = DeliveryCalculator()
    assert calculator.calculate(100) == 50
    assert calculator.calculate(1000) == 0
    try:
        calculator.calculate(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("Очікувався ValueError")
    print("Усі 3 сценарії перевірено")
