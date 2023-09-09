import random
import math
import matplotlib.pyplot as plt
import numpy as np
import sys

matrixSize = 101  # gets you a 21x21 matrix
iterations = 3
runtime = 5000
beta = 1  # bias towards up and right
epsilon = 0  # 0.01
numberOfAgents = 50
baselineAgents = []
testedAgents = []

b = (1 / (beta + 1)) / 2  # pU, pR
a = b * beta  # pD, pL

a = 1
b = 1


class Agent:
    def __init__(self, agentPosition, orientation, k, persistence, designation, omega, id):
        self.agentPosition = agentPosition
        self.orientation = orientation
        self.k = k
        self.persistence = persistence
        self.designation = designation
        self.omega = omega
        self.id = id

    def moveAgent(self, mat, mem, pU, pD, pL, pR, wU, wD, wL, wR):
        r = random.uniform(0, 1)
        mat[self.agentPosition[0]][self.agentPosition[1]] = 0
        if r <= pU:
            if self.agentPosition[0] != 0 and mat[self.agentPosition[0] - 1][self.agentPosition[1]] == 0:
                mat[self.agentPosition[0] - 1][self.agentPosition[1]] = self.designation
                mem[self.agentPosition[0] - 1][self.agentPosition[1]] += 1
                self.agentPosition[0] = self.agentPosition[0] - 1
                self.orientation = "U"
            else:
                self.moveAgent(mat, mem, 0, (wD * b * self.persistence[1]) / (
                        wD * b * self.persistence[1] + wL * b * self.persistence[2] + wR * a * self.persistence[
                    3]), (wL * b * self.persistence[2]) / (
                                       wD * b * self.persistence[1] + wL * b * self.persistence[2] + wR * a *
                                       self.persistence[3]), (wR * a * self.persistence[3]) / (
                                       wD * b * self.persistence[1] + wL * b * self.persistence[2] + wR * a *
                                       self.persistence[3]), wU, wD, wL, wR)
        elif pU < r <= pU + pD:
            if self.agentPosition[0] != matrixSize - 1 and mat[self.agentPosition[0] + 1][self.agentPosition[1]] == 0:
                mat[self.agentPosition[0] + 1][self.agentPosition[1]] = self.designation
                mem[self.agentPosition[0] + 1][self.agentPosition[1]] += 1
                self.agentPosition[0] = self.agentPosition[0] + 1
                self.orientation = "D"
            else:
                self.moveAgent(mat, mem, (wU * a * self.persistence[0]) / (
                        wU * a * self.persistence[0] + wL * b * self.persistence[2] + wR * a * self.persistence[
                    3]), 0, (wL * b * self.persistence[2]) / (
                                       wU * a * self.persistence[0] + wL * b * self.persistence[2] + wR * a *
                                       self.persistence[3]), (wR * a * self.persistence[3]) / (
                                       wU * a * self.persistence[0] + wL * b * self.persistence[2] + wR * a *
                                       self.persistence[3]), wU, wD, wL, wR)
        elif pU + pD < r <= pU + pD + pL:
            if self.agentPosition[1] != 0 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] == 0:
                mat[self.agentPosition[0]][self.agentPosition[1] - 1] = self.designation
                mem[self.agentPosition[0]][self.agentPosition[1] - 1] += 1
                self.agentPosition[1] = self.agentPosition[1] - 1
                self.orientation = "L"
            else:
                self.moveAgent(mat, mem, (wU * a * self.persistence[0]) / (
                        wU * a * self.persistence[0] + wD * b * self.persistence[1] + wR * a * self.persistence[
                    3]), (wD * b * self.persistence[1]) / (
                                       wU * a * self.persistence[0] + wD * b * self.persistence[1] + wR * a *
                                       self.persistence[3]), 0, (wR * a * self.persistence[3]) / (
                                       wU * a * self.persistence[0] + wD * b * self.persistence[1] + wR * a *
                                       self.persistence[3]), wU, wD, wL, wR)
        elif pU + pD + pL < r <= pU + pD + pL + pR:
            if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] == 0:
                mat[self.agentPosition[0]][self.agentPosition[1] + 1] = self.designation
                mem[self.agentPosition[0]][self.agentPosition[1] + 1] += 1
                self.agentPosition[1] = self.agentPosition[1] + 1
                self.orientation = "R"
            else:
                self.moveAgent(mat, mem, (wU * a * self.persistence[0]) / (
                        wU * a * self.persistence[0] + wD * b * self.persistence[1] + wL * b * self.persistence[
                    2]), (wD * b * self.persistence[1]) / (
                                       wU * a * self.persistence[0] + wD * b * self.persistence[1] + wL * b *
                                       self.persistence[2]), (wL * b * self.persistence[2]) / (
                                       wU * a * self.persistence[0] + wD * b * self.persistence[1] + wL * b *
                                       self.persistence[2]), 0, wU, wD, wL, wR)
        return mat

    def calculatePersistence(self):
        if self.orientation == "U":
            self.persistence[0] = 1 - 3 * (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
            self.persistence[1] = (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
            self.persistence[2] = (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
            self.persistence[3] = (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
        elif self.orientation == "D":
            self.persistence[0] = (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
            self.persistence[1] = 1 - 3 * (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
            self.persistence[2] = (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
            self.persistence[3] = (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
        elif self.orientation == "L":
            self.persistence[0] = (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
            self.persistence[1] = (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
            self.persistence[2] = 1 - 3 * (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
            self.persistence[3] = (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
        elif self.orientation == "R":
            self.persistence[0] = (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
            self.persistence[1] = (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
            self.persistence[2] = (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
            self.persistence[3] = 1 - 3 * (np.exp(-self.k) / (3 * np.exp(-self.k) + np.exp(self.k)))
        return self.persistence

    @staticmethod
    def weights(strength, omega):
        if strength > 100:
            strength = 100
        V = omega * strength
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

    def placeAgent(mat, mem):
        agentArray = []
        for place in range(numberOfAgents):
            done = False
            while not done:
                randomX = random.randint(int((matrixSize - 1) / 2 - 10), int((matrixSize - 1) / 2 + 10))
                randomY = random.randint(int((matrixSize - 1) / 2 - 10), int((matrixSize - 1) / 2 + 10))
                if mat[randomX][randomY] != 1 and mat[randomX][randomY] != 2:
                    if (place + 1) % 2 == 0:
                        mat[randomX][randomY] = 1
                        mem[randomX][randomY] = 1
                        agentArray.append(Agent([randomX, randomY], "U", 0.5, [0] * 4, 1, 0, place + 1))
                        done = True
                    elif (place + 1) % 2 == 1:
                        mat[randomX][randomY] = 2
                        mem[randomX][randomY] = 2
                        agentArray.append(Agent([randomX, randomY], "U", 0.5, [0] * 4, 2, 1.0, place + 1))
                        done = True
        return mat, mem, agentArray


def main():
    for _ in range(iterations):
        mat, mem, agentArray = Main.generateMatrix()
        Main.print2D(mat)
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
                mat = agent.moveAgent(mat, mem, a * ((wU * persistence[0]) / (
                        (a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                        a * wR * persistence[3]))), b * ((wD * persistence[1]) / (
                        (a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                        a * wR * persistence[3]))), b * ((wL * persistence[2]) / (
                        (a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                        a * wR * persistence[3]))), a * ((wR * persistence[3]) / (
                        (a * wU * persistence[0]) + (b * wD * persistence[1]) + (b * wL * persistence[2]) + (
                        a * wR * persistence[3]))), wU, wR, wD, wL)
        for agent in agentArray:
            if agent.designation == 1:
                baselineAgents.append(agent.agentPosition)
            else:
                testedAgents.append(agent.agentPosition)


main()
for a in range(len(baselineAgents)):
    print(baselineAgents[a][0])
print("\nY and X barrier\n")
for b in range(len(baselineAgents)):
    print(baselineAgents[b][1])
print("\n1 and 2 barrier\n")
for c in range(len(testedAgents)):
    print(testedAgents[c][0])
print("\nY and X barrier\n")
for d in range(len(testedAgents)):
    print(testedAgents[d][1])
