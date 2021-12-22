import random
import matplotlib.pyplot as plt
import concurrent.futures as future


in_circle = 0
redx = []
redy = []
bluex = []
bluey = [] 
n = 1000000
for i in range(n):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)


    if x**2 + y**2 <= 1:
        in_circle += 1
"""""
        redx.append(x)
        redy.append(y)
    else:
        bluex.append(x)
        bluey.append(y)
"""""
#plt.plot(redx,redy, 'bo')
#plt.plot(bluex,bluey, 'ro')
#plt.show(block=True)
#print(4*in_circle/n) 