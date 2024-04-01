import random
import math
import numpy as np

matrixSize = 101
iterations = 1000
runtime = 5000
beta = 1
omega = 0.5
k = 0
phaseLength = 5
epsilon = 1
agentPosArray1 = []
agentPosArray2 = []
agentPosArray3 = []
saveTime1 = 499
saveTime2 = 1499
saveTime3 = 4999
a = 1
b = 1


class App:
    @staticmethod
    def generateMatrix():
        mat = [[0] * matrixSize for _ in range(matrixSize)]
        mat[math.floor(matrixSize / 2)][math.floor(matrixSize / 2)] = 1
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

    @staticmethod
    def getOrientation():
        r = random.uniform(0, 1)
        if r <= 0.25:
            orientation = "U"
        elif 0.25 < r <= 0.5:
            orientation = "D"
        elif 0.5 < r <= 0.75:
            orientation = "L"
        else:
            orientation = "R"
        return orientation

    def weights(strength):
        V = omega * strength
        # if V > 20:
        #     V = 20
        if V > 709:
            V = 709
        weight = np.exp(V)
        return weight

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
            persistence = [0] * 4
            orientation = App.getOrientation()
            agentPosition = [int(matrixSize / 2), int(matrixSize / 2)]
            for step in range(runtime):
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
                mat, agentPosition, orientation = App.moveAgent(mat, agentPosition, a * ((wU * persistence[0]) / (
                        (a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                        a * wR * persistence[3]))), b * ((wD * persistence[1]) / (
                        (a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                        a * wR * persistence[3]))), b * ((wL * persistence[2]) / (
                        (a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                        a * wR * persistence[3]))), a * ((wR * persistence[3]) / (
                        (a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                        a * wR * persistence[3]))), wU, wD, wL, wR, persistence, orientation)
                mem[agentPosition[0]][agentPosition[1]] += 1
                # mem = App.memoryReduction(mem, ecm)
                if step == saveTime1:
                    agentPosArray1.append(list(agentPosition))
                if step == saveTime2:
                    agentPosArray2.append(list(agentPosition))
                if step == saveTime3:
                    agentPosArray3.append(list(agentPosition))


if __name__ == "__main__":
    App.main()
    count500 = 0
    for a in range(len(agentPosArray1)):
        if agentPosArray1[a][1] <= 5 or agentPosArray1[a][1] >= 95:
            count500 += 1
    print(count500)
    count1500 = 0
    for b in range(len(agentPosArray2)):
        if agentPosArray2[b][1] <= 5 or agentPosArray2[b][1] >= 95:
            count1500 += 1
    print(count1500)
    count5000 = 0
    for c in range(len(agentPosArray3)):
        if agentPosArray3[c][1] <= 5 or agentPosArray3[c][1] >= 95:
            count5000 += 1
    print(count5000)


