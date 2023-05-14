

import turtle
import random

wn = turtle.Screen()
wn.setup(500, 500)
wn.bgcolor("white")
wn.tracer(0)

#Turtle object for falling block
t = turtle.Turtle()
x, y, w, h = random.randint(-250, 140), 245, 100, 100

#Controls animation of falling block
z = 4

#Turtle object for player's block
t2 = turtle.Turtle()
a, b = 0, -145

#Controls animation of player's block
k = 5

t.hideturtle()
t2.hideturtle()

t.color("skyblue")
t2.color("pink")

#Use this to draw the block
def draw_rectangle(x, y, w, h, t):
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(0)
    for i in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()

#Use this to animate the square
def animation():
    global x
    global y
    global w
    global h

    global t
    global t2
    global wn

    global z
    global k
    global a
    global b

    t.hideturtle()
    t.clear()

    t2.hideturtle()
    t2.clear()

    #Generates the falling rectangle
    draw_rectangle(x, y, w, h, t)
    y -= z

    if y <= -245:
        y = 245
        x = random.randint(-250, 140)


    #Functions for the key presses
    def left_press():
        global k
        print("left pressed")
        k = -5

    def right_press():
        global k
        print("right pressed")
        k = 5

    wn.onkeypress(left_press, 'Left')
    wn.onkeypress(right_press, 'Right')

   #Generates the player's rectangle
    draw_rectangle(a, b, w, h, t2)

    a += k

    if a <= -250:
        k = 5

    elif a >= 145:
      k = -5
      
    #Methods to stop the game if there is an interesection
    def point_in_rectangle(x, y, x1, y1, x2, y2):
        return x >= x1 and x <= x2 and y >= y2 and y <= y1

    for p in [(x, y), (x + w, y), (x + w, y - h), (x, y - h)]:
        if point_in_rectangle(p[0], p[1], a, b, a + 100, b - 100):
            wn.bgcolor("grey")
            k = 0
            z = 0

    wn.ontimer(animation, 20)
    wn.update()

#Executing the functions
animation()

wn.listen()
wn.mainloop()

