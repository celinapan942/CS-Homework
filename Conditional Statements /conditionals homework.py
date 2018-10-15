import math
import random

# Question 1 
def question1 (age):
    if age > 18:
        print ("Old enough to drive")
    elif age < 18:
        print ("Not old enough to drive")
        
age = input("Please type in an age.")
question1(age)

# Question 2
def question2 (a,b,c):
    try: 
        anglea = math.acos(float(a**2-b**2-c**2)/float(-2*b*c))
        angleb = math.acos(float(b**2-a**2-c**2)/float(-2*a*c))
        anglec = math.acos(float(c**2-a**2-b**2)/float(-2*a*b))
        ninety = math.pi / 2 
        if anglea < ninety and angleb < ninety and anglec < ninety:
            print ("The triangle is acute")
        elif anglea == ninety or angleb == ninety or anglec == ninety:
            print ("The triangle is a right angle")
        elif anglea > ninety or angleb > ninety or anglec >ninety:
            print ("This is an obtuse tirangle")
    except:
        print ("This is not a triangle")
    
sidea = input ("Please input the length of the first side")
sideb = input ("Please input the length of the second side")
sidec = input ("Please input the length of the third side")

question2(sidea, sideb, sidec)

# Question 3

def question3 (number):
    if number%3 == 0 and number%5 != 0: 
        print ("FIZZ!")
    elif number%3 != 0 and number%5 ==0:
        print ("BUZZ!")
    elif number%3 == 0 and number %5 ==0:
        print ("FIZZBUZZ!")
    else:
        print ("Huh?")
        
number = input("Please input a number")
question3 (number)
      
#Question4

def question4 (n,r):
    numberofc = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
    if numberofc >1000000:
        print ("You have no chance")
    elif numberofc > 10000 and numberofc <1000000:
        print ("*much encouragement*")
    elif numberofc < 1000:
        print ("It's possible")

nquestion = input ("How many possibilities are there?")
rquestion = input ("How many possibilities will be chosen?")

question4(nquestion,rquestion)

# Question 5

print(random.random())
print(random.randint(-10, 10))

def question5(name):
    number = random.randint(-10, 10)
    print (number)
    if number < -8:
        print (name, ", You are an idiot")
    elif number < -6 and number > -8:
        print (name, ", You are stupid")
    elif number < -4 and number > -6:
        print (name, ", You are smart")        
    elif number < -2 and number > -4:
        print (name, ", You are kind") 
    elif number < 0 and number > -2:
        print (name, ", You are brave")
    elif number < 2 and number > 0:
        print (name, ", You are selfish")        
    elif number < 4 and number > 2:
        print (name, ", You are a failure") 
    elif number < 6 and number > 4:
        print (name, ", You are a good friend")
    elif number < 8 and number > 6:
        print (name, ", You are annoying")        
    elif number < 10 and number > 8:
        print (name, ", You are ressilient")     
        
user = raw_input("What is your name?")
question5(user)

# Question 6

def question6(guess1, guess2, guess3):
    roll1 = random.randint (1,6)
    roll2 = random.randint (1,6)
    roll3 = random.randint (1,6)
    counter = 0
    if guess1 == roll1:
        counter  = counter + 1 
    if guess2 == roll2:
        counter = counter + 1
    if guess3 == roll3:
        counter = counter + 1
    print ("You got: ", counter, " right guesses.")
     
userguess1 = input ("What is your guess for dice 1?") 
userguess2 = input ("What is your guess for dice 2?")
userguess3 = input ("What is your guess for dice 3?")

question6(userguess1, userguess2, userguess3)