import matplotlib.pyplot as plt
import math

print("This is my complex number python tool")

def rectPolar():
    A = int(input("Enter value for a in a + bi form: "))
    B = int(input("Enter value for b in a + bi form: "))
    A1 = int(input("Enter a for another a + bi form for multiplication: "))
    B1 = int(input("Enter b for another a + bi form for multiplication: "))


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
    
        
        plt.annotate(f'({a}, {b})', (a, b))

        


        plt.legend()
        

    def convertPolar(a, b):
        r = math.sqrt(a**2 + b**2)

        def convertDegrees(n):
            return n * 180/math.pi
        


        theta = math.acos(a/r)

        thetaDegrees = convertDegrees(theta)

        return  r ," CiS" , thetaDegrees

    def multiply(A, B, A1, B1):
        

        global aForm
        global bForm


        aForm = A * A1 + (-1*(B*B1))
        bForm = A*B1 + B * A1

        return aForm, "+", bForm
    






    print(*convertPolar(A, B))
    print("Product:", *multiply(A, B, A1, B1), "i")
    print("See Graph in other window")
    plot(A, B)
    plot(A1, B1)
    plot(aForm, bForm)
    
    plt.show()
    

    

rectPolar()