# Programmer: Ansh Patel
# Title: Christmas Theme Image
# Description: Creates a wonderful merry christmas image with a colourful house, christmas tree (with gifts), snowman, and snowflakes!

from turtle import *

import turtle as t

import math

t.bgcolor("turquoise")
t.shapesize(1,1)
t.speed(10)
t.title("Merry Christmas!")

# MERRY CHRISTMAS!

t.penup()

t.goto(-450,275)
t.pendown()
t.pensize(5)
t.pencolor("red")
t.write("MERRY CHRISTMAS!", font=("Century Gothic",75))

t.pensize(1)
t.pencolor("black")

# MAKING A CHRISTMAS TREE

t.fillcolor("brown")

t.penup()

t.goto(-110,-279)

t.pendown()

t.begin_fill()

for count in range(2):
    t.fd(18)

    t.lt(90)

    t.fd(18*3)

    t.lt(90)

t.end_fill()

t.penup()

t.goto(-100,-225)

t.fillcolor("dark green")

t.pendown()

t.begin_fill()

t.lt(180)

t.fd(130)

t.rt(130)

t.fd(math.sqrt(65**2 + 105**2)/1.5)

t.lt(130)

for count in range(3):
    t.fd(65/1.5)

    t.rt(130)

    t.fd(math.sqrt(65**2 + 105**2)/1.5)

    t.lt(130)

t.fd(65/1.5)

t.rt(130)

t.fd(math.sqrt(109**2 + (105*(109/65))**2)/1.5)

t.rt(100)

t.fd(math.sqrt(109**2 + (105*(109/65))**2)/1.5)

t.rt(130)

t.fd(65/1.5)

for count in range(3):
    t.lt(130)

    t.fd(math.sqrt(65**2 + 105**2)/1.5)

    t.rt(130)

    t.fd(65/1.5)

t.lt(130)

t.fd(math.sqrt(65**2 + 105**2)/1.5)

t.rt(130)

t.fd(130)

t.end_fill()

t.penup()

t.goto(-70,75)

t.pendown()

t.fillcolor("yellow")

t.begin_fill()

t.circle(10)

t.end_fill()

t.penup()

t.goto(-133,75)

t.pendown()

t.fillcolor("red")

t.begin_fill()

t.circle(10)

t.end_fill()

t.penup()

t.goto(-133,0)

t.pendown()

t.fillcolor("blue")

t.begin_fill()

t.circle(10)

t.end_fill()

t.penup()

t.goto(-70,0)

t.pendown()

t.fillcolor("dark orange")

t.begin_fill()

t.circle(10)

t.end_fill()

t.penup()

t.goto(-70,-60)

t.pendown()

t.fillcolor("spring green")

t.begin_fill()

t.circle(10)

t.end_fill()

t.penup()

t.goto(-133,-60)

t.pendown()

t.fillcolor("yellow")

t.begin_fill()

t.circle(10)

t.end_fill()

t.penup()

t.goto(-133,-120)

t.pendown()

t.fillcolor("red")

t.begin_fill()

t.circle(10)

t.end_fill()

t.penup()

t.goto(-70,-120)

t.pendown()

t.fillcolor("blue")

t.begin_fill()

t.circle(10)

t.end_fill()

t.penup()

t.goto(-70,-180)

t.pendown()

t.fillcolor("dark orange")

t.begin_fill()

t.circle(10)

t.end_fill()

t.penup()

t.goto(-133,-180)

t.pendown()

t.fillcolor("spring green")

t.begin_fill()

t.circle(10)

t.end_fill()

# MAKING GIFTS

t.penup()

t.fillcolor("red")

t.goto(-220,-300)

t.pendown()

t.begin_fill()

for count in range(4):
    t.fd(50)
    t.lt(90)

t.rt(150)
t.fd(35)
t.lt(150)
t.fd(50)
t.lt(30)
t.fd(35)
t.lt(150)
t.fd(50)
t.rt(90)
t.fd(50)
t.lt(120)
t.fd(35)
t.lt(60)
t.fd(50)

t.end_fill()

t.penup()

t.goto(-220,-300)

t.lt(90)

t.pendown()
t.fillcolor("yellow")

t.fd(25-12.5/2)
t.rt(150)
t.begin_fill()
t.fd(35)
t.lt(150)
t.fd(12.5)
t.lt(30)
t.fd(35)
t.lt(60)
t.fd(50)
t.lt(90)
t.fd(12.5)
t.lt(90)
t.fd(50)
t.rt(90)
t.end_fill()

t.fd(25-12.5/2)
t.lt(30)
t.fd((17.5-8.75/2))
t.lt(150)
t.begin_fill()
t.fd((25-12.5/2))
t.rt(150)
t.fd(8.75)
t.lt(150)
t.fd(12.5)
t.lt(30)
t.fd(8.75)
t.lt(150)
t.fd(12.5)
t.lt(180)
t.fd((50-(25-12.5/2)))
t.rt(150)
t.fd(8.75)
t.rt(30)
t.fd(50)
t.rt(90)
t.fd(50)
t.rt(60)
t.fd(8.75)
t.rt(120)
t.fd(50)
t.end_fill()

t.penup()

t.fillcolor("light pink")

t.goto(-100,-320)

t.lt(90)

t.pendown()

t.begin_fill()

for count in range(4):
    t.fd(50)
    t.lt(90)

t.rt(150)
t.fd(35)
t.lt(150)
t.fd(50)
t.lt(30)
t.fd(35)
t.lt(150)
t.fd(50)
t.rt(90)
t.fd(50)
t.lt(120)
t.fd(35)
t.lt(60)
t.fd(50)

t.end_fill()

t.penup()

t.goto(-100,-320)

t.lt(90)

t.pendown()
t.fillcolor("blue")

t.fd(25-12.5/2)
t.rt(150)
t.begin_fill()
t.fd(35)
t.lt(150)
t.fd(12.5)
t.lt(30)
t.fd(35)
t.lt(60)
t.fd(50)
t.lt(90)
t.fd(12.5)
t.lt(90)
t.fd(50)
t.rt(90)
t.end_fill()

t.fd(25-12.5/2)
t.lt(30)
t.fd((17.5-8.75/2))
t.lt(150)
t.begin_fill()
t.fd((25-12.5/2))
t.rt(150)
t.fd(8.75)
t.lt(150)
t.fd(12.5)
t.lt(30)
t.fd(8.75)
t.lt(150)
t.fd(12.5)
t.lt(180)
t.fd((50-(25-12.5/2)))
t.rt(150)
t.fd(8.75)
t.rt(30)
t.fd(50)
t.rt(90)
t.fd(50)
t.rt(60)
t.fd(8.75)
t.rt(120)
t.fd(50)
t.end_fill()

t.penup()

t.fillcolor("orange")

t.goto(20,-300)

t.lt(90)

t.pendown()

t.begin_fill()

for count in range(4):
    t.fd(50)
    t.lt(90)

t.rt(150)
t.fd(35)
t.lt(150)
t.fd(50)
t.lt(30)
t.fd(35)
t.lt(150)
t.fd(50)
t.rt(90)
t.fd(50)
t.lt(120)
t.fd(35)
t.lt(60)
t.fd(50)

t.end_fill()

t.penup()

t.goto(20,-300)

t.lt(90)

t.pendown()
t.fillcolor("spring green")

t.fd(25-12.5/2)
t.rt(150)
t.begin_fill()
t.fd(35)
t.lt(150)
t.fd(12.5)
t.lt(30)
t.fd(35)
t.lt(60)
t.fd(50)
t.lt(90)
t.fd(12.5)
t.lt(90)
t.fd(50)
t.rt(90)
t.end_fill()

t.fd(25-12.5/2)
t.lt(30)
t.fd((17.5-8.75/2))
t.lt(150)
t.begin_fill()
t.fd((25-12.5/2))
t.rt(150)
t.fd(8.75)
t.lt(150)
t.fd(12.5)
t.lt(30)
t.fd(8.75)
t.lt(150)
t.fd(12.5)
t.lt(180)
t.fd((50-(25-12.5/2)))
t.rt(150)
t.fd(8.75)
t.rt(30)
t.fd(50)
t.rt(90)
t.fd(50)
t.rt(60)
t.fd(8.75)
t.rt(120)
t.fd(50)
t.end_fill()

# MAKING A HOUSE

t.penup()

t.fillcolor("red")

t.goto(300,-200)

t.pendown()
t.begin_fill()

for count in range(2):
    t.fd(140)
    t.rt(90)
    t.fd(70)
    t.rt(90)

t.end_fill()

t.lt(90)

t.fillcolor("midnight blue")

t.begin_fill()
t.fd(65)
t.rt(90)
t.fd(200)
t.rt(60)
t.fd(((2/math.sqrt(3))*100))
t.rt(60)
t.fd(((2/math.sqrt(3))*100))
t.lt(60)
t.fd(200)
t.rt(120)
t.fd(200)
t.rt(60)
t.fd(200)
t.rt(120)
t.fd(200)
t.rt(180)
t.fd(200)
t.rt(90)
t.fd(65)
t.rt(90)
t.fd(140)
t.lt(90)
t.fd(70)
t.lt(90)
t.fd(140)
t.end_fill()

t.penup()
t.lt(90)
t.fd(135)
t.lt(90)
t.fd(200)
t.rt(60)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.fd(200)
t.lt(120)
t.fd(((2/math.sqrt(3))*100))
t.lt(50)
t.fd(80)
t.goto(235,0)
t.rt(170)
t.fd(((2/math.sqrt(3))*100)+200)
t.bk(200)
t.rt(60)
t.fd(((2/math.sqrt(3))*100))

t.end_fill()

# MAKING A SNOWMAN

t.fillcolor("white")

t.penup()

t.goto(-430,45)

t.lt(120)

t.pendown()

t.begin_fill()

t.circle(40)

t.end_fill()

t.penup()

t.goto(-470,5)

t.lt(90)

t.pendown()

t.begin_fill()

t.circle(50)

t.end_fill()

t.penup()

t.goto(-470,-95)

t.pendown()

t.begin_fill()

t.circle(60)

t.end_fill()

t.penup()

t.goto(-520,-45)

t.lt(20)

t.fillcolor("brown")

t.pendown()

t.begin_fill()

t.fd(40)

t.rt(20)

t.fd(15)

t.lt(90)

t.fd(3)

t.lt(90)

t.fd(15)

t.rt(160)

t.fd(15)

t.lt(90)

t.fd(3)

t.lt(90)

t.fd(15)

t.rt(110)

t.fd(15)

t.lt(90)

t.fd(3)

t.lt(90)

t.fd(15)

t.rt(70)

t.fd(40)

t.end_fill()

t.penup()

t.goto(-420,-45)

t.rt(40)

t.pendown()

t.begin_fill()

t.fd(40)

t.lt(20)

t.fd(15)

t.rt(90)

t.fd(3)

t.rt(90)

t.fd(15)

t.lt(160)

t.fd(15)

t.rt(90)

t.fd(3)

t.rt(90)

t.fd(15)

t.lt(110)

t.fd(15)

t.rt(90)

t.fd(3)

t.rt(90)

t.fd(15)

t.lt(70)

t.fd(40)

t.end_fill()

t.penup()

t.goto(-510,45)

t.goto(-482,57)

t.dot(7,"red")

t.goto(-458,57)

t.dot(7,"red")

t.goto(-478,40)

t.pendown()

t.fillcolor("dark orange")

t.begin_fill()

t.rt(115)

for count in range(210):
    t.fd(0.1)
    t.rt(1)

t.fd(40)

t.rt(165)

t.fd(40)

t.end_fill()

t.penup()

t.goto(-472,10)

t.rt(30)

t.pendown()

t.pensize(2.5)
t.pencolor("red")

for count in range(45):
    t.fd(1.2/3)
    t.lt(1)

t.rt(180)
for count in range(90):
    t.fd(1.2/3)
    t.rt(1)

t.penup()
t.pensize(1)
t.pencolor("black")

t.goto(-470,75)
t.lt(45)

t.pendown()
t.fillcolor("dark blue")
t.begin_fill()

t.fd(30)
t.rt(120)
t.fd(60)
t.rt(120)
t.fd(60)
t.rt(120)
t.fd(30)

t.end_fill()

# SNOWFLAKES

t.penup()

t.fillcolor("white")

t.goto(-570,185)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()

t.goto(-572.5,185)

t.pendown()
t.begin_fill()

t.rt(90)
t.fd(18)
t.lt(60)
t.fd(14*1.7)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(12*1.7)
t.lt(120)
t.fd(32)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(32)
t.lt(120)
t.fd(12*1.7)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(14*1.7)
t.lt(60)
t.fd(18)

t.end_fill()
t.penup()

t.goto(-570,185)

t.lt(90)

for count in range(5):
    for count in range(60):
        t.fd((2*math.pi*10)/360)
        t.rt(1)

    t.bk(2.5)
    t.lt(90)

    t.pendown()
    t.begin_fill()

    t.fd(18)
    t.lt(60)
    t.fd(14*1.7)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(12*1.7)
    t.lt(120)
    t.fd(32)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(32)
    t.lt(120)
    t.fd(12*1.7)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(14*1.7)
    t.lt(60)
    t.fd(18)

    t.end_fill()
    t.penup()

    t.rt(90)
    t.fd(2.5)

    t.rt(180)

t.goto(-370,185)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()

t.goto(-372.5,185)

t.pendown()
t.begin_fill()

t.rt(90)
t.fd(18)
t.lt(60)
t.fd(14*1.7)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(12*1.7)
t.lt(120)
t.fd(32)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(32)
t.lt(120)
t.fd(12*1.7)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(14*1.7)
t.lt(60)
t.fd(18)

t.end_fill()
t.penup()

t.goto(-370,185)

t.lt(90)

for count in range(5):
    for count in range(60):
        t.fd((2*math.pi*10)/360)
        t.rt(1)

    t.bk(2.5)
    t.lt(90)

    t.pendown()
    t.begin_fill()

    t.fd(18)
    t.lt(60)
    t.fd(14*1.7)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(12*1.7)
    t.lt(120)
    t.fd(32)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(32)
    t.lt(120)
    t.fd(12*1.7)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(14*1.7)
    t.lt(60)
    t.fd(18)

    t.end_fill()
    t.penup()

    t.rt(90)
    t.fd(2.5)

    t.rt(180)

t.goto(-635,0)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()

t.goto(-637.5,0)

t.pendown()
t.begin_fill()

t.rt(90)
t.fd(18)
t.lt(60)
t.fd(14*1.7)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(12*1.7)
t.lt(120)
t.fd(32)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(32)
t.lt(120)
t.fd(12*1.7)
t.rt(90)
t.fd(5)
t.rt(90)
t.fd(14*1.7)
t.lt(60)
t.fd(18)

t.end_fill()
t.penup()

t.goto(-635,0)

t.lt(90)

for count in range(5):
    for count in range(60):
        t.fd((2*math.pi*10)/360)
        t.rt(1)

    t.bk(2.5)
    t.lt(90)

    t.pendown()
    t.begin_fill()

    t.fd(18)
    t.lt(60)
    t.fd(14*1.7)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(12*1.7)
    t.lt(120)
    t.fd(32)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(32)
    t.lt(120)
    t.fd(12*1.7)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(14*1.7)
    t.lt(60)
    t.fd(18)

    t.end_fill()
    t.penup()

    t.rt(90)
    t.fd(2.5)

    t.rt(180)