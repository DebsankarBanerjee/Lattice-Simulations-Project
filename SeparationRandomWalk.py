import random
import math
import matplotlib.pyplot as plt
import numpy as np

matrixSize = 101  # gets you a 21x21 matrix
iterations = 1
runtime = 5000
beta = 1  # bias towards up and right
alpha = 1  # 1 for attracting random-walk, -1 for repulsing
epsilon = 0  # 0.01
k = 0
numberOfAgents = 30
agentArray = []

b = (1 / (beta + 1)) / 2  # pU, pR
a = b * beta  # pD, pL


class Agent:
    def __init__(self, agentPosition, orientation, persistence, designation, omega):
        self.agentPosition = agentPosition
        self.orientation = orientation
        self.persistence = persistence
        self.designation = designation
        self.omega = omega

    def moveAgent(self, mat, mem, pU, pD, pL, pR, wU, wD, wL, wR):
        r = np.float64(random.uniform(0, 1))
        mat[self.agentPosition[0]][self.agentPosition[1]] = 0
        if r <= pU:
            if self.agentPosition[0] != 0 and mat[self.agentPosition[0] - 1][self.agentPosition[1]] != 1 and mat[self.agentPosition[0] - 1][self.agentPosition[1]] != 2:
                if self.designation == 1:
                    mat[self.agentPosition[0] - 1][self.agentPosition[1]] = 1
                elif self.designation == 2:
                    mat[self.agentPosition[0] - 1][self.agentPosition[1]] = 2
                mem[self.agentPosition[0] - 1][self.agentPosition[1]] += 1
                self.agentPosition[0] = self.agentPosition[0] - 1
                self.orientation = "U"
                # print("up")
            else:
                self.moveAgent(mat, mem, 0, (wD * b * self.persistence[1]) / (
                        wD * b * self.persistence[1] + wL * b * self.persistence[2] + wR * a * self.persistence[
                    3]), (wL * b * self.persistence[2]) / (
                                       wD * b * self.persistence[1] + wL * b * self.persistence[2] + wR * a *
                                       self.persistence[3]), (wR * a * self.persistence[3]) / (
                                       wD * b * self.persistence[1] + wL * b * self.persistence[2] + wR * a *
                                       self.persistence[3]), wU, wD, wL, wR)
        elif pU < r <= pU + pD:
            if self.agentPosition[0] != matrixSize - 1 and mat[self.agentPosition[0] + 1][self.agentPosition[1]] != 1 and mat[self.agentPosition[0] + 1][self.agentPosition[1]] != 2:
                if self.designation == 1:
                    mat[self.agentPosition[0] + 1][self.agentPosition[1]] = 1
                elif self.designation == 2:
                    mat[self.agentPosition[0] + 1][self.agentPosition[1]] = 2
                mem[self.agentPosition[0] + 1][self.agentPosition[1]] += 1
                self.agentPosition[0] = self.agentPosition[0] + 1
                self.orientation = "D"
                # print("down")
            else:
                self.moveAgent(mat, mem, (wU * a * self.persistence[0]) / (
                        wU * a * self.persistence[0] + wL * b * self.persistence[2] + wR * a * self.persistence[
                    3]), 0, (wL * b * self.persistence[2]) / (
                                       wU * a * self.persistence[0] + wL * b * self.persistence[2] + wR * a *
                                       self.persistence[3]), (wR * a * self.persistence[3]) / (
                                       wU * a * self.persistence[0] + wL * b * self.persistence[2] + wR * a *
                                       self.persistence[3]), wU, wD, wL, wR)
        elif pU + pD < r <= pU + pD + pL:
            if self.agentPosition[1] != 0 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] != 1 and mat[self.agentPosition[0]][self.agentPosition[1] - 1] != 2:
                if self.designation == 1:
                    mat[self.agentPosition[0]][self.agentPosition[1] - 1] = 1
                elif self.designation == 2:
                    mat[self.agentPosition[0]][self.agentPosition[1] - 1] = 2
                mem[self.agentPosition[0]][self.agentPosition[1] - 1] += 1
                self.agentPosition[1] = self.agentPosition[1] - 1
                self.orientation = "L"
                # print("left")
            else:
                self.moveAgent(mat, mem, (wU * a * self.persistence[0]) / (
                        wU * a * self.persistence[0] + wD * b * self.persistence[1] + wR * a * self.persistence[
                    3]), (wD * b * self.persistence[1]) / (
                                       wU * a * self.persistence[0] + wD * b * self.persistence[1] + wR * a *
                                       self.persistence[3]), 0, (wR * a * self.persistence[3]) / (
                                       wU * a * self.persistence[0] + wD * b * self.persistence[1] + wR * a *
                                       self.persistence[3]), wU, wD, wL, wR)
        elif pU + pD + pL < r <= pU + pD + pL + pR:
            if self.agentPosition[1] != matrixSize - 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] != 1 and mat[self.agentPosition[0]][self.agentPosition[1] + 1] != 2:
                if self.designation == 1:
                    mat[self.agentPosition[0]][self.agentPosition[1] + 1] = 1
                elif self.designation == 2:
                    mat[self.agentPosition[0]][self.agentPosition[1] + 1] = 2
                mem[self.agentPosition[0]][self.agentPosition[1] + 1] += 1
                self.agentPosition[1] = self.agentPosition[1] + 1
                self.orientation = "R"
                # print("right")
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
        weight = np.exp(V)
        return weight


class Main:
    @staticmethod
    def generateMatrix():
        mat = [[0] * matrixSize for _ in range(matrixSize)]
        mem = [[0] * matrixSize for _ in range(matrixSize)]
        mat, mem = Main.placeAgent(mat, mem)
        return mat, mem

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
        for place in range(numberOfAgents):
            done = False
            while not done:
                randomX = random.randint(45, 55)
                randomY = random.randint(45, 55)
                if mat[randomX][randomY] != 1 and mat[randomX][randomY] != 2:
                    if place % 2 == 0:
                        mat[randomX][randomY] = 1
                        mem[randomX][randomY] = 1
                        agentArray.append(Agent([randomX, randomY], "U", [0] * 4, 1, 0))
                        done = True
                    elif place % 2 == 1:
                        mat[randomX][randomY] = 2
                        mem[randomX][randomY] = 2
                        agentArray.append(Agent([randomX, randomY], "U", [0] * 4, 2, 1))
                        done = True
        return mat, mem


def main():
    for _ in range(iterations):
        mat, mem = Main.generateMatrix()
        for _ in range(runtime):
            for agent in agentArray:
                try:
                    wU = agent.weights(mem[agent.agentPosition[0] - 1][agent.agentPosition[1]], agent.omega)
                    if wU > 5000:
                        wU = 5000
                except IndexError:
                    wU = 0
                try:
                    wD = agent.weights(mem[agent.agentPosition[0] + 1][agent.agentPosition[1]], agent.omega)
                    if wD > 5000:
                        wD = 5000
                except IndexError:
                    wD = 0
                try:
                    wL = agent.weights(mem[agent.agentPosition[0]][agent.agentPosition[1] - 1], agent.omega)
                    if wL > 5000:
                        wL = 5000
                except IndexError:
                    wL = 0
                try:
                    wR = agent.weights(mem[agent.agentPosition[0]][agent.agentPosition[1] + 1], agent.omega)
                    if wR > 5000:
                        wR = 5000
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
        plt.imshow(mat)
        plt.colorbar()
        plt.show()
    for agent in agentArray:
        if agent.designation == 1:
            print(agent.agentPosition[0])
    print("\nY and X barrier\n")
    for agent in agentArray:
        if agent.designation == 1:
            print(agent.agentPosition[1])
    print("\n1 and 2 barrier\n")
    for agent in agentArray:
        if agent.designation == 2:
            print(agent.agentPosition[0])
    print("\nY and X barrier\n")
    for agent in agentArray:
        if agent.designation == 2:
            print(agent.agentPosition[1])


main()
