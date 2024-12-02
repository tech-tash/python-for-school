# Program to decode South African identity (ID) numbers
# Name: Natasha Mazibuko
# Date: 07 May 2024

"""
ID = input("Please enter your ID number:\n")

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
    """



import turtle
def main():
 turtle.shape("turtle")
 turtle.mode("logo") 
 
 i, j = 0, 0
 
 while i <360:
  turtle.penup()
  turtle.forward(50)
  turtle.pendown()
  turtle.forward(50)
  turtle.penup()
  
  while j <36:
   turtle.right(j)
   turtle.forward(1)
   j += 1
  
  turtle.pendown()
  right(90)
  forward(50)
 
turtle.exitonclick()


main()