import matplotlib.pyplot as plt
import math

timestepLen = 0.001

def plot(startingVelocity):
    velocity = startingVelocity
    position = [0,0]
    acceleration = [0,-9.8]
    positionsx = [0]
    positionsy = [0]

    while True:        
        position = [position[0]+(velocity[0]*timestepLen), position[1]+(velocity[1]*timestepLen)+(0.5*acceleration[1]*(timestepLen**2))]
        if position[1]<0: break

        ux, uy = velocity[0], velocity[1]
        velocity = [ux+(acceleration[0]*timestepLen), uy+(acceleration[1]*timestepLen)]

        positionsx.append(position[0])
        positionsy.append(position[1])

    plt.plot(positionsx, positionsy)

def plotVelocities():
    for i in range(0,10):
        for j in range(0,10):
            plot([i,j])

def plotAngles():
    for a in range(0,10):
        for theta in range(0, 90, 5):
            plot([math.cos(math.radians(theta)), math.sin(math.radians(theta))])

#plotVelocities()
plotAngles()
plt.show()