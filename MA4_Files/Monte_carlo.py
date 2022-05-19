import random
import matplotlib.pyplot as plt
in_circle = 0
redx = []
redy = []
bluex = []
bluey = [] 
n = 100000
for i in range(n):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)


    if x**2 + y**2 <= 1:
        in_circle += 1
        redx.append(x)
        redy.append(y)
    else:
        bluex.append(x)
        bluey.append(y)

plt.plot(redx,redy, 'bo')
plt.plot(bluex,bluey, 'ro')
plt.savefig('pi100000.png')
plt.show()

print(4*in_circle/n) 
"""""
n = 1000 --> pi = 3.092
n = 10000 --> pi = 3.1488
n = 100000 --> pi = 3.13964
"""""