import turtle
import math

angle = float(input("What is the angle of elevation?"))
mass = float(input("What is the mass of the block?"))
friction = float(input("What is the coefficient of friction?"))

mg = mass*9.8
N = mg*math.cos(math.radians(angle))

if (angle > 90):
    angle2 = 180 -angle
else:
    angle2 = 90 - angle
bob = turtle.Turtle()
#Draw Box
bob.left(angle)
for x in range(0,4):
    bob.forward(100)
    bob.right(90)
bob.right(90)
bob.forward(100)
#Draw Hill
bob.right(90)
bob.forward(100)
bob.right(180)
bob.forward(300)
bob.right(180-angle2)
bob.forward(300*math.cos(math.radians(angle2)))
bob.right(90)
bob.forward(300*math.sin(math.radians(angle2)))
bob.penup()
bob.home()
bob.left(angle)
bob.forward(50)
bob.right(90)
bob.forward(50)
bob.pendown()
#Gravity Vector
bob.color("blue")
bob.right(angle)
bob.forward(mass*2)
bob.stamp()
#mg
bob.penup()
bob.forward(10)
bob.write(mg)
bob.right(180)
bob.forward(10)
bob.pendown()
bob.forward(mass*2)
#Normal Force Vector
bob.color("red")
if (angle > 90):
    bob.left(angle)
    bob.forward(mass*-2*math.cos(math.radians(angle)))
    bob.write(N)
    bob.stamp()
else:
    bob.left(angle)
    bob.forward(mass*2*math.cos(math.radians(angle)))
    bob.write(N)
    bob.stamp()
#Return Home
bob.color("black")
bob.penup()
bob.home()
#Friction Vector
bob.left(angle)
bob.forward(50)
bob.right(90)
bob.forward(50)
bob.left(90)
bob.color("green")
bob.pendown()
bob.forward(mass*2*friction*math.cos(math.radians(angle)))
bob.stamp()
bob.write(friction*N)


print("The force of gravity is ",mg," Newtons.")
print("The normal force acting on the block is ",N," Newtons.")
print("The frictionl force is ",friction*N," Newtons.")
