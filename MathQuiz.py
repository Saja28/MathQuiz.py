import random
import time
seconds = time.time()
local_time = time.ctime(seconds)
print("Local time:", local_time)
score = 0
loop= 0
set_second = 7
count_loop =5
while loop< count_loop:
    loop += 1
    print("yor currently score is:", score)

    
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    oper= ("+", "-",  "*")
    operator = random.choice(oper)

    if operator == '+' :
        z= x+y
    elif operator == "-":
        z= x-y
    elif operator == "*":
        z= x*y
    
    start_time = time.time()
    m =  int(input("What is {} {} {} =".format(x,operator, y)))
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < set_second :
        if m == z  :  
            score = score +1 
            
        elif  m != z  :
            score = score -1
            #if score<=4:
                #print("loser")  
    else:
        print("you wast your time!")
       
if score >= 4 :
    print ("you are winner!") 
else:
                print("loser")  


    

        
            

    



