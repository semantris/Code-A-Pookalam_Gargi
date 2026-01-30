import turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

for i in range(36):   # 36 petals
    t.color(colors[i % len(colors)])
    t.circle(100)
    t.left(10)

turtle.done()
# End of pookalam.py