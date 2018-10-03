count = 0
total = 0.2
a = 1
b = 2
count = 0
height = 0

#while count < 10:
    #print (count*10)
    #count  = count +1
    
while count < 26:
    total = total - 0.2
    print (total)
    count = count + 1
    
for i in range (0,5):
    a = b*a + i
print (a)

for i in range (0, 100):
    if i%3 == 0:
        None
    elif i%8 == 0:
        None
    else:
        print (i)
    
for height in range (0,5):
    if height == 1:
        print ("   *   ")
    elif height == 2:
        print ("  * * ")  
    elif height == 3:
        print (" *   * ")  
    elif height == 4:
        print ("*     *")    
    
for height in range (0,4):
    height = 4 - height 
    if height == 1:
        print ("   *   ")
    elif height == 2:
        print ("  * * ")  
    elif height == 3:
        print (" *   * ")  
    elif height == 4:
        print ("*     *")    