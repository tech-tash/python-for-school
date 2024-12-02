import math

def circle_area(diameter):
    # Your code here
    return ((1/4) * math.pi * diameter ** 2) 

def cylinder_volume(diameter, height):
    # Your code here
    return (circle_area(diameter) * height)

def main():
    # Your code here
    diameter = eval(input("Enter diameter:\n"))
    height = eval(input("Enter height:\n"))
    
    print("The volume of the cylinder is {:.2f}".format(cylinder_volume(diameter, height)))

if __name__=='__main__':
    main()
