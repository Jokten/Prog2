#!/usr/bin/env python3.9
from cProfile import label
from time import perf_counter as pc
from person import Person
from numba import njit
import matplotlib.pyplot as plt
def main():
	py = []
	num = []
	c = []
	for i in range(30, 46):
		start = pc()
		fib_py(i)
		end = pc()
		fib2_py(i)
		end2 = pc()
		f = Person(i)
		f.fib()
		end3 = pc()
		py.append(end-start)
		num.append(end2-end)
		c.append(end3-end2)
		print(i)
	x = list(range(30,46))
	plt.plot(x,py,label='py')
	plt.plot(x,num,label='numba')
	plt.plot(x,c,label='c')
	plt.legend()	
	plt.savefig('time.png')
	print(fib2_py(47))
	ff = Person(47)
	print(ff.fib())
	
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
