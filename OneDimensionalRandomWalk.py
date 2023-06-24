import random
import math
import matplotlib.pyplot as plt
import numpy as np

matrixSize = 50  # gets you a 21x21 matrix
iterations = 1
runtime = 263
beta = 1  # bias towards up and right
omega = 0
alpha = 1  # 1 for attracting random-walk, -1 for repulsing
epsilon = 0  # 0.01
k = 0
values = []

# b = (1 / (beta + 1)) / 2  # pU, pR
# a = b * beta  # pD, pL

a = 1
b = 1


class App:
    @staticmethod
    def generateMatrix():
        mat = [0] * matrixSize
        mat[math.floor(matrixSize / 2)] = 1
        return mat

    def getAgentPosition(mat):
        agentPosition = 0
        i = 0
        while i < len(mat):
            if mat[i] == 1:
                agentPosition = i
            i += 1
        return agentPosition

    def weights(strength):
        V = omega * strength
        weight = np.exp(alpha * V)
        return weight

    @staticmethod
    def persistence(persistence, orientation):
        if orientation == "L":
            persistence[1] = (np.exp(-k) / (np.exp(-k) + np.exp(k)))
            persistence[0] = 1 - persistence[0]
        elif orientation == "R":
            persistence[0] = (np.exp(-k) / (np.exp(-k) + np.exp(k)))
            persistence[1] = 1 - persistence[1]
        return persistence

    def memoryReduction(mem):
        i = 0
        while i < len(mem):
            mem[i]= mem[i] - epsilon * mem[i]
            if mem[i] < 0:
                mem[i] = 0
            i += 1
        return mem

    def moveAgent(mat, agentPosition, pL, pR, wL, wR, persistence, orientation):
        r = random.uniform(0, 1)
        if r < pL:
            if agentPosition != 0:
                mat[agentPosition - 1] = 1
                agentPosition = agentPosition - 1
                orientation = "L"
            else:
                App.moveAgent(mat, agentPosition, 0, (wR * a * persistence[1]) / (wR * a * persistence[1]), wL, wR, persistence, orientation)
        elif pL < r <= pL + pR:
            if agentPosition != matrixSize - 1:
                mat[agentPosition + 1] = 1
                agentPosition = agentPosition + 1
                orientation = "R"
            else:
                App.moveAgent(mat, agentPosition, (wL * b * persistence[0]) / (wL * b * persistence[0]), 0, wL, wR, persistence, orientation)
        return mat, agentPosition, orientation

    @staticmethod
    def main():
        for _ in range(iterations):
            mat = App.generateMatrix()
            mem = App.generateMatrix()
            residence = App.generateMatrix()
            evolution = App.generateMatrix()
            persistence = [0] * 2
            orientation = "L"
            agentPosition = App.getAgentPosition(mat)
            for step in range(runtime):
                try:
                    wL = App.weights(mem[agentPosition - 1])
                except IndexError:
                    wL = 0
                try:
                    wR = App.weights(mem[agentPosition + 1])
                except IndexError:
                    wR = 0
                persistence = App.persistence(persistence, orientation)
                mat[agentPosition] = 0
                mat, agentPosition, orientation = App.moveAgent(mat, agentPosition, b * ((wL * persistence[0]) / ((b * wL * persistence[0]) + (a * wR * persistence[1]))), a * ((wR * persistence[1]) / ((b * wL * persistence[0]) + (a * wR * persistence[1]))), wR, wL, persistence, orientation)
                # App.print2D(mem)
                # print("")
                # mem = App.memoryReduction(mem)
                mem[agentPosition] = mem[agentPosition] + 1
                residence[agentPosition] = residence[agentPosition] + 1
                evolution[agentPosition] = step
                # orientation = App.getOrientation(oldAgentPosition, newAgentPosition, orientation)
                # print(str(agentPosition[0]) + ", " + str(agentPosition[1]) + ", " + str(runtime))
                # App.print2D(mat)
            print(residence)
            # print("")
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
            # plt.title("k = " + str(k) + ", omega = " + str(omega) + ", epsilon = " + str(epsilon))
            # plt.subplot(212)
            # plt.imshow(mem)
            # plt.colorbar()
            # plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
            # plt.show()


if __name__ == "__main__":
    App.main()