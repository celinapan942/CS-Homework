import matplotlib
import random

data = []
total = 10
for i in range(0, 100):
    total += random.random() * 2 - 1
    data.append(total)

plot(data, 'b-')
show()