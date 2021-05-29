from vpython import *
canvas(background=color.purple)
myring = ring(radius=0.5,thickness=0.25, color=vector(400, 100, 1))
rad = 0
while True: 
    rate(10)
    myring.rotate(angle=rad, axis=vector(0,1,0))
    rad +=0.005