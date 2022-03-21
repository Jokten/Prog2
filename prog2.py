import time

def findsNr(key, s):
    if len(s) == 0:
        return 0
    val = findsNr(key, s[1:])
    if s[0] == key:
        val += 1
    return val


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


def multiply(a, b):
    if a > b:
        m, n = a, b
    else:
        m, n = b, a
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)


def divide(t, n):
    if t - n < 0:
        return 0
    else:
        return 1 + divide(t - n, n)


def harmonic(n):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic(n - 1)


def largest(a):
    if len(a) == 1:
        return a[0]
    elif a[0] > largest(a[1:]):
        return a[0]
    else:
        return largest(a[1:])


def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])


def bricklek(fr, h, to, n):
    if n == 1:
        print(f'{fr}->{to}')
    else:
        bricklek(fr, to, h, n-1)
        print(f'{fr}->{to}')
        bricklek(h, fr, to, n-1)


def count(x, s):
    if type(s) != list:
        return x == s
    elif len(s) != 1:
        return count(x, s[0]) + count(x, s[1:])
    else:
        return count(x, s[0])
    
    #if len(s) == 1:
    #    return s[0] == x
    #else:
    #    return (s[0] == x) + count(x, s[2:])




change = [1, 5, 10, 50, 100]


def vaxel(a, n):
    if a == 0:
        return 1
    elif((a < 0) or (n == 0)):
        return 0
    else:
        return vaxel(a, n-1) + vaxel(a-change[n-1], n)


def paren_mach(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

def power(x, n):
    if (n==0):
        return 1
    elif (n==-1):
        return 1/x
    else:
        p = power(x, n//2)
        if (n%2==0):
            return p*p
        elif n < 0:
            print('hej')
            return 1/x*p*p
        else:
            return x*p*p


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(count(4, [1, 4, 2, ['a', [ [ 4 ] , 3, 4] ] ]))



