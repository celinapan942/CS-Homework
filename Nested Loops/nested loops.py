length = 0
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

length = int(input ("What is the length of the square?"))
width = length
for i in range (1, length+1):
    print ()   
    for n in range (1,width+1):  
        if i == 1 or i == length or n == 1 or n == width:
            print ("*", end = " " )
        if i == n and i +n <=length +1 :
            print ("*", end = " " )
        if i > n and i >length/2 and i + n == length +1 and i != n:
            print ("*", end = " ") 
        if i < n and i < length/2 and i + n == length and i != n:
            print ("*", end = " ") 
        if i + n > length +1 and i == n +1:
            print ("*", end = " ")
        else: 
            print("", end = " " )     
    
