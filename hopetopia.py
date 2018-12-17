import matplotlib
import random
import math

step = 1
males = 84
females = 91
population = 175
birth_rate = 0.6*0.3
chance_of_girl = 0.5
chance_of_boy = 0.5
death_rate = 0.05

x_coords = []
y_coords = []
area = 80

for i in range (0,100):
    for j in range (0,females):
        if random.random()<birth_rate: 
            if random.random()<chance_of_girl:
                females += 1
            else:
                males += 1 
    for j in range (0,population):
        if random.random() < death_rate:
            if random.random() < (91/175):
                females -= 1
            else:
                males -= 1
    
    population = males +females
    x_coords.append(i*step)
    y_coords.append(population)    
    
print (x_coords)
print (y_coords)
print ("Therefore it takes around 45 years for the population to become over 800 and around 50 for it to exceed 1000. You can tell this from the scatter plot.")

plt.scatter (x_coords,y_coords,s=area, color="blue", alpha = 0.5)
plt.show()
