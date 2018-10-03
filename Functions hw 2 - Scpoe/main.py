import module1
import math

def say_hello(name):
    print ("You smell bad", name)
    
def sqrt():
    print ("......")

print(module1.var1)

module1.say_hello("Aria")

from module1 import say_hello

say_hello("Aria")

print (math.ceil(3.5))
print (math.isnan(3))
print (math.modf(3.5))
print (math.pow(2,3))
print (math.sin(0))

from math import sqrt

print (sqrt(4))