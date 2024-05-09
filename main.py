import matplotlib.pyplot as plt
import math

def rectPolar():
    A = int(input("Enter value for a in a + bi form: "))
    B = int(input("Enter value for b in a + bi form: "))

    global xAxisLen
    global yAxisLen


    xAxisLen = 2*A + 1
    yAxisLen = 2*B + 1

     
    def plot(a, b):
        x1 = [0, a]
        y1 = [0, b]
        plt.plot(x1, y1)

        plt.xlim(-xAxisLen, xAxisLen)
        plt.ylim(-yAxisLen, yAxisLen)

        plt.plot([-xAxisLen, xAxisLen], [0, 0], label = "X Axis")
        plt.plot([0, 0], [-yAxisLen, yAxisLen], label = "Y Axis")
    
        
        plt.annotate(f'({a}, {b})', (a, b), textcoords="offset points", xytext=(0,10), ha='center')

        


        plt.legend()
        plt.show()

    def convertPolar(a, b):
        r = math.sqrt(a**2 + b**2)

        def convertDegrees(n):
            return n * 180/math.pi
        


        theta = math.acos(a/r)

        thetaDegrees = convertDegrees(theta)

        return  r ," CiS" , thetaDegrees


    print(*convertPolar(A, B))
    print("See Graph in other window")
    plot(A, B)

    

rectPolar()