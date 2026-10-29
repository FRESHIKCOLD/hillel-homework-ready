n = int(input())
sign = -1 if n < 0 else 1
n = abs(n)
reversed_number = 0
while n > 0:
    reversed_number = reversed_number * 10 + n % 10
    n //= 10
print(sign * reversed_number)
