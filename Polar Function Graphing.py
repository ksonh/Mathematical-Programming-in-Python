###
## This program generates a polar plane using Python's Turtles module, then 
## generates the rectangular coordinates for a circle, cardioid, or rose to 
## draw the shape.
## Designed by: Kenneth Hanson.
##

import turtle
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    turtle.delay(5)

    draw_axes(200)

    print("This program draws the graph of a circle, cardioid, or rose on a polar plane using the Turtles module. Click on screen to exit.")
    shape = input("Please enter the desired shape: ")

    acceptable_shapes = ["circle", "cardioid", "rose"]
    while shape.lower() not in acceptable_shapes:
        shape = input("Please enter the desired shape: ")

    if shape.lower() == "rose":
        n = input("Enter how many pedals you want for the rose (maximum is 6): ")
        if n.isdigit() == True and int(n) <= 6:
            plot(shape, 200, int(n))
        else:
            n = input("Enter how many pedals you want for the rose (maximum is 6): ")  
    elif shape.lower() == "circle":
        radius = input("Enter the radius for the circle: ")
        if radius.isdigit() == True:
            plot(shape, int(radius))
        else:
            radius = input("Enter the radius for the circle: ")
    else:
        plot(shape.lower(), 100)

    turtle.hideturtle()

    turtle.exitonclick()

## Draws a polar plane using Python's Turtles
## module showing the angles in degrees.
# @param radius the radius of the polar plane
def draw_axes(radius):
    FONT_SIZE = 8
    FONT = ("Courier", FONT_SIZE, "bold")

    width = radius * 2 + 100
    height = radius * 2 + 100

    turtle.title("Polar Plot")

    turtle.screensize(canvwidth=width, canvheight=height)
    turtle.setup(width=width + 30, height=height + 30)
    turtle.shape("classic")

    degree_label_radius = radius + 16

    turtle.pencolor("black")

    for degrees in range(0, 360, 15):

        radians = math.radians(degrees)

        turtle.penup()
        turtle.home()

        turtle.pendown()
        turtle.goto(math.cos(radians) * radius, math.sin(radians) * radius)

        turtle.penup()
        turtle.goto(math.cos(radians) * degree_label_radius,
                    math.sin(radians) * degree_label_radius)

        turtle.goto(turtle.position()[0], turtle.position()[1] - FONT_SIZE)

        turtle.pendown()
        #Writes the angle in degrees followed by the degree symbol.
        turtle.write(str(degrees) + u'\u00B0', align='center', font=FONT)

## Plots the shape entered by the user with
## the polar coordinates generated by the
## generate_coordinates helper function.
# @param shape the shape entered by the user
# @param radius the radius if it is a circle
# @param n the number of pedals if it is a rose
def plot(shape, radius, n=None):
    turtle.title(shape)

    turtle.pensize(2)
    turtle.pencolor(1.0, 0.0, 0.0)
    turtle.penup()

    rads = np.arange(0, (2 * np.pi), 0.01) 

    for degrees in range(0, 360 + 1):

        radians = math.radians(degrees)
        if shape == "rose":
            cords = generate_coordinates(str(shape), radians, radius, n=n)
        elif shape == "circle":
            cords = generate_coordinates(str(shape), radians, radius)
        else:
            cords = generate_coordinates(str(shape), radians, radius)
        turtle.goto(cords["x"], cords["y"])

        turtle.pendown()

## Returns a sequence of rectangular coordinates given by the
## polar-rectangular conversion formulas x = rcosθ and y = rsinθ.
# @param shape the shape entered by the user
# @param radians the angle in radians--or theta
# @param radius the radius of the circle
# @param n the number of pedals if it is a rose
# @return dictionary of x- and y-coordinates
def generate_coordinates(shape, radians, radius, n=None):
    if shape == "circle":
        return {"x": math.cos(radians) * radius, "y": math.sin(radians) * radius}
    elif shape == "cardioid":
        r = (1 + math.cos(radians)) * radius
        return {"x": math.cos(radians) * r, "y": math.sin(radians) * r}
    elif shape == "rose":
        r = math.sin(radians * n) * radius
        return {"x": math.cos(radians) * r, "y": math.sin(radians) * r}

if __name__ in '__main__':
    main()