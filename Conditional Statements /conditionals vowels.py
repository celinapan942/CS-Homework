string1 = "eoiou"
string2 = "aria"
string3 = "sdf"
num1 = 3.4
num2 = 3

def function(string):
    if string.count("a")>=1 and string.count("e")>= 1 and string.count("i")>= 1 and string.count("o")>=1 and string.count("u")>=1:
        print (string, "contains all five values.")
    elif string.count("a")>=1 or string.count("e")>= 1 or string.count("i")>= 1 or string.count("o")>=1 or string.count("u")>=1:
        print (string, "contains some vowels")
    else:
        print(string, "contains no vowels.")
        
function (string1)
function (string2)
function (string3)

def easy(num):
    if type(num) == int:
        print (num, "is an integar")
    else:
        print (num,"is not an integar")
        
easy (num1)
easy(num2)