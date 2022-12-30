# can make function setProbabilities and then return array with a and b values if current beta setup not working
# 1421 and 1422 runtimes and omega 1 cause overflow and invalid value errors leading to agent snapping to top left

import random
import math
import matplotlib.pyplot as plt
import numpy as np

matrixSize = 41  # gets you a 21x21 matrix
iterations = 1
runtime = 1
beta = 10  # bias towards up and right
omega = 1
alpha = 1  # 1 for attracting random-walk, -1 for repulsing

b = (1 / (beta + 1)) / 2  # pU, pR
a = b * beta  # pD, pL


class App:
    @staticmethod
    def generateMatrix():
        mat = [[0] * matrixSize for _ in range(matrixSize)]
        # mat[random.randint(1, matrixSize - 1)][random.randint(1, matrixSize - 1)] = 1
        mat[math.floor(matrixSize / 2)][math.floor(matrixSize / 2)] = 1
        # mat[0][matrixSize - 1] = 1
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

    def moveAgent(mat, agentPosition, pU, pD, pL, pR, wU, wD, wL, wR):
        r = random.uniform(0, 1)
        if r < pU:
            if agentPosition[0] != 0:
                mat[agentPosition[0] - 1][agentPosition[1]] = 1
            else:
                App.moveAgent(mat, agentPosition, 0, (wD * b) / (wD * b + wL * b + wR * a), (wL * b) / (wD * b + wL * b + wR * a), (wR * a) / (wD * b + wL * b + wR * a), wU, wD, wL, wR)
        elif pU < r <= pU + pD:
            if agentPosition[0] != matrixSize - 1:
                mat[agentPosition[0] + 1][agentPosition[1]] = 1
            else:
                App.moveAgent(mat, agentPosition, (wU * a) / (wU * a + wL * b + wR * a), 0, (wL * b) / (wU * a + wL * b + wR * a), (wR * a) / (wU * a + wL * b + wR * a), wU, wD, wL, wR)
        elif pU + pD < r <= pU + pD + pL:
            if agentPosition[1] != 0:
                mat[agentPosition[0]][agentPosition[1] - 1] = 1
            else:
                App.moveAgent(mat, agentPosition, (wU * a) / (wU * a + wD * b + wR * a), (wD * b) / (wU * a + wD * b + wR * a), 0, (wR * a) / (wU * a + wD * b + wR * a), wU, wD, wL, wR)
        elif pU + pD + pL < r <= pU + pD + pL + pR:
            if agentPosition[1] != matrixSize - 1:
                mat[agentPosition[0]][agentPosition[1] + 1] = 1
            else:
                App.moveAgent(mat, agentPosition, (wU * a) / (wU * a + wD * b + wL * b), (wD * b) / (wU * a + wD * b + wL * b), (wL * b) / (wU * a + wD * b + wL * b), 0, wU, wD, wL, wR)
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
                mat[agentPosition[0]][agentPosition[1]] = 0
                mat = App.moveAgent(mat, agentPosition, a * (wU / ((a * wU) + (b * wD) + (b * wL) + (a * wR))), b * (wD / ((a * wU) + (b * wD) + (b * wL) + (a * wR))), b * (wL / ((a * wU) + (b * wD) + (b * wL) + (a * wR))), a * (wR / ((a * wU) + (b * wD) + (b * wL) + (a * wR))), wU, wR, wD, wL)
                mem[agentPosition[0]][agentPosition[1]] = mem[agentPosition[0]][agentPosition[1]] + 1
                # print(str(agentPosition[0]) + ", " + str(agentPosition[1]) + ", " + str(runtime))
                # App.print2D(mat)
            # print("")
            # App.print2D(mat)
            # App.print2D(mem)
            # print(runtime)
            plt.imshow(mem, vmin=0, vmax=10)
            plt.colorbar()
            plt.title("alpha = " + str(alpha) + ", omega = " + str(omega) + ", beta = " + str(beta))
            plt.show()


if __name__ == "__main__":
    App.main()
