# agentPosition[1] is the x coordinate and agentPosition[0] is the y coordinate – can change if necessary

import matplotlib.pyplot as plt
import random
import math

matrixSize = 21  # gets you a 21x21 matrix
runtime = 100  
iterations = 1000
xPoints = []
yPoints = []


class App:
    @staticmethod
    def generateMatrix():
        mat = [[0] * matrixSize for _ in range(matrixSize)]
        # mat[random.randint(1, matrixSize - 1)][random.randint(1, matrixSize - 1)] = 1
        mat[math.floor(matrixSize / 2)][math.floor(matrixSize / 2)] = 1
        return mat

    def getAgentPosition(mat):
        agentPosition = [0] * 2
        i = 0
        while i < len(mat):
            j = 0
            while j < len(mat[i]):
                if mat[i][j] == 1:
                    agentPosition[0] = i
                    agentPosition[1] = j
                j += 1
            i += 1
        return agentPosition

    def moveAgent(mat, agentPosition, pU, pD, pL, pR):
        r = random.uniform(0, 1)
        if r < pU:
            if agentPosition[0] != 0:
                mat[agentPosition[0] - 1][agentPosition[1]] = 1
            else:
                App.moveAgent(mat, agentPosition, 0, 0.33, 0.33, 0.33)
        elif pU < r <= pU + pD:
            if agentPosition[0] != matrixSize - 1:
                mat[agentPosition[0] + 1][agentPosition[1]] = 1
            else:
                App.moveAgent(mat, agentPosition, 0.33, 0, 0.33, 0.33)
        elif pU + pD < r <= pU + pD + pL:
            if agentPosition[1] != 0:
                mat[agentPosition[0]][agentPosition[1] - 1] = 1
            else:
                App.moveAgent(mat, agentPosition, 0.33, 0.33, 0, 0.33)
        elif pU + pD + pL < r <= pU + pD + pL + pR:
            if agentPosition[1] != matrixSize - 1:
                mat[agentPosition[0]][agentPosition[1] + 1] = 1
            else:
                App.moveAgent(mat, agentPosition, 0.33, 0.33, 0.33, 0)
        return mat

    def print2D(mat):
        for row in mat:
            print(row)

    def plot(agentPosition):
        xPoints.append(agentPosition[1])
        yPoints.append(-agentPosition[0])
        plt.hist2d(xPoints, yPoints)

    @staticmethod
    def main():
        for _ in range(iterations):
            mat = App.generateMatrix()
            # App.print2D(mat)
            for _ in range(runtime):
                agentPosition = App.getAgentPosition(mat)
                # print(str((x + 1)) + ", " + str(agentPosition[0]) + ", " + str(agentPosition[1]))
                mat[agentPosition[0]][agentPosition[1]] = 0
                mat = App.moveAgent(mat, agentPosition, 0.25, 0.25, 0.25, 0.25)
            agentPosition = App.getAgentPosition(mat)
            App.plot(agentPosition)
        print("")
        # App.print2D(mat)
        plt.show()


if __name__ == "__main__":
    App.main()
