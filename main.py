import matplotlib.pyplot as plt
import math

def rectPolar():
    a = int(input("Enter value for a in a + bi form: "))
    b = int(input("Enter value for b in a + bi form: "))

    options = ["(1) Convert to Polar Coordinates in CiS form", "(2) Graph Simple Visualization"]

    global xAxisLen
    global yAxisLen


    xAxisLen = 2*a + 1
    yAxisLen = 2*b + 1

     
    def plot():
        x = [0, a]
        y = [0, b]
        plt.plot(x, y)



        # orX = [-xAxisLen, xAxisLen]   
        # orY = [0, 0]

        # plt.plot(orX, orY)
        
        # orX1 = [0, 0]
        # orY1 = [-yAxisLen, yAxisLen]


        # plt.plot(orX1, orY1)

        plt.xlabel("x-axis")
        plt.ylabel("y-axis")


        plt.legend()
        plt.show()

    def convert():
        r = math.sqrt(a**2 + b**2)

        def convertDegrees(n):
            return n * 180/math.pi
        


        theta = math.acos(a/r)

        thetaDegrees = convertDegrees(theta)

        print(r, "CiS", thetaDegrees)

    convert()    
    
rectPolar()