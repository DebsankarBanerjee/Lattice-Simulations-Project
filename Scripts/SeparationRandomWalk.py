import random
import math
import matplotlib.pyplot as plt
import numpy as np
import sys

matrixSize = 101 
iterations = 1
runtime = 10000
epsilon = 0
numberOfAgents = 50
k = 0
baselineAgents = []
testedAgents = []


class Agent:
    def __init__(self, agentPosition, orientation, persistence, designation, omega):
        self.agentPosition = agentPosition
        self.orientation = orientation
        self.persistence = persistence
        self.designation = designation
        self.omega = omega

    def moveAgent(self, mat, mem, pU, pD, pL, pR, wU, wD, wL, wR):
        r = random.uniform(0, 1)
        mat[self.agentPosition[0]][self.agentPosition[1]] = 0
        if r <= pU:
            if self.agentPosition[0] != 0 and mat[self.agentPosition[0] - 1][self.agentPosition[1]] == 0:
                mat[self.agentPosition[0] - 1][self.agentPosition[1]] = self.designation
                mem[self.agentPosition[0] - 1][self.agentPosition[1]] += 1
                self.agentPosition[0] = self.agentPosition[0] - 1
                self.orientation = "U"
            elif self.agentPosition[0] != matrixSize - 1 and mat[self.agentPosition[0] + 1][self.agentPosition[1]] == 0:
                if self.agentPosition[1] != 0 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] == 0:
                    if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0:
                        self.moveAgent(mat, mem, 0, (wD * self.persistence[1]) / (wD * self.persistence[1] + wL * self.persistence[2] + wR * self.persistence[3]),
                                       (wL * self.persistence[2]) / (wD * self.persistence[1] + wL * self.persistence[2] + wR * self.persistence[3]),
                                       (wR * self.persistence[3]) / (wD * self.persistence[1] + wL * self.persistence[2] + wR * self.persistence[3]), wU, wD, wL, wR)
                    else:
                        self.moveAgent(mat, mem, 0, (wD * self.persistence[1]) / (wD * self.persistence[1] + wL * self.persistence[2]),
                                       (wL * self.persistence[2]) / (wD * self.persistence[1] + wL * self.persistence[2]), 0, wU, wD, wL, wR)
                else:
                    if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0:
                        self.moveAgent(mat, mem, 0, (wD * self.persistence[1]) / (wD * self.persistence[1] + wR * self.persistence[3]), 0,
                                       (wR * self.persistence[3]) / (wD * self.persistence[1] + wR * self.persistence[3]), wU, wD, wL, wR)
                    else:
                        self.moveAgent(mat, mem, 0, 1, 0, 0, wU, wD, wL, wR)
            else:
                if (self.agentPosition[1] != 0 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] == 0) and (self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0):
                    self.moveAgent(mat, mem, 0, 0, (wL * self.persistence[2]) / (wL * self.persistence[2] + wR * self.persistence[3]),
                                   (wR * self.persistence[3]) / (wL * self.persistence[2] + wR * self.persistence[3]), wU, wD, wL, wR)
                else:
                    if self.agentPosition[1] != 0 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] == 0:
                        self.moveAgent(mat, mem, 0, 0, 1, 0, wU, wD, wL, wR)
                    else:
                        if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0:
                            self.moveAgent(mat, mem, 0, 0, 0, 1, wU, wD, wL, wR)
        elif pU < r <= pU + pD:
            if self.agentPosition[0] != matrixSize - 1 and mat[self.agentPosition[0] + 1][self.agentPosition[1]] == 0:
                mat[self.agentPosition[0] + 1][self.agentPosition[1]] = self.designation
                mem[self.agentPosition[0] + 1][self.agentPosition[1]] += 1
                self.agentPosition[0] = self.agentPosition[0] + 1
                self.orientation = "D"
            elif self.agentPosition[0] != 0 and mat[self.agentPosition[0] - 1][self.agentPosition[1]] == 0:
                if self.agentPosition[1] != 0 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] == 0:
                    if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0:
                        self.moveAgent(mat, mem, (wU * self.persistence[0]) / (wU * self.persistence[0] + wL * self.persistence[2] + wR * self.persistence[3]),
                                       0, (wL * self.persistence[2]) / (wU * self.persistence[0] + wL * self.persistence[2] + wR * self.persistence[3]),
                                       (wR * self.persistence[3]) / (wU * self.persistence[0] + wL * self.persistence[2] + wR * self.persistence[3]), wU, wD, wL, wR)
                    else:
                        self.moveAgent(mat, mem, (wU * self.persistence[0]) / (wU * self.persistence[0] + wL * self.persistence[2]), 0,
                                       (wL * self.persistence[2]) / (wU * self.persistence[0] + wL * self.persistence[2]), 0, wU, wD, wL, wR)
                else:
                    if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0:
                        self.moveAgent(mat, mem, (wU * self.persistence[0]) / (wU * self.persistence[0] + wR * self.persistence[3]), 0, 0,
                                       (wR * self.persistence[3]) / (wU * self.persistence[0] + wR * self.persistence[3]), wU, wD, wL, wR)
                    else:
                        self.moveAgent(mat, mem, 1, 0, 0, 0, wU, wD, wL, wR)
            else:
                if (self.agentPosition != 0 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] == 0) and (self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0):
                    self.moveAgent(mat, mem, 0, 0, (wL * self.persistence[2]) / (wL * self.persistence[2] + wR * self.persistence[3]),
                                   (wR * self.persistence[3]) / (wL * self.persistence[2] + wR * self.persistence[3]), wU, wD, wL, wR)
                else:
                    if self.agentPosition[1] != 0 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] == 0:
                        self.moveAgent(mat, mem, 0, 0, 1, 0, wU, wD, wL, wR)
                    else:
                        if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0:
                            self.moveAgent(mat, mem, 0, 0, 0, 1, wU, wD, wL, wR)
        elif pU + pD < r <= pU + pD + pL:
            if self.agentPosition[1] != 0 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] == 0:
                mat[self.agentPosition[0]][self.agentPosition[1] - 1] = self.designation
                mem[self.agentPosition[0]][self.agentPosition[1] - 1] += 1
                self.agentPosition[1] = self.agentPosition[1] - 1
                self.orientation = "L"
            elif self.agentPosition[0] != 0 and mat[self.agentPosition[0] - 1][self.agentPosition[1]] == 0:
                if self.agentPosition[0] != matrixSize - 1 and mat[self.agentPosition[0] + 1][self.agentPosition[1]] == 0:
                    if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0:
                        self.moveAgent(mat, mem, (wU * self.persistence[0]) / (wU * self.persistence[0] + wD * self.persistence[1] + wR * self.persistence[3]),
                                       (wD * self.persistence[1]) / (wU * self.persistence[0] + wD * self.persistence[1] + wR * self.persistence[3]), 0,
                                       (wR * self.persistence[3]) / (wU * self.persistence[0] + wD * self.persistence[1] + wR * self.persistence[3]), wU, wD, wL, wR)
                    else:
                        self.moveAgent(mat, mem, (wU * self.persistence[0]) / (wU * self.persistence[0] + wD * self.persistence[1]),
                                  (wD * self.persistence[1]) / (wU * self.persistence[0] + wD * self.persistence[1]), 0, 0, wU, wD, wL, wR)
                else:
                    if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0:
                        self.moveAgent(mat, mem, (wU * self.persistence[0]) / (wU * self.persistence[0] + wR * self.persistence[3]), 0, 0,
                                       (wR * self.persistence[3]) / (wU * self.persistence[0] + wR * self.persistence[3]), wU, wD, wL, wR)
                    else:
                        self.moveAgent(mat, mem, 1, 0, 0, 0, wU, wD, wL, wR)
            else:
                if (self.agentPosition[0] != matrixSize - 1 and mat[self.agentPosition[0] + 1][self.agentPosition[1]] == 0) and (self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0):
                    self.moveAgent(mat, mem, 0, (wD * self.persistence[1]) / (wD * self.persistence[1] + wR * self.persistence[3]), 0,
                                   (wR * self.persistence[3]) / (wD * self.persistence[1] + wR * self.persistence[3]), wU, wD, wL, wR)
                else:
                    if self.agentPosition[0] != matrixSize - 1 and mat[self.agentPosition[0] + 1][self.agentPosition[1]] == 0:
                        self.moveAgent(mat, mem, 0, 1, 0, 0, wU, wD, wL, wR)
                    else:
                        if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0:
                            self.moveAgent(mat, mem, 0, 0, 0, 1, wU, wD, wL, wR)
        elif pU + pD + pL < r <= pU + pD + pL + pR:
            if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0:
                mat[self.agentPosition[0]][self.agentPosition[1] + 1] = self.designation
                mem[self.agentPosition[0]][self.agentPosition[1] + 1] += 1
                self.agentPosition[1] = self.agentPosition[1] + 1
                self.orientation = "R"
            elif self.agentPosition[0] != 0 and mat[self.agentPosition[0] - 1][self.agentPosition[1]] == 0:
                if self.agentPosition[1] != 0 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] == 0:
                    if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0:
                        self.moveAgent(mat, mem, (wU * self.persistence[0]) / (wU * self.persistence[0] + wD * self.persistence[1] + wL * self.persistence[2]),
                                       (wD * self.persistence[1]) / (wU * self.persistence[0] + wD * self.persistence[1] + wL * self.persistence[2]),
                                       (wL * self.persistence[2]) / (wU * self.persistence[0] + wD * self.persistence[1] + wL * self.persistence[2]), 0, wU, wD, wL, wR)
                    else:
                        self.moveAgent(mat, mem, (wU * self.persistence[0]) / (wU * self.persistence[0] + wD * self.persistence[1]),
                                       (wD * self.persistence[1]) / (wU * self.persistence[0] + wD * self.persistence[1]), 0, 0, wU, wD, wL, wR)
                else:
                    if self.agentPosition[1] != 0 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] == 0:
                        self.moveAgent(mat, mem, (wU * self.persistence[0]) / (wU * self.persistence[0] + wL * self.persistence[2]), 0,
                                       (wL * self.persistence[2]) / (wU * self.persistence[0] + wL * self.persistence[2]), 0, wU, wD, wL, wR)
                    else:
                        self.moveAgent(mat, mem, 1, 0, 0, 0, wU, wD, wL, wR)
            else:
                if (self.agentPosition[0] != matrixSize - 1 and mat[self.agentPosition[0] + 1][self.agentPosition[1]] == 0) and (self.agentPosition[1] != 0 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] == 0):
                    self.moveAgent(mat, mem, 0, (wD * self.persistence[1]) / (wD * self.persistence[1] + wL * self.persistence[2]),
                                   (wL * self.persistence[2]) / (wD * self.persistence[1] + wL * self.persistence[2]), 0, wU, wD, wL, wR)
                else:
                    if self.agentPosition[0] != matrixSize - 1 and mat[self.agentPosition[0] + 1][self.agentPosition[1]] == 0:
                        self.moveAgent(mat, mem, 0, 1, 0, 0, wU, wD, wL, wR)
                    else:
                        self.moveAgent(mat, mem, 0, 0, 1, 0, wU, wD, wL, wR)
        return mat, mem, self.agentPosition

    def calculatePersistence(self):
        if self.orientation == "U":
            self.persistence[0] = 1 - 3 * (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            self.persistence[1] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            self.persistence[2] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            self.persistence[3] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
        elif self.orientation == "D":
            self.persistence[0] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            self.persistence[1] = 1 - 3 * (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            self.persistence[2] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            self.persistence[3] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
        elif self.orientation == "L":
            self.persistence[0] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            self.persistence[1] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            self.persistence[2] = 1 - 3 * (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            self.persistence[3] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
        elif self.orientation == "R":
            self.persistence[0] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            self.persistence[1] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            self.persistence[2] = (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
            self.persistence[3] = 1 - 3 * (np.exp(-k) / (3 * np.exp(-k) + np.exp(k)))
        return self.persistence

    @staticmethod
    def weights(strength, omega):
        V = omega * strength
        if V > 20:
            V = 20
        # if V > 709:
        #     V = 709
        weight = np.exp(V)
        return weight


class Main:
    @staticmethod
    def generateMatrix():
        mat = [[0] * matrixSize for _ in range(matrixSize)]
        mem = [[0] * matrixSize for _ in range(matrixSize)]
        mat, mem, agentArray = Main.placeAgent(mat, mem)
        return mat, mem, agentArray

    def print2D(mat):
        for row in mat:
            print(row)

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

    def placeAgent(mat, mem):
        agentArray = []
        for place in range(numberOfAgents):
            done = False
            while not done:
                randomX = random.randint((matrixSize - 1) / 2 - 5, (matrixSize - 1) / 2 + 5)
                randomY = random.randint((matrixSize - 1) / 2 - 5, (matrixSize - 1) / 2 + 5)
                if mat[randomX][randomY] != 1 and mat[randomX][randomY] != 2:
                    if (place + 1) % 2 == 0:
                        mat[randomX][randomY] = 1
                        mem[randomX][randomY] = 1
                        agentArray.append(Agent([randomX, randomY], Main.getOrientation(), [0] * 4, 1, 0.2))
                        done = True
                    elif (place + 1) % 2 == 1:
                        mat[randomX][randomY] = 2
                        mem[randomX][randomY] = 1
                        agentArray.append(Agent([randomX, randomY], Main.getOrientation(), [0] * 4, 2, 0.2))
                        done = True
        return mat, mem, agentArray


def main():
    for _ in range(iterations):
        mat, mem, agentArray = Main.generateMatrix()
        for _ in range(runtime):
            for agent in agentArray:
                try:
                    wU = agent.weights(mem[agent.agentPosition[0] - 1][agent.agentPosition[1]], agent.omega)
                except IndexError:
                    wU = 0
                try:
                    wD = agent.weights(mem[agent.agentPosition[0] + 1][agent.agentPosition[1]], agent.omega)
                except IndexError:
                    wD = 0
                try:
                    wL = agent.weights(mem[agent.agentPosition[0]][agent.agentPosition[1] - 1], agent.omega)
                except IndexError:
                    wL = 0
                try:
                    wR = agent.weights(mem[agent.agentPosition[0]][agent.agentPosition[1] + 1], agent.omega)
                except IndexError:
                    wR = 0
                persistence = agent.calculatePersistence()
                mat, mem, agentPosition = agent.moveAgent(mat, mem, (wU * persistence[0]) / (
                        (wU * persistence[0]) + (wD * persistence[1]) + (wL * persistence[2]) +
                        (wR * persistence[3])), (wD * persistence[1]) / (
                        (wU * persistence[0]) + (wD * persistence[1]) + (wL * persistence[2]) +
                        (wR * persistence[3])), (wL * persistence[2]) / (
                        (wU * persistence[0]) + (wD * persistence[1]) + (wL * persistence[2]) +
                        (wR * persistence[3])), (wR * persistence[3]) / (
                        (wU * persistence[0]) + (wD * persistence[1]) + (wL * persistence[2]) +
                        (wR * persistence[3])), wU, wD, wL, wR)
                agent.agentPosition = agentPosition
        for agent in agentArray:
            if agent.designation == 1:
                baselineAgents.append(agent.agentPosition)
            else:
                testedAgents.append(agent.agentPosition)
        plt.imshow(mat)
        plt.colorbar()
        plt.show()


main()
for d in range(len(testedAgents)):
    print(testedAgents[d][1])
print("\n2 and 1 barrier\n")
for b in range(len(baselineAgents)):
    print(baselineAgents[b][1])


