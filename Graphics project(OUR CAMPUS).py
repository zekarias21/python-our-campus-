##A+

##pseudo code
##pseudo code
##pseudo code
## 1. create canvas in the beginning that is 1300(width) x 800(length) pixel
## 2. create fence, gate, office, mountain, car, green area, rocket and them to
##    the canvas
## 3. while the program is executing (animating)
###### 3.1 rotate the windturbine during all animation session
###### 3.2 move the car in south east direction
###### 3.3 as the car approaches the cross, rotate and move the car in the east
###### 3.4 when the car finally finishes its movement launch the rocket
###### 3.5 when the rocket approaches some height dispart its wing
## 4. close canvas
##
##
## animate windturbine during all movement 
###### while the car is moving
###### car rotate while it approaches the cross then move to the east
######

from cs1graphics import *
import time
import sys
p=Point
c=Canvas(1300,800)
c.setTitle("ASTU CAMPUS (THE HELL)Graphics Project")

##Aman Bereket          ID. No 0137/08
##Amanuel Desalegn      ID. No 0145/08
##Amanuel Berhanu       ID.No 0143/08

##submitted to: Inst. Getnet Yilma
c.setBackgroundColor("green")
r=Rectangle(1300,450,Point(650,525))
r.setFillColor("darkgreen")
c.add(r)

############road

road=Polygon (p(50,0), p(250,0), p(900,600), p(300,600))
road.setFillColor("black")
c.add(road)

road2=Rectangle(900,100,p(850,250))
road2.setFillColor("black")
c.add(road2)


##########door

doora=Ellipse(600,450,p(600,600))
doora.setBorderColor("blue")
doora.setFillColor("white")
doora.setBorderWidth(5)
c.add(doora)



doorh=Ellipse(800,400,p(600,730))
doorh.setFillColor("black")

c.add(doorh)

door1=Ellipse(100,200,p(400,600))
door1.setDepth(48)
door1.setFillColor("black")
c.add(door1)

door2=Ellipse(100,200,p(800,600))
door2.setDepth(48)
door2.setFillColor("black")
door2.rotate(-10)
c.add(door2)

door3=Ellipse(130,300,p(523,600))
door3.setDepth(48)
door3.setFillColor("black")
c.add(door3)

door4=Ellipse(130,300,p(676,600))
door4.setDepth(48)
door4.setFillColor("black")
c.add(door4)


doora=Ellipse(600,450,p(600,600))
doora.setBorderColor("blue")
doora.setBorderWidth(5)
c.add(doora)

doorh=Ellipse(800,400,p(600,730))
doorh.setFillColor("black")

c.add(doorh)

s=Spline (p(250,550),p(400,320),p(670,380))
s.setBorderColor("blue")
s.setBorderWidth(4)

s.setDepth(49)
c.add(s)



##gate name
m=Text("A")
m.setFontColor("blue")
m.scale(3)
m.moveTo(440,460)
c.add(m)

m2=Text("S")
m2.setFontColor("blue")
m2.scale(3)
m2.moveTo(540,425)
c.add(m2)

m3=Text("T")
m3.setFontColor("blue")
m3.scale(3)
m3.moveTo(640,425)
c.add(m3)

m4=Text("U")
m4.setFontColor("blue")
m4.scale(3)
m4.moveTo(740,440)
c.add(m4)

##emblem
emblem=Circle(10,p(590,440))
emblem.setFillColor("red")
c.add(emblem)
emblem2=Circle(7,p(590,440))
emblem2.setFillColor("green")
c.add(emblem2)

######## green area
green1=Polygon (p(0,600), p(300,600), p(380,800), p(0,800))
green1.setFillColor("green")
c.add(green1)

green2=Polygon (p(900,600), p(1300,600), p(1380,800), p(1000,800))
green2.setFillColor("green")
c.add(green2)
green3=Polygon (p(0,700), p(340,700), p(450,800), p(0,800))
green3.setFillColor("black")
c.add(green3)

green4=Polygon (p(870,700), p(1300,700), p(1380,800), p(1000,800))
green4.setFillColor("black")
c.add(green4)

########fence
fence=Polygon (p(0,500),p(285,500),p(275,600),p(0,600))
fence.setFillColor("grey")
fence.setDepth(46)
c.add(fence)

fence2=Polygon (p(870,500),p(1300,500),p(1300,600),p(900,600))
fence2.setFillColor("grey")
fence2.setDepth(46)

c.add(fence2)


########house

house=Layer()
h=Polygon(Point(700,180) ,Point(700,0) ,Point(650,40) ,Point(650,160))
h.setBorderColor("black")
h.setFillColor("yellow")
h.setDepth(25)

h1=Polygon(Point(700,0) ,Point(740,20) ,Point(740,180) ,Point(700,180))
h1.setBorderColor("black")
h1.setFillColor("yellow")
h1.setDepth(25)

h2=Polygon(Point(740,20) ,Point(860,20) ,Point(860,180) ,Point(740,180))
h2.setBorderColor("yellow")
h2.setFillColor("grey")
h2.setDepth(25)

h3=Polygon(Point(700,0) ,Point(820,0) ,Point(860,20) ,Point(740,20))
h3.setBorderColor("yellow")
h3.setFillColor("darkred")
h3.setDepth(25)
##window
h4=Rectangle(25,35,p(760,50))
h4.setBorderColor("yellow")
h4.setFillColor("brown")
h4.setDepth(25)


h5=h4.clone()
h5.moveTo(800,50)

h6=h4.clone()
h6.moveTo(840,50)

h7=h4.clone()
h7.moveTo(800,100)

h8=h4.clone()
h8.moveTo(840,100)

h9=h4.clone()
h9.moveTo(760,100)

h10=h4.clone()
h10.moveTo(760,150)

h11=h4.clone()
h11.moveTo(800,150)

h12=h4.clone()
h12.moveTo(840,150)





house.add(h)
house.add(h1)
house.add(h2)
house.add(h3)
house.add(h4)
house.add(h5)
house.add(h6)
house.add(h7)
house.add(h8)
house.add(h9)
house.add(h10)
house.add(h11)
house.add(h12)
house.setDepth(25)
c.add(house)

house2=house.clone()
house2.moveTo(400,0)
c.add(house2)

house3=house.clone()
house3.moveTo(230,0)
c.add(house3)
house4=house.clone()
house4.moveTo(440,165)
c.add(house4)

house5=house.clone()
house5.moveTo(270,165)
h
c.add(house5)

########office
office=Layer()

hr=Polygon(p(470,200),p(550,220),p(550,340),p(470,320))
hr.setFillColor("gray")
hr2=Polygon(p(550,220),p(590,220),p(590,340),p(550,340))
hr2.setFillColor("gray")
hr3=Polygon(p(590,220),p(640,240),p(640,360),p(590,340))
hr3.setFillColor("gray")
hr4=Polygon(p(640,240),p(700,220),p(700,340),p(640,360))
hr4.setFillColor("gray")
hr5=Polygon(p(700,290),p(750,290),p(750,340),p(700,340))
hr5.setFillColor("gray")

hr6=Polygon(p(470,200),p(520,160),p(550,220))
hr6.setFillColor("black")
hr7=Polygon(p(520,160),p(625,180),p(590,220),p(550,220))
hr7.setFillColor("darkred")
hr8=Polygon(p(590,220),p(625,180),p(640,240))
hr8.setFillColor("black")

hr9=Polygon(p(625,180),p(675,180),p(700,220),p(640,240))
hr9.setFillColor("darkred")


hr10=Polygon(p(700,290),p(725,270),p(750,290))
hr10.setFillColor("black")
hr11=Polygon(p(700,270),p(725,270),p(700,290))
hr11.setFillColor("darkred")

box=hr.clone()
box.scale(0.2)
box.moveTo(600,245)
box.setFillColor("brown")

box2=box.clone()
box2.moveTo(600,300)

box3=box.clone()
box3.moveTo(710,300)
box3.rotate(-1)

box4=box.clone()
box4.moveTo(515,283)
box4.scale(2)
box4.setFillColor("blue")



office.add(hr)
office.add(hr2)
office.add(hr3)
office.add(hr4)
office.add(hr5)
office.add(hr6)
office.add(hr7)
office.add(hr8)
office.add(hr9)
office.add(hr10)
office.add(hr11)
office.add(box)
office.add(box2)
office.add(box3)
office.add(box4)
c.add(office)
office.moveTo(-45,-170)
office.rotate(1)
office.setDepth(21)
##horizontal road
l6=Path(p(600,245),p(700,245))
l6.setBorderColor("white")
l6.setBorderWidth(3)
c.add(l6)

l7=l6.clone()
l7.moveTo(780,245)
c.add(l7)


##road line
l=Path(p(270,150),p(230,100))
l.setDepth(48)
l.setBorderColor("white")
l.setBorderWidth(3)
c.add(l)

l1=Path(p(330,220),p(290,170))
l1.setDepth(48)
l1.setBorderColor("white")
l1.setBorderWidth(3)
c.add(l1)

l2=l1.clone()
l2.moveTo(400,300)
c.add(l2)

l3=l1.clone()
l3.moveTo(465,375)
c.add(l3)

l4=l1.clone()
l4.moveTo(645,600)
l4.scale(1.15)
c.add(l4)

l5=l1.clone()
l5.moveTo(710,685)
l5.scale(1.2)
c.add(l5)


##mountain

m1=Polygon(p(0,300),p(70,100),p(140,300))
m1.setDepth(99)
m1.setFillColor((80,80,10))
c.add(m1)

m2=Ellipse(200,250,p(0,200))
m2.setDepth(100)
m2.setFillColor((80,80,10))
c.add(m2)

########windturbine
wt=Path(p(100,200),p(100,300))
wt.setBorderColor("white")
wt.setBorderWidth(5)
c.add(wt)

wt2=Path(p(100,200),p(100,250))
wt2.setBorderColor("white")
wt2.setBorderWidth(4)
wt2.rotate(0)
c.add(wt2)

wt3=Path(p(100,200),p(100,250))
wt3.setBorderColor("white")
wt3.setBorderWidth(4)
wt3.rotate(120)
c.add(wt3)

wt4=Path(p(100,200),p(100,250))
wt4.setBorderColor("white")
wt4.setBorderWidth(4)
wt4.rotate(240)
c.add(wt4)

## wind tubine blade

wtt1=Path(p(40,200),p(40,300))
wtt1.setBorderColor("white")
wtt1.setBorderWidth(5)
c.add(wtt1)

wtt2=Path(p(40,200),p(40,250))
wtt2.setBorderColor("white")
wtt2.setBorderWidth(4)
wtt2.rotate(0)
c.add(wtt2)

wtt3=Path(p(40,200),p(40,250))
wtt3.setBorderColor("white")
wtt3.setBorderWidth(4)
wtt3.rotate(120)
c.add(wtt3)

wtt4=Path(p(40,200),p(40,250))
wtt4.setBorderColor("white")
wtt4.setBorderWidth(4)
wtt4.rotate(240)
c.add(wtt4)

########rocket
rocket=Layer()

rocr2=Ellipse(60,200,p(130,400))
rocr2.setFillColor("white")
rocket.add(rocr2)
rocr=Polygon (p(100,400), p(160,400), p(160,600), p(100,600))
rocr.setFillColor("white")
rocket.add(rocr)

roc=Polygon (p(160,510), p(240,550), p(240,580), p(160,570))
roc.setFillColor("white")
roc.setDepth(40)
rocket.add(roc)

roc1=Polygon (p(100,510), p(100,570), p(30,580), p(30,550))
roc1.setFillColor("white")
roc.setDepth(40)
rocket.add(roc1)

roc2=Path(p(130,510),p(130,570))
roc2.setDepth(38)
roc2.setBorderColor("black")
roc2.setBorderWidth(7)
rocket.add(roc2)

roc3=Polygon (p(120,600), p(140,600), p(160,610), p(100,610))
roc3.setFillColor("white")
roc.setDepth(40)
rocket.add(roc3)

rocket.setDepth(20)
rocket.moveTo(950,100)
rocket.scale(0.5)
c.add(rocket)

##rocket liftoff
rocklift=Rectangle(35,20,p(1013,415))
rocklift.setFillColor("white")
c.add(rocklift)
##rocket fire
rockf= Ellipse(25,80,p(1015,360))
rockf.setFillColor("red")
rockf.setDepth(22)
c.add(rockf)

##########car
car1=Layer()
car1.moveTo(140,-100)
part1=Polygon(p(-40,-10),p(-40,-30),p(-30,-40),p(20,-40),p(30,-30),p(40,-20),p(40,-10))
part1.setFillColor("blue")
part1.setDepth(58)
part2=Rectangle(30,10,p(-15,-30))
part2.setDepth(57)
part2.setFillColor("lightblue")
part3=Rectangle(18,10,p(10,-30))
part3.setDepth(57)
part3.setFillColor("lightblue")
part4=Circle(7,p(-20,-10))
part4.setDepth(57)
part4.setFillColor("black")
part4.setBorderColor("white")
part5=Circle(7,p(20,-10))
part5.setFillColor("black")
part5.setBorderColor("white")
part5.setDepth(57)
car1.setDepth(30)
car1.move(0,20)

car1.add(part1)
car1.add(part2)
car1.add(part3)
car1.add(part4)
car1.add(part5)

car1.rotate(45)

c.add(car1)


##precursor animation
def windturbine():
    wt2.rotate(10)
    wt3.rotate(10)
    wt4.rotate(10)
    wtt2.rotate(10)
    wtt3.rotate(10)
    wtt4.rotate(10)
    
######animation


for i in range(50):
    car1.move(4.8,6)
    windturbine()
    time.sleep(0.07)

for i in range (45):
        car1.rotate(-1)
        car1.move(2,1)
        time.sleep(0.01)
        windturbine()
        
for i in range (100):
        car1.move(4.2,0)
        windturbine()

for i in range(80):
    car1.move(4,0)
    windturbine()
    time.sleep(0.01)

for i in range (50):
    rocket.move(0,-2.5)
    rockf.scale(0.94)
    windturbine()
rocket.remove(roc1)
rocket.remove(roc)
roc.moveTo(950,200)
roc.scale(0.5)
roc.setDepth(20)
roc1.moveTo(1100,200)
roc1.scale(0.5)
roc1.setDepth(0.5)
c.add(roc)
c.add(roc1)
for i in range (140):
    rocket.move(0,-2.5)
    windturbine()
    roc.move(0,1.33)
    roc1.move(0,1.33)




