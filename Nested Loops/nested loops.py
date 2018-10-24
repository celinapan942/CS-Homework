for i in range (0,5):
    print ()
    for j in range (0,10):
        print ("*", end= " ")

print ("\nQuestion2")
counter = 5
for i in range (1,11,2):
    print (" "*counter,end = " " )
    print ("*"*i)
    counter = counter -1

print ("\nQuestion3")
length = 7
for i in range (0,length):
    if i == 0 or i == length -1:
        print ("*"*length)
    if i == 1 or i == length - 2:
        print (2*"*", )

