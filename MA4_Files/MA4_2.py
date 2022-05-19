#!/usr/bin/env python3.9
from time import perf_counter as pc
from person import Person
from numba import njit
def main():
	f = Person(5)
	print(f.get())
	f.set(4)
	print(f.fib())
	start = pc()
	fib_py(17)
	end = pc()
	print(fib2_py(47))
	end2 = pc()
	f = Person(47)
	print(f.fib())
	end3 = pc()

	print(end-start)
	print(end2-end)
	print(end3-end2)

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

@njit
def fib2_py(n):
	if n <= 1:
		return n
	else:
		return(fib2_py(n-1) + fib2_py(n-2))

if __name__ == '__main__':
	main()
