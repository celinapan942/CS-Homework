import math
radius = 0
volume = 0
area = 0


def question1(a, b):
    if a%b == 0:
        print (int(a // b))
    else:
        print (int(a//b), int(a%b),'/', b)

variable1 = input("Please input a number")
variable2 = input("Please input another number")

question1(variable1, variable2)





def vowel_count1 (string):
    print ("the number of As is: ", string.count("a"))
    print ("the number of Es is: ", string.count("e"))
    print ("the number of Is is: ", string.count("i"))
    print ("the number of Os is: ", string.count("o"))
    print ("the number of Us is: ", string.count("u"))

def vowel_count2 (string):
    print ("the number of vowels is: ",(string.count("a")+string.count("e")+string.count("i")+string.count("o")+string.count("u")))


def vowel_count3 (string):
    return string.count("a"), string.count("e"), string.count("i"), string.count("o"), string.count("u")

string1 = raw_input("please type in a word")

vowel_count1(string1)
vowel_count2(string1)






def volumeofsphere(radius):
    return(4*math.pi*(radius**3)/3)

def areaofsphere(radius):
    return(4*math.pi*(radius**2))

def printva():
    print ("The volume of the sphere is: ",volumeofsphere(r))
    print ("The surface area of the sphere is: ",areaofsphere(r))

r = input("Please input the radius of the sphere")

volumeofsphere(r)
areaofsphere(r)
printva()


def info():
    name = raw_input ("What is the person's name?")
    weight = input ("What is the person's weight")
    age = input("What is the person's age?")

info()




def converttohex(binarycode):
    print (hex(binarycode))

def converttobin(hexcode):
    print(bin(int(hexcode, 16))[2:])

rgbbin = input("What is the RGB color in binary numbers?")
converttohex(rgbbin)

rgbhex = str(raw_input("What is the RGB color in hex?"))
converttobin(rgbhex)