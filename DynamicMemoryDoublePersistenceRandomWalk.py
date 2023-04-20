# can make function setProbabilities and then return array with a and b values if current beta setup not working
# 1421 and 1422 runtimes and omega 1 cause overflow and invalid value errors leading to agent snapping to top left

import random
import math
import matplotlib.pyplot as plt
import numpy as np


matrixSize = 51  # gets you a 21x21 matrix
iterations = 1
runtime = 100
beta = 1  # bias towards up and right
omega = 0
alpha = 1  # 1 for attracting random-walk, -1 for repulsing
phi = 1
delta = 0.9
epsilon = 0

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

    def getOrientation(oldAgentPosition, newAgentPosition, orientation):
        if newAgentPosition[0] == oldAgentPosition[0] - 1:
            orientation = "U"
        elif newAgentPosition[0] == oldAgentPosition[0] + 1:
            orientation = "D"
        elif newAgentPosition[1] == oldAgentPosition[1] - 1:
            orientation = "L"
        elif newAgentPosition[1] == oldAgentPosition[1] + 1:
            orientation = "R"
        return orientation

    def setOrientation(orientation):
        r = random.uniform(0, 1)
        if orientation == "U":
            if r < (1 + 2 * delta) / 3:
                orientation = "U"
            elif (1 + 2 * delta) / 3 < r < (1 + 2 * delta) / 3 + (1 - delta) / 3:
                orientation = "L"
            elif (1 + 2 * delta) / 3 + (1 - delta) / 3 < r < (1 + 2 * delta) / 3 + (1 - delta) / 3 + (1 - delta) / 3:
                orientation = "R"
        elif orientation == "D":
            if r < (1 + 2 * delta) / 3:
                orientation = "D"
            elif (1 + 2 * delta) / 3 < r < (1 + 2 * delta) / 3 + (1 - delta) / 3:
                orientation = "L"
            elif (1 + 2 * delta) / 3 + (1 - delta) / 3 < r < (1 + 2 * delta) / 3 + (1 - delta) / 3 + (1 - delta) / 3:
                orientation = "R"
        elif orientation == "L":
            if r < (1 - delta) / 3:
                orientation = "U"
            elif (1 - delta) / 3 < r < (1 - delta) / 3 + (1 - delta) / 3:
                orientation = "D"
            elif (1 - delta) / 3 + (1 - delta) / 3 < r < (1 - delta) / 3 + (1 - delta) / 3 + (1 + 2 * delta) / 3:
                orientation = "L"
        elif orientation == "R":
            if r < (1 - delta) / 3:
                orientation = "U"
            elif (1 - delta) / 3 < r < (1 - delta) / 3 + (1 - delta) / 3:
                orientation = "D"
            elif (1 - delta) / 3 + (1 - delta) / 3 < r < (1 - delta) / 3 + (1 - delta) / 3 + (1 + 2 * delta) / 3:
                orientation = "R"
        return orientation

    @staticmethod
    def persistence(persistence, orientation):
        if orientation == "U":
            persistence[0] = (1 + phi) / 4
            persistence[1] = (1 - phi) / 4
            persistence[2] = 1/4
            persistence[3] = 1/4
        elif orientation == "D":
            persistence[0] = (1 - phi) / 4
            persistence[1] = (1 + phi) / 4
            persistence[2] = 1/4
            persistence[3] = 1/4
        elif orientation == "L":
            persistence[0] = 1/4
            persistence[1] = 1/4
            persistence[2] = (1 + phi) / 4
            persistence[3] = (1 - phi) / 4
        elif orientation == "R":
            persistence[0] = 1/4
            persistence[1] = 1/4
            persistence[2] = (1 - phi) / 4
            persistence[3] = (1 + phi) / 4
        return persistence

    def memoryReduction(mem):
        i = 0
        while i < len(mem):
            j = 0
            while j < len(mem[i]):
                r = random.uniform(0, 1)
                if r < (epsilon * mem[i][j]) / (1 + epsilon * mem[i][j]):
                    mem[i][j] = mem[i][j] - 1
                j += 1
            i += 1
        return mem

    def moveAgent(mat, agentPosition, pU, pD, pL, pR, wU, wD, wL, wR, persistence):
        r = np.float64(random.uniform(0, 1))
        if r < pU:
            if agentPosition[0] != 0:
                mat[agentPosition[0] - 1][agentPosition[1]] = 1
                agentPosition[0] = agentPosition[0] - 1
            else:
                App.moveAgent(mat, agentPosition, 0, (wD * b * persistence[1]) / (wD * b * persistence[1] + wL * b * persistence[2] + wR * a * persistence[3]), (wL * b * persistence[2]) / (wD * b * persistence[1] + wL * b * persistence[2] + wR * a * persistence[3]), (wR * a * persistence[3]) / (wD * b * persistence[1] + wL * b * persistence[2] + wR * a * persistence[3]), wU, wD, wL, wR, persistence)
        elif pU < r <= pU + pD:
            if agentPosition[0] != matrixSize - 1:
                mat[agentPosition[0] + 1][agentPosition[1]] = 1
                agentPosition[0] = agentPosition[0] + 1
            else:
                App.moveAgent(mat, agentPosition, (wU * a * persistence[0]) / (wU * a * persistence[0] + wL * b * persistence[2] + wR * a * persistence[3]), 0, (wL * b * persistence[2]) / (wU * a * persistence[0] + wL * b * persistence[2] + wR * a * persistence[3]), (wR * a * persistence[3]) / (wU * a * persistence[0] + wL * b * persistence[2] + wR * a * persistence[3]), wU, wD, wL, wR, persistence)
        elif pU + pD < r <= pU + pD + pL:
            if agentPosition[1] != 0:
                mat[agentPosition[0]][agentPosition[1] - 1] = 1
                agentPosition[1] = agentPosition[1] - 1
            else:
                App.moveAgent(mat, agentPosition, (wU * a * persistence[0]) / (wU * a * persistence[0] + wD * b * persistence[1] + wR * a * persistence[3]), (wD * b * persistence[1]) / (wU * a * persistence[0] + wD * b * persistence[1] + wR * a * persistence[3]), 0, (wR * a * persistence[3]) / (wU * a * persistence[0] + wD * b * persistence[1] + wR * a * persistence[3]), wU, wD, wL, wR, persistence)
        elif pU + pD + pL < r <= pU + pD + pL + pR:
            if agentPosition[1] != matrixSize - 1:
                mat[agentPosition[0]][agentPosition[1] + 1] = 1
                agentPosition[1] = agentPosition[1] + 1
            else:
                App.moveAgent(mat, agentPosition, (wU * a * persistence[0]) / (wU * a * persistence[0] + wD * b * persistence[1] + wL * b * persistence[2]), (wD * b * persistence[1]) / (wU * a * persistence[0] + wD * b * persistence[1] + wL * b * persistence[2]), (wL * b * persistence[2]) / (wU * a * persistence[0] + wD * b * persistence[1] + wL * b * persistence[2]), 0, wU, wD, wL, wR, persistence)
        return mat, agentPosition

    def print2D(mat):
        for row in mat:
            print(row)

    @staticmethod
    def main():
        for _ in range(iterations):
            mat = App.generateMatrix()
            mem = App.generateMatrix()
            persistence = [0] * 4
            orientation = "U"
            agentPosition = App.getAgentPosition(mat)
            # print(str(agentPosition[0]) + ", " + str(agentPosition[1]) + ", " + str(runtime))
            for _ in range(runtime):
                # oldAgentPosition = agentPosition
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
                persistence = App.persistence(persistence, orientation)
                mat[agentPosition[0]][agentPosition[1]] = 0
                mat, agentPosition = App.moveAgent(mat, agentPosition, a * ((wU * persistence[0]) / ((a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (a * wR * persistence[3]))), b * ((wD * persistence[1]) / ((a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (a * wR * persistence[3]))), b * ((wL * persistence[2]) / ((a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (a * wR * persistence[3]))), a * ((wR * persistence[3]) / ((a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (a * wR * persistence[3]))), wU, wR, wD, wL, persistence)
                mem = App.memoryReduction(mem)
                mem[agentPosition[0]][agentPosition[1]] = mem[agentPosition[0]][agentPosition[1]] + 1
                orientation = App.setOrientation(orientation)
                # orientation = App.getOrientation(oldAgentPosition, newAgentPosition, orientation)
                # print(str(agentPosition[0]) + ", " + str(agentPosition[1]) + ", " + str(runtime))
                # App.print2D(mat)
            # print("")
            # App.print2D(mat)
            # App.print2D(mem)
            # print(runtime)
            # agentPosition = App.getAgentPosition(mat)
            # print("[", math.floor(matrixSize / 2), ",", math.floor(matrixSize / 2), "]")
            # print(str(agentPosition))
            # print(agentPosition[0] - 20)
            # print(agentPosition[1] - 20)
            # values.append(agentPosition[0] - 20)
            # values.append(agentPosition[1] - 20)
            plt.imshow(mem, vmin=0, vmax=10)
            plt.colorbar()
            plt.title("alpha = " + str(alpha) + ", omega = " + str(omega) + ", beta = " + str(beta) + ", phi = " + str(phi))
            plt.show()


if __name__ == "__main__":
    App.main()
