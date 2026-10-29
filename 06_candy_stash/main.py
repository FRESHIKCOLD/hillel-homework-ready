class CandyStash:
    MAX_CAPACITY = 50

    @staticmethod
    def validate_amount(value):
        if type(value) is not int or value < 0:
            raise ValueError("Кількість має бути невід'ємним цілим числом")

    def __init__(self, count=0):
        self.count = count

    @classmethod
    def full_stash(cls):
        return cls(cls.MAX_CAPACITY)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self.validate_amount(value)
        self._count = min(value, self.MAX_CAPACITY)

    def __str__(self):
        return f"CandyStash ({self.count}/{self.MAX_CAPACITY})"

    def __repr__(self):
        return str(self)

    def __add__(self, amount):
        self.validate_amount(amount)
        return type(self)(self.count + amount)

    def __sub__(self, amount):
        self.validate_amount(amount)
        return type(self)(max(0, self.count - amount))

    def __eq__(self, other):
        if isinstance(other, CandyStash):
            return self.count == other.count
        if type(other) is int:
            return self.count == other
        return NotImplemented


if __name__ == "__main__":
    stash = CandyStash(12)
    print(stash)
    stash = stash + 45
    print(stash)
    stash = stash - 100
    print(stash)
    print(CandyStash.full_stash() == 50)
