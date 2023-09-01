import random
import math
import matplotlib.pyplot as plt
import numpy as np

matrixSize = 101  # gets you a 21x21 matrix
iterations = 1
runtime = 1
beta = 1  # bias towards up and right
omega = 0
epsilon = 1  # 0.01
k = 0
phaseLength = 5

a = 1
b = 1


class App:
    @staticmethod
    def generateMatrix():
        mat = [0] * matrixSize
        mat[math.floor(matrixSize / 2)] = 1
        return mat

    @staticmethod
    def generateECM():
        ecm = [0] * matrixSize
        i = 0
        while i < len(ecm):
            if i <= (matrixSize - 1) / 2 - phaseLength:
                value = epsilon * (i / int(matrixSize / 2))
                for j in range(phaseLength):
                    ecm[i + j] = value
                i += phaseLength
            elif i == (matrixSize - 1) / 2:
                ecm[i] = epsilon
                i += 1
            elif i > (matrixSize - 1) / 2:
                value = epsilon * (1 - ((i - ((matrixSize - 1) / 2 - phaseLength + 1)) / ((matrixSize - 1) / 2)))
                for j in range(phaseLength):
                    ecm[i + j] = value
                i += phaseLength
        return ecm

    def getAgentPosition(mat):
        agentPosition = 0
        i = 0
        while i < len(mat):
            if mat[i] == 1:
                agentPosition = i
            i += 1
        return agentPosition

    def weights(strength):
        if strength > 100:
            strength = 100
        V = omega * strength
        weight = np.exp(V)
        return weight

    def print2D(mat):
        for row in mat:
            print(row)

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
            mem[i] = mem[i] - epsilon * mem[i]
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
            ecm = App.generateECM()
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
                mem = App.memoryReduction(mem)
                residence[agentPosition] = residence[agentPosition] + 1
                evolution[agentPosition] = step
            # values.append(agentPosition - int(matrixSize / 2))
        # msd = 0
        # for x in values:
        #     msd = msd + (x ** 2)
        # msd = msd / iterations
        # print(msd)



if __name__ == "__main__":
    App.main()
