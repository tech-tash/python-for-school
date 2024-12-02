# Program to draw my own initials using turtle
# Name: Natasha Mazibuko
# Date: 17 April 2024

import turtle

def main():
 turtle.shape("turtle")
 turtle.mode("logo")
 
 turtle.title("N.M")
 
 turtle.penup()        #move from the centre
 turtle.left(90)
 turtle.forward(220)
 turtle.right(90)
 
 turtle.pencolor("magenta")
 turtle.pendown()     #draw 'N'
 turtle.forward(200)
 turtle.right(135)
 
 turtle.forward(282)
 
 turtle.left(135)
 turtle.forward(200)
 
 
 turtle.penup()           #space between 'N' and 'M'
 turtle.right(90)
 turtle.forward(50)
 turtle.right(90)
 turtle.forward(200)
 turtle.pendown()
 
 turtle.pencolor("green")
 turtle.backward(200)    #draw 'M'
 turtle.left(45)
 turtle.forward(141)
 turtle.left(95)
 turtle.forward(141)
 turtle.right(140)
 turtle.forward(200)
 
 turtle.exitonclick()
 
main()