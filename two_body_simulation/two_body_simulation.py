from dataclasses import dataclass
import math
import  time


@dataclass()
class TwoBodyModel:
    T: int
    dt: float
    massRatio: float
    eccentricity: float
    method: str



class TwoBodyController:
    def __init__(self, model):
        self.T = model.T
        self.dt = model.dt
        self.massRatio = model.massRatio
        self.eccentricity = model.eccentricity
        self.method = model.method
        self.u = [1,0,0,0] # first two are x and y position, second two are x, y components of velocity
        self.m1 = 1
        self.m2 = self.massRatio
        self.m12 = self.m1 + self.m2
        self.positions = [{"x" : 0, "y" : 0},{"x" : 0, "y" : 0}] # [body1,body2]
        self.recordedPositions = []
        self.u[3] = self.initialVelocity(self.massRatio,self.eccentricity)
        self.text = ""

    def initialVelocity(self, massRatio, eccentricity):
        return math.sqrt((1 + massRatio) * (1 + eccentricity))

    def derivative(self):
        du = [0 for i in self.u]
        r = self.u[:2]         # x and y cordinates
        rr = math.sqrt(math.pow(r[0],2) + math.pow(r[1],2))      # distance between bodies

        for i in range(2):
            du[i] = self.u[i+2]
            du[i+2] = -(1+ self.massRatio)*r[i]/(math.pow(rr,3))
        return du

    def rungeKutta(self, h, u):
        a = [h/2, h/2, h, 0]
        b = [h/6, h/3, h/3, h/6]
        u0 = []
        ut = []
        dimension = len(u)
        for i in u:
            u0.append(i)
            ut.append(0)
        for j in range(4):
            du = self.derivative()

            for i in range(dimension):
                u[i] = u0[i] + a[j]*du[i]
                ut[i] = ut[i] + b[j]*du[i]

        for i in range(dimension):
            u[i] = u0[i] + ut[i]

    def euler(self,h,u):
        #TODO
        pass

    def calculateNewPosition(self):
        r = 1 # distance between bodies
        a1 = (self.m2 / self.m12) * r
        a2 = (self.m1 / self.m12) * r

        self.positions[0]["x"] = -a2 * self.u[0]
        self.positions[0]["y"] = -a2 * self.u[1]

        self.positions[1]["x"] = a1 * self.u[0]
        self.positions[1]["y"] = a1 * self.u[1]

    def updatePosition(self):
        startTime = time.time()
        timeDifference = 0
        while self.T/1000 >= timeDifference:
            if(self.method == 1):
                self.rungeKutta(self.dt,self.u)
            else:
                self.euler(self.dt,self.u)
            self.recordPositions()
            self.calculateNewPosition()
            lastTime = time.time()
            timeDifference = lastTime - startTime

    def recordPositions(self):
         self.text += str(self.positions[0]["x"]) + "," + str(self.positions[0]["y"]) + "," + str(self.positions[1]["x"]) + "," + str(self.positions[1]["y"]) + "\n"
    def savePositionsToFile(self):
        file = open("locationVectors.txt","w")
        file.write(self.text)
        file.close()


class App:
    def __init__(self):
        self.T = 5
        self.dt = 0.15
        self.massRatio = 0.5
        self.eccentricity = 0.7
        self.method = "runge-kutta"

    def run(self):
        model = TwoBodyModel(self.T, self.dt, self.massRatio, self.eccentricity, self.method )
        c = TwoBodyController(model)
        c.updatePosition()
        c.savePositionsToFile()

    def getInputs(self):
        self.T = int(input("Enter T : "))
        self.dt = float(input("Enter time step h : "))
        self.massRatio = float(input("Enter mass ratio : "))
        self.method = int(input("Enter 1 for Runge-Kutta or 2 for Euler's method: "))


if __name__ == "__main__":
    app = App()
    app.getInputs()
    app.run()