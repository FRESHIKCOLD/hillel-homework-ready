class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return 0 <= v and self.coins + v <= self.capacity

    def add(self, v):
        if not self.can_add(v):
            raise ValueError("Недостатньо місця або від'ємна кількість монет")
        self.coins += v


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    k = int(input())
    box = MoneyBox(n)
    box.add(m)
    print(box.can_add(k))
