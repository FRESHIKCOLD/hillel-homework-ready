numbers = list(map(int, input().split()))
if not numbers:
    raise ValueError("Введіть хоча б одне число")
largest = max(numbers)
print(largest, numbers.index(largest))
