#Question1: 34, 16, 27, 53

a = 10
b = 20
c = 30

#Question2
def foo1 (a,b):
    global b
    a = b +c
    print (b)
 
#Question3   
def add (num1, num2):
    return num1 + num2

def triple (num):
    return add (num, add(num, num))

def quadruple (num):
    return add (num, triple (num))
