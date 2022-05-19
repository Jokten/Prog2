import functools
from math import pi, gamma
from random import uniform
import concurrent.futures as future
from time import perf_counter as pc

def V(d):
    return (pi**(d/2))/(gamma((d/2)+1)) # Antar r = 1

def approx(n,dim):
    return (2**dim)*len(list(filter(lambda x: x < 1,[sum([uniform(-1,1)**2 for i in range(dim)]) for j in range(n)])))/n

if __name__ == '__main__':
    # Del 1
    print(approx(100000,2)) # 3.13892
    print(approx(100000,11)) # 1.9456
    start = pc()
    with future.ProcessPoolExecutor() as ex:
        result = ex.map(approx, [1000000]*10, [11]*10)
        print(sum(result)/10)
    start2 = pc()
    print(approx(10000000,11))
    end = pc()
    print(f'MP took {start2-start} seconds')
    print(f'SP took {end-start2} seconds')