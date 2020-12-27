import random
import matplotlib.pyplot as plt

list = [0] * 101

for i in range(100000):
    x = random.randint(0, 100)
    list[x] += 1

print(list)

plt.plot(range(101), list)
plt.show()
