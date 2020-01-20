import turtle
import tkinter

def btnSaveClick():
    print("Button Clicked!")
"""
window = tkinter.Tk()
window.minsize(width=900,height=850)
window.title("TURTLE EXERCISE")
btnSave = tkinter.Button(window, text="Save",command=btnSaveClick)
btnSave.pack()
window.mainloop()"""

turtle.title("CHESSBOARD")
turtle.penup()
turtle.goto(-150,200)
turtle.pendown()
turtle.write("CHESSBOARD", font=("Candera", 32, "bold"))
turtle.penup()
turtle.goto(-200,-220)
turtle.pendown()
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.penup()
"""turtle.goto(-50,-260)
turtle.pendown()
turtle.pencolor("black")
turtle.color("green")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()
turtle.penup()
turtle.goto(-200,-250)
turtle.color("black")
turtle.write("Circle", font=("Arial",16,"normal"))"""

xpos = -200
ypos = -220
distance = 0
turtle.goto(xpos,ypos)
for j in range(0,8):
    if(j%2 == 0):
        for i in range(0,8):
            if(i%2 == 0):
                turtle.color("black")
                turtle.begin_fill()
                turtle.pendown()
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.end_fill()
                turtle.penup()
            else:
                turtle.color("white")
                turtle.begin_fill()
                turtle.pendown()
                turtle.pencolor("black")
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.end_fill()
                turtle.penup()
            distance += 50
            turtle.goto(xpos+distance,ypos)
    else:
        for i in range(0,8):
            if(i%2 == 0):
                turtle.color("white")
                turtle.begin_fill()
                turtle.pendown()
                turtle.pencolor("black")
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.end_fill()
                turtle.penup()
            else:
                turtle.color("black")
                turtle.begin_fill()
                turtle.pendown()
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.end_fill()
                turtle.penup()
            distance += 50
            turtle.goto(xpos+distance,ypos)
    ypos += 50
    distance = 0
    turtle.goto(xpos+distance,ypos)
turtle.hideturtle()
