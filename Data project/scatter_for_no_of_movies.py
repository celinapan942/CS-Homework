import pickle 
import matplotlib.pyplot as plt
from random import random

number = {}

with open("dictionary1.pickle","wb")as f:
    pickle.dump(dictionary1,f)

with open("dictionary1.pickle","rb")as f:
    number = pickle.load(f)
    
x = []
y = []
area = 80
colors = []

for i in number:
    x.append(i)
    y.append(number[i])
    colors.append(random()*50)
    
plt.scatter (x,y,s=area, c=colors, alpha = 0.5)
plt.show()