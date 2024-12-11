import turtle 
import datetime as dt 
import time
# create a turtle to create rectangle box
t1=turtle.Turtle()
# create a turtle to display time
t2=turtle.Turtle()
# create screen
s = turtle.Screen()
 
# set background color of the screen
s.bgcolor("green")

sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour

t1.pensize(3)
t1.color('dark blue')
t1.penup()

t1.goto(-20, 0)
t1.pendown()
 
for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(70)
    t1.left(90)
t1.hideturtle()

while True:
    t2.hideturtle()
    t2.clear()
    # display the time
    t2.write(str(hr).zfill(2)
            + ":"+str(min).zfill(2)+":"
            + str(sec).zfill(2),
            font=("Arial Narrow", 25, "bold"))
    time.sleep(1)
    sec += 1
 
    if sec == 60:
        sec = 0
        min += 1
 
    if min == 60:
        min = 0
        hr += 1
 
    if hr == 13:
        hr = 1