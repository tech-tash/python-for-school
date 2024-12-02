# Program that can calculate the class to which a vehicle belongs.
# Name: Natasha Mazibuko
# Date: 10 May 2024

vehicleGVM = int(input("What is the gross vehicle mass (in kg)?\n"))
trailer = input("Does the vehicle have a trailer?\n")

if trailer == "y" or trailer == "yes":
    trailerGVM = int(input("What is the gross vehicle mass of the trailer (in kg)?\n"))
    
    if vehicleGVM <= 3500 and trailerGVM > 750:
        print("This vehicle is class EB.")
    
    elif vehicleGVM <= 3500:
        print("This vehicle is class B.")
        
    if 3500 < vehicleGVM <= 16000 and trailerGVM > 750:
        print("This vehicle is class EC1.")
        
    elif 3500 < vehicleGVM <= 16000:
        print("This vehicle is class C1.")
        
    if vehicleGVM > 16000 and trailerGVM > 750:
        print("This vehicle is class EC.")
        
    elif vehicleGVM > 16000:
        print("This vehicle is class C.")
        
  
elif trailer == "n" or trailer == "no":
    articulated = input("Is the vehicle articulated?\n")
    
    if articulated == "y" or articulated == "yes":
        if vehicleGVM <= 3500:
            print("This vehicle is class EB.")
            
        elif 3500 < vehicleGVM <= 16000:
            print("This vehicle is class EC1.")
            
        elif vehicleGVM > 16000:
            print("This vehicle is class EC.")   
            
    elif articulated == "n" or articulated == "no":
        if vehicleGVM <= 3500:
            print("This vehicle is class B.")
            
        elif 3500 < vehicleGVM <= 16000:
            print("This vehicle is class C1.")
            
        elif vehicleGVM > 16000:
            print("This vehicle is class C.")          
    