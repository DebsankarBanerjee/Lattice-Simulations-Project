# can make function setProbabilities and then return array with a and b values if current beta setup not working
# 1421 and 1422 runtimes and omega 1 cause overflow and invalid value errors leading to agent snapping to top left
# 20 segments

import random
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import logsumexp

# random.seed(10525)
matrixSize = 101  # gets you a 21x21 matrix
iterations = 10
runtime = 5000
beta = 1  # bias towards up and right
omega = 0
k = 0
phaseLength = 5
epsilon = 1
agentPosArray1 = []
agentPosArray2 = []
agentPosArray3 = []
saveTime1 = 499
saveTime2 = 1499
saveTime3 = 4999

# b = (1 / (beta + 1)) / 2  # pU, pR
# a = b * beta  # pD, pL

a = 1
b = 1


class App:
    @staticmethod
    def generateMatrix():
        mat = [[0] * matrixSize for _ in range(matrixSize)]
        # mat[random.randint(1, matrixSize - 1)][random.randint(1, matrixSize - 1)] = 1
        mat[math.floor(matrixSize / 2)][math.floor(matrixSize / 2)] = 1
        # mat[0][matrixSize - 1] = 1
        # mat[math.floor(matrixSize / 2)][2] = 1
        return mat

    @staticmethod
    def generateECM():
        ecm = [[0] * matrixSize for _ in range(matrixSize)]
        row = 0
        while row < len(ecm):
            col = 0
            while col < len(ecm[row]):
                if col <= (matrixSize - 1) / 2 - phaseLength:
                    value = epsilon * (col / int(matrixSize / 2))
                    for i in range(phaseLength):
                        ecm[row][col + i] = value
                    col += phaseLength
                elif col == (matrixSize - 1) / 2:
                    ecm[row][col] = epsilon
                    col += 1
                elif col > (matrixSize - 1) / 2:
                    value = epsilon * (1 - ((col - ((matrixSize - 1) / 2 - phaseLength + 1)) / ((matrixSize - 1) / 2)))
                    for i in range(phaseLength):
                        ecm[row][col + i] = value
                    col += phaseLength
            row += 1
        return ecm

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
        if strength > 100:
            strength = 100
        V = omega * strength
        weight = np.exp(V)
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

    @staticmethod
    def persistence(persistence, orientation):
        if orientation == "U":
            persistence[0] = 1 - 3 * (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            persistence[1] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            persistence[2] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            persistence[3] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
        elif orientation == "D":
            persistence[0] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            persistence[1] = 1 - 3 * (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            persistence[2] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            persistence[3] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
        elif orientation == "L":
            persistence[0] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            persistence[1] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            persistence[2] = 1 - 3 * (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            persistence[3] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
        elif orientation == "R":
            persistence[0] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            persistence[1] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            persistence[2] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            persistence[3] = 1 - 3 * (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
        return persistence

    def memoryReduction(mem, ecm):
        i = 0
        while i < len(mem):
            j = 0
            while j < len(mem[i]):
                #  r = random.uniform(0, 1)
                #  if r < (ecm[i][j] * mem[i][j]) / (1 + ecm[i][j] * mem[i][j]):
                # print(r)
                # print((epsilon * mem[i][j]) / (1 + epsilon * mem[i][j]))
                mem[i][j] = mem[i][j] - (ecm[i][j] * mem[i][j])
                if mem[i][j] < 0:
                    mem[i][j] = 0
                elif mem[i][j] < 0.0001:
                    mem[i][j] = 0
                j += 1
            i += 1
        return mem

    def moveAgent(mat, agentPosition, pU, pD, pL, pR, wU, wD, wL, wR, persistence, orientation):
        r = np.float64(random.uniform(0, 1))
        if r < pU:
            if agentPosition[0] != 0:
                mat[agentPosition[0] - 1][agentPosition[1]] = 1
                agentPosition[0] = agentPosition[0] - 1
                orientation = "U"
            else:
                App.moveAgent(mat, agentPosition, 0, (wD * b * persistence[1]) / (
                            wD * b * persistence[1] + wL * b * persistence[2] + wR * a * persistence[3]),
                              (wL * b * persistence[2]) / (
                                          wD * b * persistence[1] + wL * b * persistence[2] + wR * a * persistence[3]),
                              (wR * a * persistence[3]) / (
                                          wD * b * persistence[1] + wL * b * persistence[2] + wR * a * persistence[3]),
                              wU, wD, wL, wR, persistence, orientation)
        elif pU < r <= pU + pD:
            if agentPosition[0] != matrixSize - 1:
                mat[agentPosition[0] + 1][agentPosition[1]] = 1
                agentPosition[0] = agentPosition[0] + 1
                orientation = "D"
            else:
                App.moveAgent(mat, agentPosition, (wU * a * persistence[0]) / (
                            wU * a * persistence[0] + wL * b * persistence[2] + wR * a * persistence[3]), 0,
                              (wL * b * persistence[2]) / (
                                          wU * a * persistence[0] + wL * b * persistence[2] + wR * a * persistence[3]),
                              (wR * a * persistence[3]) / (
                                          wU * a * persistence[0] + wL * b * persistence[2] + wR * a * persistence[3]),
                              wU, wD, wL, wR, persistence, orientation)
        elif pU + pD < r <= pU + pD + pL:
            if agentPosition[1] != 0:
                mat[agentPosition[0]][agentPosition[1] - 1] = 1
                agentPosition[1] = agentPosition[1] - 1
                orientation = "L"
            else:
                App.moveAgent(mat, agentPosition, (wU * a * persistence[0]) / (
                            wU * a * persistence[0] + wD * b * persistence[1] + wR * a * persistence[3]),
                              (wD * b * persistence[1]) / (
                                          wU * a * persistence[0] + wD * b * persistence[1] + wR * a * persistence[3]),
                              0, (wR * a * persistence[3]) / (
                                          wU * a * persistence[0] + wD * b * persistence[1] + wR * a * persistence[3]),
                              wU, wD, wL, wR, persistence, orientation)
        elif pU + pD + pL < r <= pU + pD + pL + pR:
            if agentPosition[1] != matrixSize - 1:
                mat[agentPosition[0]][agentPosition[1] + 1] = 1
                agentPosition[1] = agentPosition[1] + 1
                orientation = "R"
            else:
                App.moveAgent(mat, agentPosition, (wU * a * persistence[0]) / (
                            wU * a * persistence[0] + wD * b * persistence[1] + wL * b * persistence[2]),
                              (wD * b * persistence[1]) / (
                                          wU * a * persistence[0] + wD * b * persistence[1] + wL * b * persistence[2]),
                              (wL * b * persistence[2]) / (
                                          wU * a * persistence[0] + wD * b * persistence[1] + wL * b * persistence[2]),
                              0, wU, wD, wL, wR, persistence, orientation)
        return mat, agentPosition, orientation

    def print2D(mat):
        for row in mat:
            print(row)

    @staticmethod
    def main():
        for _ in range(iterations):
            mat = App.generateMatrix()
            mem = App.generateMatrix()
            ecm = App.generateECM()
            residence = App.generateMatrix()
            evolution = App.generateMatrix()
            persistence = [0] * 4
            orientation = "U"
            agentPosition = App.getAgentPosition(mat)
            for step in range(runtime):
                # if mem[agentPosition[0]][agentPosition[1]] < 100:
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
                # print((a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                #                a * wR * persistence[3]))
                mat, agentPosition, orientation = App.moveAgent(mat, agentPosition, a * ((wU * persistence[0]) / (
                            (a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                                a * wR * persistence[3]))), b * ((wD * persistence[1]) / (
                            (a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                                a * wR * persistence[3]))), b * ((wL * persistence[2]) / (
                            (a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                                a * wR * persistence[3]))), a * ((wR * persistence[3]) / (
                            (a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                                a * wR * persistence[3]))), wU, wD, wR, wL, persistence, orientation)
                mem[agentPosition[0]][agentPosition[1]] = mem[agentPosition[0]][agentPosition[1]] + 1
                # mem = App.memoryReduction(mem, ecm)
                residence[agentPosition[0]][agentPosition[1]] = residence[agentPosition[0]][agentPosition[1]] + 1
                evolution[agentPosition[0]][agentPosition[1]] = step
                # orientation = App.getOrientation(oldAgentPosition, newAgentPosition, orientation)
                # print(str(agentPosition[0]) + ", " + str(agentPosition[1]) + ", " + str(runtime))
                # App.print2D(mat)
                if step == saveTime1:
                    agentPosArray1.append(list(agentPosition))
                elif step == saveTime2:
                    agentPosArray2.append(list(agentPosition))
                elif step == saveTime3:
                    agentPosArray3.append(list(agentPosition))
            # print(""
            # App.print2D(mat)
            # App.print2D(mem)
            # print(runtime)
            # agentPosition = App.getAgentPosition(mat)
            # print("[", math.floor(matrixSize / 2), ",", math.floor(matrixSize / 2), "]")
            # print(str(agentPosition))
            # print(agentPosition[0] - 20)
            # print(agentPosition[1] - 20)
            # values.append(agentPosition[0] - math.floor(matrixSize / 2))
            # values.append(agentPosition[1] - math.floor(matrixSize / 2))
            # plt.subplot(211)
            # plt.imshow(evolution)
            # plt.colorbar()
            # plt.title("k = " + str(k) + ", omega = " + str(omega))
            # plt.subplot(212)
            # plt.imshow(residence)
            # plt.colorbar()
            # plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
            # plt.imshow(ecm)
            # plt.show()


if __name__ == "__main__":
    App.main()
    print("These are the values for runtime = 500\n")
    for a in range(len(agentPosArray1)):
        print(agentPosArray1[a][0])
    print("\nThis is the barrier between x and y\n")
    for b in range(len(agentPosArray1)):
        print(agentPosArray1[b][1])
    print("\n")
    print("These are the values for runtime = 2000\n")
    for c in range(len(agentPosArray2)):
        print(agentPosArray2[c][0])
    print("\nThis is the barrier between x and y\n")
    for d in range(len(agentPosArray2)):
        print(agentPosArray2[d][1])
    print("\n")
    print("These are the values for runtime = 5000\n")
    for e in range(len(agentPosArray3)):
        print(agentPosArray3[e][0])
    print("\nThis is the barrier between x and y\n")
    for f in range(len(agentPosArray3)):
        print(agentPosArray3[f][1])
