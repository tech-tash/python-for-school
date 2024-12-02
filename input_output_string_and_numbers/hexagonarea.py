# Program to calculate and print the area of a regular hexagon
# Name: Natasha Mazibuko
# Date: 17 April 2024

from math import sqrt         #do not have to import the whole math thing

def main():
 side = eval(input("Enter the length of the side (cm):\n"))

 area = (3 * sqrt(3) * side ** 2)/2
 rounded_area = round(area, 3)         #round to 3 decimal places
 print_area = str(rounded_area)        #convert to string to able to add "." when printing oukt 

 print("The area of a hexagon of side {} is {:.3f}.".format(side, rounded_area))
 
main() 