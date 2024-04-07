import random
import math
import numpy as np

matrixSize = 501
iterations = 1000
omega = 0.5
epsilon = 0
k = 1.0

times = np.logspace(0.1, 4.0, num=20)
for i in range(len(times)):
    times[i] = math.floor(times[i])
print(times)

xvalues1 = []
yvalues1 = []
xvalues2 = []
yvalues2 = []
xvalues3 = []
yvalues3 = []
xvalues4 = []
yvalues4 = []
xvalues5 = []
yvalues5 = []
xvalues6 = []
yvalues6 = []
xvalues7 = []
yvalues7 = []
xvalues8 = []
yvalues8 = []
xvalues9 = []
yvalues9 = []
xvalues10 = []
yvalues10 = []
xvalues11 = []
yvalues11 = []
xvalues12 = []
yvalues12 = []
xvalues13 = []
yvalues13 = []
xvalues14 = []
yvalues14 = []
xvalues15 = []
yvalues15 = []
xvalues16 = []
yvalues16 = []
xvalues17 = []
yvalues17 = []
xvalues18 = []
yvalues18 = []
xvalues19 = []
yvalues19 = []
xvalues20 = []
yvalues20 = []


class App:
    @staticmethod
    def generateMatrix():
        mat = [[0] * matrixSize for _ in range(matrixSize)]
        mat[math.floor(matrixSize / 2)][math.floor(matrixSize / 2)] = 1
        return mat

    def weights(strength):
        V = omega * strength
        if V > 709:
            V = 709
        weight = np.exp(V)
        return weight

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

    def memoryReduction(mem):
        i = 0
        while i < len(mem):
            j = 0
            while j < len(mem[i]):
                if mem[i][j] > 0:
                    mem[i][j] = mem[i][j] - epsilon * mem[i][j]
                j += 1
            i += 1
        return mem

    def moveAgent(mat, agentPosition, pU, pD, pL, pR, wU, wD, wL, wR, persistence, orientation):
        r = random.uniform(0, 1)
        if r < pU:
            if agentPosition[0] != 0:
                mat[agentPosition[0] - 1][agentPosition[1]] = 1
                agentPosition[0] = agentPosition[0] - 1
                orientation = "U"
            else:
                print("Oh no!", agentPosition)
                App.moveAgent(mat, agentPosition, 0, (wD * persistence[1]) / (wD * persistence[1] + wL * persistence[2] + wR * persistence[3]), (wL * persistence[2]) / (wD * persistence[1] + wL * persistence[2] + wR * persistence[3]), (wR * persistence[3]) / (wD * persistence[1] + wL * persistence[2] + wR * persistence[3]), wU, wD, wL, wR, persistence, orientation)
        elif pU < r <= pU + pD:
            if agentPosition[0] != matrixSize - 1:
                mat[agentPosition[0] + 1][agentPosition[1]] = 1
                agentPosition[0] = agentPosition[0] + 1
                orientation = "D"
            else:
                print("Oh no!", agentPosition)
                App.moveAgent(mat, agentPosition, (wU * persistence[0]) / (wU * persistence[0] + wL * persistence[2] + wR * persistence[3]), 0, (wL * persistence[2]) / (wU * persistence[0] + wL * persistence[2] + wR * persistence[3]), (wR * persistence[3]) / (wU * persistence[0] + wL * persistence[2] + wR * persistence[3]), wU, wD, wL, wR, persistence, orientation)
        elif pU + pD < r <= pU + pD + pL:
            if agentPosition[1] != 0:
                mat[agentPosition[0]][agentPosition[1] - 1] = 1
                agentPosition[1] = agentPosition[1] - 1
                orientation = "L"
            else:
                print("Oh no!", agentPosition)
                App.moveAgent(mat, agentPosition, (wU * persistence[0]) / (wU * persistence[0] + wD * persistence[1] + wR * persistence[3]), (wD * persistence[1]) / (wU * persistence[0] + wD * persistence[1] + wR * persistence[3]), 0, (wR * persistence[3]) / (wU * persistence[0] + wD * persistence[1] + wR * persistence[3]), wU, wD, wL, wR, persistence, orientation)
        elif pU + pD + pL < r <= pU + pD + pL + pR:
            if agentPosition[1] != matrixSize - 1:
                mat[agentPosition[0]][agentPosition[1] + 1] = 1
                agentPosition[1] = agentPosition[1] + 1
                orientation = "R"
            else:
                print("Oh no!", agentPosition)
                App.moveAgent(mat, agentPosition, (wU * persistence[0]) / (wU * persistence[0] + wD * persistence[1] + wL * persistence[2]), (wD * persistence[1]) / (wU * persistence[0] + wD * persistence[1] + wL * persistence[2]), (wL * persistence[2]) / (wU * persistence[0] + wD * persistence[1] + wL * persistence[2]), 0, wU, wD, wL, wR, persistence, orientation)
        return mat, agentPosition, orientation

    def print2D(mat):
        for row in mat:
            print(row)

    @staticmethod
    def main():
        for _ in range(iterations):
            mat = App.generateMatrix()
            mem = App.generateMatrix()
            persistence = [0] * 4
            orientation = App.getOrientation()
            agentPosition = [math.floor(matrixSize / 2), math.floor(matrixSize / 2)]
            for steps in range(int(times[19])):
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
                mat, agentPosition, orientation = App.moveAgent(mat, agentPosition, ((wU * persistence[0]) / ((wU * persistence[0]) + (wD * persistence[1]) + (wL * persistence[2]) + (wR * persistence[3]))), ((wD * persistence[1]) / ((wU * persistence[0]) + (wD * persistence[1]) + (wL * persistence[2]) + (wR * persistence[3]))), ((wL * persistence[2]) / ((wU * persistence[0]) + (wD * persistence[1]) + (wL * persistence[2]) + (wR * persistence[3]))), ((wR * persistence[3]) / ((wU * persistence[0]) + (wD * persistence[1]) + (wL * persistence[2]) + (wR * persistence[3]))), wU, wD, wL, wR, persistence, orientation)
                #mem = App.memoryReduction(mem)
                mem[agentPosition[0]][agentPosition[1]] = mem[agentPosition[0]][agentPosition[1]] + 1
                if steps == times[0] - 1:
                    xvalues1.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues1.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[1] - 1:
                    xvalues2.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues2.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[2] - 1:
                    xvalues3.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues3.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[3] - 1:
                    xvalues4.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues4.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[4] - 1:
                    xvalues5.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues5.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[5] - 1:
                    xvalues6.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues6.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[6] - 1:
                    xvalues7.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues7.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[7] - 1:
                    xvalues8.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues8.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[8] - 1:
                    xvalues9.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues9.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[9] - 1:
                    xvalues10.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues10.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[10] - 1:
                    xvalues11.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues11.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[11] - 1:
                    xvalues12.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues12.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[12] - 1:
                    xvalues13.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues13.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[13] - 1:
                    xvalues14.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues14.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[14] - 1:
                    xvalues15.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues15.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[15] - 1:
                    xvalues16.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues16.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[16] - 1:
                    xvalues17.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues17.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[17] - 1:
                    xvalues18.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues18.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[18] - 1:
                    xvalues19.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues19.append(agentPosition[1] - math.floor(matrixSize / 2))
                elif steps == times[19] - 1:
                    xvalues20.append(agentPosition[0] - math.floor(matrixSize / 2))
                    yvalues20.append(agentPosition[1] - math.floor(matrixSize / 2))
        msd = 0.0
        mstd = 0.0
        for k in range(iterations):
            msd = msd + (xvalues1[k] ** 2) + (yvalues1[k] ** 2)
            mstd = mstd + ((xvalues1[k] ** 2) + (yvalues1[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[0], msd, merr)
        msd = 0.0
        mstd = 0.0
        for k in range(iterations):
            msd = msd + (xvalues2[k] ** 2) + (yvalues2[k] ** 2)
            mstd = mstd + ((xvalues2[k] ** 2) + (yvalues2[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[1], msd, merr)
        msd = 0.0
        mstd = 0.0
        for k in range(iterations):
            msd = msd + (xvalues3[k] ** 2) + (yvalues3[k] ** 2)
            mstd = mstd + ((xvalues3[k] ** 2) + (yvalues3[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[2], msd, merr)
        msd = 0.0
        mstd = 0.0
        for k in range(iterations):
            msd = msd + (xvalues4[k] ** 2) + (yvalues4[k] ** 2)
            mstd = mstd + ((xvalues4[k] ** 2) + (yvalues4[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[3], msd, merr)
        msd = 0.0
        mstd = 0.0
        for k in range(iterations):
            msd = msd + (xvalues5[k] ** 2) + (yvalues5[k] ** 2)
            mstd = mstd + ((xvalues5[k] ** 2) + (yvalues5[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[4], msd, merr)
        msd = 0.0
        mstd = 0.0
        for k in range(iterations):
            msd = msd + (xvalues6[k] ** 2) + (yvalues6[k] ** 2)
            mstd = mstd + ((xvalues6[k] ** 2) + (yvalues6[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[5], msd, merr)
        msd = 0.0
        mstd = 0.0
        for k in range(iterations):
            msd = msd + (xvalues7[k] ** 2) + (yvalues7[k] ** 2)
            mstd = mstd + ((xvalues7[k] ** 2) + (yvalues7[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[6], msd, merr)
        msd = 0.0
        mstd = 0.0
        for k in range(iterations):
            msd = msd + (xvalues8[k] ** 2) + (yvalues8[k] ** 2)
            mstd = mstd + ((xvalues8[k] ** 2) + (yvalues8[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[7], msd, merr)
        msd = 0.0
        mstd = 0.0
        for k in range(iterations):
            msd = msd + (xvalues9[k] ** 2) + (yvalues9[k] ** 2)
            mstd = mstd + ((xvalues9[k] ** 2) + (yvalues9[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[8], msd, merr)
        msd = 0.0
        mstd = 0.0
        for k in range(iterations):
            msd = msd + (xvalues10[k] ** 2) + (yvalues10[k] ** 2)
            mstd = mstd + ((xvalues10[k] ** 2) + (yvalues10[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[9], msd, merr)
        msd = 0.0
        mstd = 0.0
        for k in range(iterations):
            msd = msd + (xvalues11[k] ** 2) + (yvalues11[k] ** 2)
            mstd = mstd + ((xvalues11[k] ** 2) + (yvalues11[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[10], msd, merr)
        msd = 0.0
        mstd = 0.0
        for k in range(iterations):
            msd = msd + (xvalues12[k] ** 2) + (yvalues12[k] ** 2)
            mstd = mstd + ((xvalues12[k] ** 2) + (yvalues12[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[11], msd, merr)
        for k in range(iterations):
            msd = msd + (xvalues13[k] ** 2) + (yvalues13[k] ** 2)
            mstd = mstd + ((xvalues13[k] ** 2) + (yvalues13[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[12], msd, merr)
        for k in range(iterations):
            msd = msd + (xvalues14[k] ** 2) + (yvalues14[k] ** 2)
            mstd = mstd + ((xvalues14[k] ** 2) + (yvalues14[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[13], msd, merr)
        for k in range(iterations):
            msd = msd + (xvalues15[k] ** 2) + (yvalues15[k] ** 2)
            mstd = mstd + ((xvalues15[k] ** 2) + (yvalues15[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[14], msd, merr)
        for k in range(iterations):
            msd = msd + (xvalues16[k] ** 2) + (yvalues16[k] ** 2)
            mstd = mstd + ((xvalues16[k] ** 2) + (yvalues16[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[15], msd, merr)
        for k in range(iterations):
            msd = msd + (xvalues17[k] ** 2) + (yvalues17[k] ** 2)
            mstd = mstd + ((xvalues17[k] ** 2) + (yvalues17[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[16], msd, merr)
        for k in range(iterations):
            msd = msd + (xvalues18[k] ** 2) + (yvalues18[k] ** 2)
            mstd = mstd + ((xvalues18[k] ** 2) + (yvalues18[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[17], msd, merr)
        for k in range(iterations):
            msd = msd + (xvalues19[k] ** 2) + (yvalues19[k] ** 2)
            mstd = mstd + ((xvalues19[k] ** 2) + (yvalues19[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[18], msd, merr)
        for k in range(iterations):
            msd = msd + (xvalues20[k] ** 2) + (yvalues20[k] ** 2)
            mstd = mstd + ((xvalues20[k] ** 2) + (yvalues20[k] ** 2)) ** 2
        msd = msd / iterations
        mstd = mstd / iterations
        merr = np.sqrt((mstd - msd * msd) / iterations)
        print(times[19], msd, merr)


if __name__ == "__main__":
    App.main()
