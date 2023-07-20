# Turtle Party Project
# by Sarah Vincent
# 7/20/2023

import turtle

r=0        # These variables control color (0, 50, 255) for blue
g=50
b=255

turtle.shape("turtle")   # optional
turtle.speed(5)         # optional
turtle.width(3)
turtle.pencolor(r,g,b)

# Polygon Function
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360/num)

# Move across the page
def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def left(len):
  turtle.penup()
  turtle.left(len)
  turtle.pendown()
  
def forward(len):
  turtle.penup()
  turtle.forward(len)
  turtle.pendown()

# Dark red square
turtle.pencolor(139,0,0)
polygon(4, 90)
forward(100)

# Blue grey triangle
turtle.pencolor(115, 147, 179)
polygon(3, 50)
back(150)
left(180)

# Blue green square
turtle.pencolor(8, 143, 143)
polygon(4, 75)

turtle.Screen().exitonclick()
