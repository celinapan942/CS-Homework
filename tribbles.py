from random import randint,triangular
from random import randint
import random
import math

population = 3
step = 12
time = 0
birthrate = 0.30
deathrate = 0.05
predator_rate = 0.01
starvation_rate_baseline = 0.15
current_starvation_rate = starvation_rate_baseline
x_coords = []
y_coords = []

for i in range (0,30):
    for j in range (0,population):
        if random.random()<birthrate: 
            population += int(triangular(1,15,10))
    for j in range (0,population):
        if random.random()<deathrate: 
            population -= 1 
    for j in range (0,population):
        if random.random()<predator_rate: 
            population -= 1  
    for j in range (0,population):
        if random.random() < current_starvation_rate: 
            population -= 1      
    current_starvation_rate = starvation_rate_baseline * math.log(population, 10)
    if population >1000:
        predator_rate += 0.001
    if population < 1000:
        predator_rate = 0.001
    x_coords.append(i*step)
    y_coords.append(population)
    
'''
plt.figure()
plt.plot(x_coords, y_coords)
plt.xlabel("Hours")
plt.ylabel("Population")
plt.title("Tribble population Growth")
plt.show()
'''

print (x_coords)
print (y_coords)
