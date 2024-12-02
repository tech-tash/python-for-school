# Program to draw a top-view turtle using turtle graphics
# Name: Natasha Mazibuko
# Date: 17 April 2024

import turtle

def main():
    
    #turtle setup
    turtle.shape("turtle")
    #turtle.mode("logo")
    turtle.speed(10)
    #turtle.bgcolor("pink")
    
    #head
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
       #new functions used to draw a circle and colour it black
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    
    turtle.penup()
    
    #ears
       #right ear
    turtle.goto(30, 130)   
    turtle.pendown()
       #draw circle with new functions
    turtle.color("darkolivegreen")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    
        #left ear
    turtle.goto(-30, 130) #right ear
    turtle.pendown()
       #draw circle and colour it in using new functions
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()        
    
    #legs
    turtle.pencolor("darkolivegreen")
    turtle.color("darkolivegreen")
    leg_position = [(-80, -50), (80, -50), (-100, 50), (100, 50)]
    for pos in leg_position:
        turtle.penup()
        turtle.goto(pos)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(30) #draw full circle for legs
        turtle.end_fill()
        
    #shell
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.color("green4")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(0, -20)
    turtle.pendown()
    turtle.color("darkgreen")
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()
    
    #circles on the shell
    turtle.color("darkolivegreen") #new colour
    shell_positions = [(0,50), (-50,0), (50,0), (0,-50)]
    for pos in shell_positions:
        turtle.penup()
        turtle.goto(pos)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()
    
    
    turtle.exitonclick()

main()    