import matplotlib.pyplot as plt
import math

timestepLen = 0.001
spehereRadius = 0.02551
sphereArea = math.pi * (spehereRadius**2)
sphereVolume = (4/3) * math.pi * (spehereRadius**3)

airDensity = 1.2754
G = 9.8

def plot(startingVelocity, startingDisplacement, dragCX, dragCY, mass, areaX, areaY):
    velocity = startingVelocity
    position = startingDisplacement
    acceleration = [0,-G]
    positionsx = [0]
    positionsy = [0]

    while True:        
        position = [position[0]+(velocity[0]*timestepLen)+(0.5*acceleration[0]*(timestepLen**2)), position[1]+(velocity[1]*timestepLen)+(0.5*acceleration[1]*(timestepLen**2))]
        if position[1]<0: break

        ux, uy = velocity[0], velocity[1]
        velocity = [ux+(acceleration[0]*timestepLen), uy+(acceleration[1]*timestepLen)]

        dragx = 0.5 * dragCX * mass * areaX * (velocity[0]**2)
        dragy = 0.5 * dragCY * mass * areaY * (velocity[1]**2)

        aix = acceleration[0]
        aiy = acceleration[1]

        upthrust = G * (sphereVolume * airDensity)
        weight = mass * G

        resx = dragx
        resy = upthrust + dragy - weight

        acceleration[0] = (resx / mass)
        acceleration[1] = (resy / mass)

        positionsx.append(position[0])
        positionsy.append(position[1])

    plt.plot(positionsx, positionsy)
    return positionsx, positionsy

def plotVelocities():
    for i in range(0,10):
        for j in range(0,10):
            plot([i,j], 0.5, 0.5, 0.0098, sphereArea, sphereArea)

def plotAngles():
    #for a in range(0,10):
    for theta in range(0, 90, 5):
        plot([math.cos(math.radians(theta)), math.sin(math.radians(theta))], 0.5, 0.5, 0.0098, sphereArea, sphereArea)

def predict(startingVelocity, startingDisplacement, dragCX, dragCY, mass, areaX, areaY):
    px, py = plot(startingVelocity, startingDisplacement, dragCX, dragCY, mass, areaX, areaY)
    return px[-1]

#plotAngles()
#plotAngles()
#plt.show()

print(predict([7.086, 0], [0,0.248], 0.5, 0.5, 0.0098, sphereArea, sphereArea))