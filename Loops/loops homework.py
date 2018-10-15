import random

ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

#Question 1
counter = -3

while counter <9:
    print (counter)
    counter = counter +1 

for i in range (-3,9):
    print (i)
    
#Question 2
def is_odd(number):
    if number%2 != 0:
        return True
    if number%2 == 0:
        return False 
    
for n in range (1,11):
    if is_odd(n) == True:
        print ("The number is odd")
    if is_odd(n) == False:
        print ("The number is even")   

#Question 3
rolls = input ("How many times should the dice be rolled?")

for i in range (0,rolls):
    dice = random.randint (1,6)
    if dice == 1:
        ones = ones +1
    if dice == 2:
        twos = twos +1    
    if dice == 3:
        threes = threes +1
    if dice == 4:
        fours = fours +1        
    if dice == 5:
        fives = fives +1        
    if dice == 6:
        sixes = sixes +1   

print ("There were: ", ones, " ones, ", twos, " twos, ", threes, " threes, ", fours, " fours, ", fives, " fives, ", sixes, " sixes.")

#Question 4 

def question4(numberasstring):
    noofeven = numberasstring.count("2") + numberasstring.count("4")+ numberasstring.count("6") + numberasstring.count("8") + numberasstring.count("0")
    print ("The number has: ", noofeven, " even numbers.")
    noofodd = numberasstring.count("1") + numberasstring.count("3")+ numberasstring.count("5") + numberasstring.count("7") + numberasstring.count("9")
    print ("The number has: ", noofodd, " odd numbers.")    

number = raw_input ("Please type in a number")
question4(number)
