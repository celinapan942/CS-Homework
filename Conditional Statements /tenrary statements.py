import math

a = 10
b = 2
number1 = 144
number2 = 9
number3 = 100
string1 = "aria"
string2 = "4d8jss"

print ("Yes") if a < b else ("No")

def easy (number):
    if math.sqrt(number) < 5 or math.sqrt (number) >10:
        print ("the square root is smaller than 5 or the square root is larger than 10")
    elif math.sqrt(number) == 10:
        print ("the square root is equal to 10.")
        
easy(number1)
easy(number2)
easy(number3)

def hard (string):
    if len (string) <30 and string.isalpha() == True:
        print ("Vlid name")
    else:
        print ("Invalid. More than 30 or has numbers")

hard (string1)
hard (string2)
    

