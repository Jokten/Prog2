"""
Solutions to module 1
Student: 
Mail:
Reviewed by:
Reviewed date:
"""

import math
import random
import time



def power(x, n):         # Optional
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)



def multiply(m, n):      # Compulsory
    if m > n:
        a, b = m, n
    else:
        a, b = n, m
    if b == 0:
        return 0
    if b == 1:
        return a
    else:
        return a + multiply(a, b - 1)


def divide(t, n):        # Optional
    if t - n < 0:
        return 0
    else:
        return 1 + divide(t - n, n)


def harmonic(n):         # Compulsory
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic(n - 1)

def digit_sum(x):        # Optional
    pass


def get_binary(x):       # Optional
    pass


def reverse(s):          # Optional
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])



def largest(a):          # Compulsory
    if len(a) == 1:
        return a[0]
    elif a[0] > largest(a[1:]):
        return a[0]
    else:
        return largest(a[1:])


def count(x, s):         # Compulsory
    a, b = 0, 0
    if s[0] == x:
      a = 1  
    elif type(s[0]) == list:
        a = count(x, s[0])
    if len(s) > 1:
        b = count(x, s[1:])
    return a + b
    
    #if len(s) == 1:
    #    return s[0] == x
    #else:
    #    return (s[0] == x) + count(x, s[2:])

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def zippa(l1, l2):       # Compulsory
    if len(l1) == 1:
        return l1 + l2
    else:
        return [l1[0]] + zippa(l2,l1[1:])



def bricklek(f, t, h, n): # Compulsory
    if n == 1:
        return [f'{f}->{t}']
    else:
        return bricklek(f, h, t, n-1) + [f'{f}->{t}'] + bricklek(h, t, f, n-1)

def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    start = time.time()
    fib(20)
    time2 = time.time()
    fib(30)
    time3 = time.time()
    print(math.log((time3-time2)/(time2-start),1.618))
    print(time3-time2)
    print('Bye!')
    

if __name__ == "__main__":
    main()
    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  
  2**50 - 1 = 1125899906842623 seconds = 35 702 051 years
  
  
  
  
  Exercise 17: Time for Fibonacci:
  a) Code in main
  b) 0.26986026763916016*1.618**20 = 4080 seconds
  0.26986026763916016*1.618**70 = 114718948085697 seconds

  
  
  
  
  Exercise 20: Comparison sorting methods:
  For 10^6:
  1000 times larger input --> 1000^2 = 1 000 000 sec = 11.6 days for insertion
                          --> 1000*log1000 = 3*1000 = 3000 seconds = 50 minutes for mergesort
For 10^9:
  10^6 times larger input --> (10^6)^2 = 10^12 sec > 31 000 years for insertion
                          --> 10^6*log10^6 = 6*10^6 = 6 000 000 seconds = 69 days for mergesort
  
  
  
  
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  
  
  
  
  
  
  





"""