# can make function setProbabilities and then return array with a and b values if current beta setup not working
# 1421 and 1422 runtimes cause overflow and invalid value errors leading to agent snapping to top left

import random
import math
import matplotlib.pyplot as plt
import numpy as np

matrixSize = 41  # gets you a 21x21 matrix
iterations = 1
runtime = 1000
beta = 1  # bias towards up and right
omega = 0.1  # omega > 1
alpha = 1  # 1 for attracting random-walk, -1 for repulsing

b = (1 / (beta + 1)) / 2  # pU, pR
a = b * beta  # pD, pL


class App:
    @staticmethod
    def generateMatrix():
        mat = [[0] * matrixSize for _ in range(matrixSize)]
        # mat[random.randint(1, matrixSize - 1)][random.randint(1, matrixSize - 1)] = 1
        mat[math.floor(matrixSize / 2)][math.floor(matrixSize / 2)] = 1
        # mat[matrixSize - 1][0] = 1
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

    def weights(strength):
        V = omega * strength
        weight = np.exp(alpha * V)
        return weight

    def moveAgent(mat, agentPosition, pU, pD, pL, pR):
        r = random.uniform(0, 1)
        if r < pU:
            if agentPosition[0] != 0:
                mat[agentPosition[0] - 1][agentPosition[1]] = 1
            else:
                App.moveAgent(mat, agentPosition, 0, b, b, 2 * a)
        elif pU < r <= pU + pD:
            if agentPosition[0] != matrixSize - 1:
                mat[agentPosition[0] + 1][agentPosition[1]] = 1
            else:
                App.moveAgent(mat, agentPosition, a, 0, 2 * b, a)
        elif pU + pD < r <= pU + pD + pL:
            if agentPosition[1] != 0:
                mat[agentPosition[0]][agentPosition[1] - 1] = 1
            else:
                App.moveAgent(mat, agentPosition, a, 2 * b, 0, a)
        elif pU + pD + pL < r <= pU + pD + pL + pR:
            if agentPosition[1] != matrixSize - 1:
                mat[agentPosition[0]][agentPosition[1] + 1] = 1
            else:
                App.moveAgent(mat, agentPosition, 2 * a, b, b, 0)
        return mat

    def print2D(mat):
        for row in mat:
            print(row)

    @staticmethod
    def main():
        for _ in range(iterations):
            mat = App.generateMatrix()
            mem = App.generateMatrix()
            # App.print2D(mat)
            # agentPosition = App.getAgentPosition(mat)
            # print(str(agentPosition[0]) + ", " + str(agentPosition[1]) + ", " + str(runtime))
            for _ in range(runtime):
                agentPosition = App.getAgentPosition(mat)
                try:
                    wU = App.weights(mem[agentPosition[0] - 1][agentPosition[1]])
                except IndexError:
                    wU = 0
                try:
                    wD = App.weights(mem[agentPosition[0] + 1][agentPosition[1]])
                except IndexError:
                    wD = 0
                try:
                    wL = App.weights(mem[agentPosition[0]][agentPosition[1] - 1])
                except IndexError:
                    wL = 0
                try:
                    wR = App.weights(mem[agentPosition[0]][agentPosition[1] + 1])
                except IndexError:
                    wR = 0
                sum = (a * wU) + (b * wD) + (b * wL) + (a * wR)
                mat[agentPosition[0]][agentPosition[1]] = 0
                mat = App.moveAgent(mat, agentPosition, a * (wU / sum), b * (wD / sum), b * (wL / sum), a * (wR / sum))
                mem[agentPosition[0]][agentPosition[1]] = mem[agentPosition[0]][agentPosition[1]] + 1
                # print(str(agentPosition[0]) + ", " + str(agentPosition[1]) + ", " + str(runtime))
                # App.print2D(mat)
            # print("")
            # App.print2D(mat)
            # App.print2D(mem)
            # print(runtime)
            plt.imshow(mem, vmin=0, vmax=10)
            plt.colorbar()
            plt.show()


if __name__ == "__main__":
    App.main()
