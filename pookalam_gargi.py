import joy 
def trianglep():
    p1=point(x=0,y=0)
    p2=point(x=-10,y=80)
    p3=point(x=10,y=80)
    p=polygon([p1,p2,p3],fill="pink",stroke="white",stroke_width=2)
    return p
def trianglev():
    p1=point(x=0,y=0)
    p2=point(x=-10,y=70)
    p3=point(x=10,y=70)
    v=polygon([p1,p2,p3],fill="violet",stroke="pink",stroke_width=2)
    return v
def triangleb():
    p1=point(x=0,y=0)
    p2=point(x=-10,y=60)
    
    p3=point(x=10,y=60)
    b=polygon([p1,p2,p3],fill="#1E90FF",stroke="violet",stroke_width=2)
    return b
    
c1=circle(r=150,fill="black")
r1=rectangle(w=210,h=210,fill="#DC143C", stroke="none")|repeat(100,rotate(10))
r2=rectangle(w=210,h=180,fill="orange",stroke="none")|repeat(10,rotate(10))
r3=rectangle(w=210,h=150,fill="yellow",stroke="none")|repeat(11,rotate(10))
r4=rectangle(w=210,h=120,fill="white",stroke="none")|repeat(12,rotate(10))
c2=circle(r=105,fill="green",stroke="#8B0000",stroke_width=5)
c3=circle(x=75,y=0,r=20,fill="white",stroke="none")|repeat(40,rotate(10))
t1=trianglep()|repeat(36,rotate(10))
t2=trianglev()|repeat(36,rotate(10))
t3=triangleb()|repeat(36,rotate(10))
e1=ellipse(x=35,y=0 ,w=60,h=35,fill="yellow",stroke="none")|repeat(10,rotate(45))
e2=ellipse(x=30,y=0 ,w=55,h=35,fill="orange",stroke="none")|repeat(10,rotate(45))
e3=ellipse(x=25,y=0 ,w=50,h=35,fill="#DC143C",stroke="none")|repeat(10,rotate(45))
e4=ellipse(x=20,y=0,w=45,h=35,fill="white",stroke="none")|repeat(8,rotate(45))

c4=circle(r=33,fill="orange",stroke="green",stroke_width=3)
e5=ellipse(x=15,y=0,w=25,h=10,fill="green",stroke="none")|repeat(6,rotate(60))
e6=ellipse(x=10,y=0,w=20,h=10,fill="blue",stroke="none")|repeat(6,rotate(60))
e7=ellipse(x=5,y=0,w=15,h=10,fill="yellow",stroke="none")|repeat(6,rotate(60))
e8=ellipse(x=0,y=0,w=10,h=10,fill="white",stroke="none")|repeat(6,rotate(60))
show(c1,r1,r2,r3,r4,c2,c3,t1,t2,t3,e1,e2,e3,e4,c4,e5,e6,e7,e8)