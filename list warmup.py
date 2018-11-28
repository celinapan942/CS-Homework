mylist = [] 

def question1 ():
    highest = int (0)
    highesttwo = int (0)    
    for i in range (0,5):
        number = int (input ("Please type in a number"))
        mylist.append (number)
    for n in range (len(mylist)):
        if mylist [n] > highest:
            highest = mylist[n] 
    for j in range (len(mylist)):
        if mylist [j] == highest:
            del mylist[j]
    for k in range (len(mylist)):
        if mylist [k] > highesttwo:
            highestwo = k
    print (highest, highesttwo)
    
question1 () 