# Program that displays a multiplication table
# Name: Natasha Mazibuko
# Date: 10 May 2024

n1 = input("Enter a value for n (not greater than 30):\n")

if n1.isdigit() == False:
    print("Sorry, n must be an integer number in the range 1 to 30.")
    
elif int(n1) > 30 or int(n1) < 1:
    print("Sorry, n must be an integer number in the range 1 to 30.")
    
else:
    
    n = int(n1)
    
    print("Table from {} to {}:".format(n,n+10))
    print("{:3}|".format("*"), end ="")
    
    for i in range(n, n+10):
        print("{:4}".format(i), end = "")
    
    print()    
        
    for i in range(44):
        print("-", end ="" )
    
    print()
    
    print("{:<3}|".format(n), end = "")
    for i in range(n, n+10):
        print("{:4}".format(i*n), end = "")
    
    print()
    
    print("{:<3}|".format(n+1), end = "")
    for i in range(n, n+10):
        print("{:4}".format(i*(n+1)), end = "")
        
    print()
    
    print("{:<3}|".format(n+2), end = "")
    for i in range(n, n+10):
        print("{:4}".format(i*(n+2)), end = "")
        
    print()
    
    print("{:<3}|".format(n+3), end = "")
    for i in range(n, n+10):
        print("{:4}".format(i*(n+3)), end = "")
        
    print()
    
    print("{:<3}|".format(n+4), end = "")
    for i in range(n, n+10):
        print("{:4}".format(i*(n+4)), end = "")
        
    print()
    
    print("{:<3}|".format(n+5), end = "")
    for i in range(n, n+10):
        print("{:4}".format(i*(n+5)), end = "")
        
    print()
    
    print("{:<3}|".format(n+6), end = "")
    for i in range(n, n+10):
        print("{:4}".format(i*(n+6)), end = "")
        
    print()
    
    print("{:<3}|".format(n+7), end = "")
    for i in range(n, n+10):
        print("{:4}".format(i*(n+7)), end = "")
        
    print()
    
    print("{:<3}|".format(n+8), end = "")
    for i in range(n, n+10):
        print("{:4}".format(i*(n+8)), end = "")
        
    print()
    
    print("{:<3}|".format(n+9), end = "")
    for i in range(n, n+10):
        print("{:4}".format(i*(n+9)), end = "")    