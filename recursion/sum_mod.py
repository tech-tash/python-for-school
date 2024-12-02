# Program with function that will recursively sum the values from 1 to n for an integer n. 
# Name: Natasha Mazibuko
# Date: 31 August 2024

def sum_to_n(n):
    if n == 1:
        return 1
    
    else:
        return n + sum_to_n(n-1)