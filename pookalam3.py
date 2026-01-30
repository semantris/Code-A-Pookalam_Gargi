import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
colors = ["yellow", "pink", "green", "maroon", "orange"]

# Function to draw one petal (like a teardrop)
def petal(color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(100, 60)   # first arc
    t.left(120)
    t.circle(100, 60)   # second arc
    t.left(120)
    t.end_fill()
    
def spetal(color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(140,60)
    t.left(120)
    t.circle(140,60)
    t.left(120)
    t.end_fill()
    
def tpetal(color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(180,60)
    t.left(120)
    t.circle(180,60)
    t.left(120)
    t.end_fill()
    
for x in range(3):
    num_triangles=12
    t.penup()
    t.goto(0,0)
    t.pendown()
    for n in range(1,num_triangles+1):
        if x==1:
             t.fillcolor("white")
             triangle_length=200
        else:
            t.fillcolor("green")
            triangle_length=190
        t.begin_fill()
        t.setheading(n*(360/num_triangles))
        t.forward(triangle_length)
        t.left(105.5)
        t.forward(triangle_length/1.8555)
        t.left(60)
        t.goto(0,0)
        t.end_fill()
       
    
for k in range(19):
    tpetal(colors[4])
    t.left(20)
#for j in range(19):
#    spetal(colors[j % len(colors)])
#    t.left(20)
for j in range(19):
    spetal(colors[0])
    t.left(20)    
    
# Draw a flower with petals
for i in range(12):   # 12 petals around
    petal(colors[3])
    t.left(30)   # rotate for next petal


for a in range(2):
    if a==0:   
        t.penup()
        t.goto(-10,12.5)
        t.pendown()
        t.fillcolor("green")
        t.begin_fill()     
        t.circle(15)
        t.end_fill()
    elif a==1:
        t.penup()
        t.goto(-7.5,7.5)
        t.pendown()
        t.fillcolor("white")
        t.begin_fill()
        t.circle(10)
        t.end_fill()
    

        

t.hideturtle()
turtle.done()

