def fib(n):
    if n <= 2:
        return 1
    old = 1
    new = 1
    for i in range(n-2):
        updated = new + old
        old = new
        new = updated
    return new
print(fib(4))