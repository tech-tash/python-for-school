# Program that asks the user to input their ID number, and checks details
# Name: Natasha Mazibuko
# Date: 11 May 2024

ID = input("Please enter your ID number:\n")
length = len(ID)

sum_ODD = 0
sum_EVEN = 0

if length == 13 and ID.isdigit():
    for i in range(11, 0, -2):
        d = int(ID[i])
        sum_ODD += d
        
    #print(sum_ODD)    
            
    for i in range(0, 13, 2):
        k = int(ID[i])
        p = k*2
        
        if p < 9:
            sum_EVEN += p
            
        else:
            b = str(p)
            c = len(b)
            
            for j in range(c):
                m = int(b[j])
                sum_EVEN += m
                
    #print(sum_EVEN)            
        
    if (sum_EVEN + sum_ODD) % 10 == 0:
        day = ID[4:6]
        month = ID[2:4]
        year = ID[0:2]
        
        print("Your date of birth is " + day + "/" + month + "/" + year + ".")
        
        if 0000 <= int(ID[6:10]) <= 4999:  
            print("You are female.")
            
        elif 5000 <= int(ID[6:10]) <= 9999:
            print("You are male.")
            
        if ID[10] == "0":
            print("You are a South African citizen.")
            
        elif ID[10] == "1":
            print("You are a permanent resident.")    
            
    else:
        print("Invalid ID number.")    
    
else:
    print("Invalid ID number.")    


  