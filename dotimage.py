import turtle as turtle_module
import random
t=turtle_module
turtle_module.colormode(255)
tim=turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

colour=[(245, 248, 34), (55, 29, 15), (27, 34, 165), (248, 28, 66), (177, 7, 62), (146, 81, 49), (31, 251, 212), (235, 10, 219), (249, 228, 174), (4, 46, 19), (9, 16, 56), (58, 83, 195), (43, 227, 18), (199, 159, 115), (19, 147, 43), (249, 54, 20), (5, 110, 55), (196, 16, 9), (52, 7, 29), (230, 234, 8), (177, 148, 44), (69, 94, 229), (57, 231, 47), (251, 9, 30), (0, 253, 252), (90, 87, 12), (20, 247, 252), (218, 113, 184), (72, 160, 218), (253, 11, 9)]
#position of starting point
tim.setheading(225) # Point the turtle to the top-left corner
tim.forward(300) # Move the turtle to the starting position
tim.setheading(0) # Point the turtle to the right

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colour)) # Draw a dot with a random color from the list
    tim.forward(50) # Move the turtle forward to the next position

    if dot_count % 10 == 0: # After every 10 dots, move to the next row
        tim.setheading(90) # Point the turtle upwards
        tim.forward(50) # Move the turtle up to the next row
        tim.setheading(180) # Point the turtle to the left
        tim.forward(500) # Move the turtle back to the starting position of the new row
        tim.setheading(0) # Point the turtle to the right again
