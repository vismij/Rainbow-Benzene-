import turtle
colors = ['red','green','purple','orange','blue','yellow']
a = turtle.Pen()
turtle.bgcolor('black')
for b in range(360):
    a.pencolor(colors[b%6])
    a.width(b//100 + 1)
    a.forward(b)
    a.left(59)