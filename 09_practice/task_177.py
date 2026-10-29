n = int(input())
if not 0 <= n <= 9999:
    raise ValueError("Число має бути від 0 до 9999")
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
print(a != b and a != c and a != d and b != c and b != d and c != d)
