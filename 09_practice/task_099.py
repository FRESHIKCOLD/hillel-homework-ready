k = int(input())
n = int(input())
if k <= 0 or n <= 0:
    raise ValueError("k і n мають бути додатними")
print((n - 1) // k + 1, (n - 1) % k + 1)
