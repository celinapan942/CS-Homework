import random

q1first = [1,2,3]
q1second = [1,2,6]
q1three = [6,2,1]
q6 = [1, 1, 13, 4, 5]
q9  = ["Hi", "HI", 9, 9, 0]
'''
def question1 (ls):
                if ls[0] == 6 or ls [len(ls)-1] == 6:
                                print ("True")
                else: 
                                print ("False")

question1(q1first)


def question2 (ls):
                first = ls[0]
                second = ls[1]
                third = ls[2]
                lsreverse = []
                lsreverse.append(third)
                lsreverse.append(second)
                lsreverse.append(first)
                print (lsreverse[0:])
        
question2(q1first)

def question3(ls):
                first = ls[0]
                last = ls[len(ls)-1]
                newlist = []
                newlist.append(first)
                newlist.append (last)
                print (newlist[0:])
    
question3(q1first)

def question4 (ls):
                for i in range (0, len(ls)):
                                if ls[i] == 2 or ls[i] == 3:
                                                flag = 1
                                else: 
                                                flag = 0
                if flag == 1:
                                print ("True")

question4(q1first)

def question5(ls):
                count = 0
                for i in range (0, len(ls)):
                                if ls[i]%2 == 0:
                                                count +=1
                print (count)
                
question5(q1first)

def question6(ls):
                add = 0
                for i in range (0, len(ls)):
                                if ls[i]  == 13:
                                                ls[i] = 0
                                                ls[i+1] = 0
                for i in range (0,len(ls)):
                                add += ls[i]
                print (add)
                 
question6(q6)
       
def question7(ls):
                total = 0
                highest = 0
                lowest = 1000
                for i in range (0, len(ls)):
                                if ls[i] > highest:
                                                highest = ls[i]
                for i in range (0, len(ls)):
                                if ls[i] < lowest:
                                                lowest = ls[i]         
                for i in range (0, len(ls)):
                                if ls[i]  == highest:
                                                ls.pop(i)               
                for i in range (0, len(ls)-1):
                                if ls[i] ==  lowest:
                                                ls.pop(i)             
                for i in range (0, len(ls)):
                                total += ls[i]
                print(total/len(ls))
                
question7(q1first)
'''
#def question8(ls):

          
def question9(ls):
                ls = list(set(ls))
                print(ls[0:])               

question9(q9)

def question10(ls):
                pointlist = []
                for i in range (0,10):
                                coordinate = tuple(str((random.randint(-100,100), random.randint(-100,100), random.randint(-100,100))))
                                pointlist.append(coordinate)
                print (pointlist[0:])
                