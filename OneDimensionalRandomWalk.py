import random
import math
import matplotlib.pyplot as plt
import numpy as np

matrixSize = 1000  # gets you a 21x21 matrix
iterations = 10
runtime = 263
beta = 1  # bias towards up and right
omega = 0
alpha = 1  # 1 for attracting random-walk, -1 for repulsing
epsilon = 0  # 0.01
k = 0
values = []

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
                mem[agentPosition] = mem[agentPosition] + 1
                residence[agentPosition] = residence[agentPosition] + 1
                evolution[agentPosition] = step
            values.append(agentPosition - int(matrixSize / 2))
        msd = 0
        for x in values:
            msd = msd + (x ** 2)
        msd = msd / iterations
        print(msd)


if __name__ == "__main__":
    App.main()
    