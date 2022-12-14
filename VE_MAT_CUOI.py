import turtle
turtle.pensize(5)
turtle.pencolor("blue")

#face
facesize = 200
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.circle(facesize)

#eye
eye_size = 20
turtle.fillcolor("rosybrown")


#right eye
turtle.penup()
turtle.goto(100,58)
turtle.pendown()
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()

#left eye
turtle.penup()
turtle.goto(-100,58)
turtle.pendown()
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()

#nose
turtle.penup ()
turtle.goto(0,50)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(-70, steps=3)
turtle.end_fill()

#smile
turtle.penup()
turtle.goto(-100,-70)
turtle.pendown()
turtle.right(90)
turtle.circle(100,180)
turtle.mainloop()



turtle.done()

