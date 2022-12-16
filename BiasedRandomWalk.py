import matplotlib.pyplot as plt
import random
import math

matrixSize = 21  # gets you a 21x21 matrix
iterations = 1
xPoints = []
yPoints = []


class App:
    @staticmethod
    def generateMatrix():
        mat = [[0] * matrixSize for _ in range(matrixSize)]
        # mat[random.randint(1, matrixSize - 1)][random.randint(1, matrixSize - 1)] = 1
        # mat[math.floor(matrixSize / 2)][math.floor(matrixSize / 2)] = 1
        mat[matrixSize - 1][0] = 1
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
                App.moveAgent(mat, agentPosition, 0, 1/4, 1/4, 1/2)
        elif pU < r <= pU + pD:
            if agentPosition[0] != matrixSize - 1:
                mat[agentPosition[0] + 1][agentPosition[1]] = 1
            else:
                App.moveAgent(mat, agentPosition, 1/4, 0, 1/2, 1/4)
        elif pU + pD < r <= pU + pD + pL:
            if agentPosition[1] != 0:
                mat[agentPosition[0]][agentPosition[1] - 1] = 1
            else:
                App.moveAgent(mat, agentPosition, 1/4, 1/2, 0, 1/4)
        elif pU + pD + pL < r <= pU + pD + pL + pR:
            if agentPosition[1] != matrixSize - 1:
                mat[agentPosition[0]][agentPosition[1] + 1] = 1
            else:
                App.moveAgent(mat, agentPosition, 1/2, 1/4, 1/4, 0)
        return mat

    def print2D(mat):
        for row in mat:
            print(row)

    def plot(agentPosition):
        xPoints.append(agentPosition[1])
        yPoints.append(-agentPosition[0])
        plt.scatter(xPoints, yPoints)

    @staticmethod
    def main():
        for _ in range(iterations):
            mat = App.generateMatrix()
            # App.print2D(mat)
            agentPosition = App.getAgentPosition(mat)
            runtime = 0
            while agentPosition != [0, matrixSize - 1]:
                agentPosition = App.getAgentPosition(mat)
                mat[agentPosition[0]][agentPosition[1]] = 0
                mat = App.moveAgent(mat, agentPosition, 1/4, 1/4, 1/4, 1/4)
                runtime = runtime + 1
                agentPosition = App.getAgentPosition(mat)
                # print(str(agentPosition[0]) + ", " + str(agentPosition[1]) + ", " + str(runtime))
            # print("")
            # App.print2D(mat)
            print(runtime)


if __name__ == "__main__":
    App.main()
