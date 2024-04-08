import random
import matplotlib.pyplot as plt
import numpy as np

matrixSize = 501
iterations = 250
beta = 1  # bias towards up and right
epsilon = 0.1  # 0.01
numberOfAgents = 8
k = 0
baselineAgents = []
testedAgents = []

times = np.logspace(0.1, 4.0, num=20)
for i in range(len(times)):
    times[i] = int(times[i])

bvalues1 = []
bvalues2 = []
bvalues3 = []
bvalues4 = []
bvalues5 = []
bvalues6 = []
bvalues7 = []
bvalues8 = []
bvalues9 = []
bvalues10 = []
bvalues11 = []
bvalues12 = []
bvalues13 = []
bvalues14 = []
bvalues15 = []
bvalues16 = []
bvalues17 = []
bvalues18 = []
bvalues19 = []
bvalues20 = []

tvalues1 = []
tvalues2 = []
tvalues3 = []
tvalues4 = []
tvalues5 = []
tvalues6 = []
tvalues7 = []
tvalues8 = []
tvalues9 = []
tvalues10 = []
tvalues11 = []
tvalues12 = []
tvalues13 = []
tvalues14 = []
tvalues15 = []
tvalues16 = []
tvalues17 = []
tvalues18 = []
tvalues19 = []
tvalues20 = []



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
        if self.agentPosition[0] == 0 or self.agentPosition[0] == matrixSize - 1 or self.agentPosition[1] == 0 or self.agentPosition == matrixSize - 1:
            print("Oh no!")
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
        if V > 709:
            V = 709
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

    def memoryReduction(mem):
        i = 0
        while i < len(mem):
            j = 0
            while j < len(mem[i]):
                if mem[i][j] > 0:
                    mem[i][j] -= epsilon * mem[i][j]
                j += 1
            i += 1
        return mem

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
                randomX = random.randint(int(matrixSize / 2) - 1, int(matrixSize / 2) + 1)
                randomY = random.randint(int(matrixSize / 2) - 1, int(matrixSize / 2) + 1)
                if mat[randomX][randomY] == 0:
                    if place % 2 == 0:
                        mat[randomX][randomY] = 1
                        mem[randomX][randomY] = 1
                        agentArray.append(Agent([randomX, randomY], Main.getOrientation(), [0] * 4, 1, 0))
                    else:
                        mat[randomX][randomY] = 2
                        mem[randomX][randomY] = 1
                        agentArray.append(Agent([randomX, randomY], Main.getOrientation(), [0] * 4, 2, 0.5))
                    done = True
        return mat, mem, agentArray


def main():
    for iteration in range(iterations):
        mat, mem, agentArray = Main.generateMatrix()
        print(iteration)
        for steps in range(int(times[18])):
            bmsd = 0
            tmsd = 0
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
                if agent.designation == 1:
                    bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                else:
                    tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (agent.agentPosition[1] - int(matrixSize / 2)) ** 2
            mem = Main.memoryReduction(mem)
            if steps == times[0] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues1.append(bmsd / (numberOfAgents / 2))
                tvalues1.append(tmsd / (numberOfAgents / 2))
            elif steps == times[1] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues2.append(bmsd / (numberOfAgents / 2))
                tvalues2.append(tmsd / (numberOfAgents / 2))
            elif steps == times[2] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues3.append(bmsd / (numberOfAgents / 2))
                tvalues3.append(tmsd / (numberOfAgents / 2))
            elif steps == times[3] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues4.append(bmsd / (numberOfAgents / 2))
                tvalues4.append(tmsd / (numberOfAgents / 2))
            elif steps == times[4] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues5.append(bmsd / (numberOfAgents / 2))
                tvalues5.append(tmsd / (numberOfAgents / 2))
            elif steps == times[5] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues6.append(bmsd / (numberOfAgents / 2))
                tvalues6.append(tmsd / (numberOfAgents / 2))
            elif steps == times[6] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues7.append(bmsd / (numberOfAgents / 2))
                tvalues7.append(tmsd / (numberOfAgents / 2))
            elif steps == times[7] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues8.append(bmsd / (numberOfAgents / 2))
                tvalues8.append(tmsd / (numberOfAgents / 2))
            elif steps == times[8] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues9.append(bmsd / (numberOfAgents / 2))
                tvalues9.append(tmsd / (numberOfAgents / 2))
            elif steps == times[9] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues10.append(bmsd / (numberOfAgents / 2))
                tvalues10.append(tmsd / (numberOfAgents / 2))
            elif steps == times[10] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues11.append(bmsd / (numberOfAgents / 2))
                tvalues11.append(tmsd / (numberOfAgents / 2))
            elif steps == times[11] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues12.append(bmsd / (numberOfAgents / 2))
                tvalues12.append(tmsd / (numberOfAgents / 2))
            elif steps == times[12] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues13.append(bmsd / (numberOfAgents / 2))
                tvalues13.append(tmsd / (numberOfAgents / 2))
            elif steps == times[13] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues14.append(bmsd / (numberOfAgents / 2))
                tvalues14.append(tmsd / (numberOfAgents / 2))
            elif steps == times[14] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues15.append(bmsd / (numberOfAgents / 2))
                tvalues15.append(tmsd / (numberOfAgents / 2))
            elif steps == times[15] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues16.append(bmsd / (numberOfAgents / 2))
                tvalues16.append(tmsd / (numberOfAgents / 2))
            elif steps == times[16] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues17.append(bmsd / (numberOfAgents / 2))
                tvalues17.append(tmsd / (numberOfAgents / 2))
            elif steps == times[17] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues18.append(bmsd / (numberOfAgents / 2))
                tvalues18.append(tmsd / (numberOfAgents / 2))
            elif steps == times[18] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues19.append(bmsd / (numberOfAgents / 2))
                tvalues19.append(tmsd / (numberOfAgents / 2))
            elif steps == times[19] - 1:
                bmsd = 0
                tmsd = 0
                for agent in agentArray:
                    if agent.designation == 1:
                        bmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                    else:
                        tmsd += (agent.agentPosition[0] - int(matrixSize / 2)) ** 2 + (
                                    agent.agentPosition[1] - int(matrixSize / 2)) ** 2
                bvalues20.append(bmsd / (numberOfAgents / 2))
                tvalues20.append(tmsd / (numberOfAgents / 2))
        # plt.imshow(mat)
        # plt.colorbar()
        # plt.show()


main()
b1avg = 0
for msd in bvalues1:
    b1avg += msd
print(b1avg / iterations)
b2avg = 0
for msd in bvalues2:
    b2avg += msd
print(b2avg / iterations)
b3avg = 0
for msd in bvalues3:
    b3avg += msd
print(b3avg / iterations)
b4avg = 0
for msd in bvalues4:
    b4avg += msd
print(b4avg / iterations)
b5avg = 0
for msd in bvalues5:
    b5avg += msd
print(b5avg / iterations)
b6avg = 0
for msd in bvalues6:
    b6avg += msd
print(b6avg / iterations)
b7avg = 0
for msd in bvalues7:
    b7avg += msd
print(b7avg / iterations)
b8avg = 0
for msd in bvalues8:
    b8avg += msd
print(b8avg / iterations)
b9avg = 0
for msd in bvalues9:
    b9avg += msd
print(b9avg / iterations)
b10avg = 0
for msd in bvalues10:
    b10avg += msd
print(b10avg / iterations)
b11avg = 0
for msd in bvalues11:
    b11avg += msd
print(b11avg / iterations)
b12avg = 0
for msd in bvalues12:
    b12avg += msd
print(b12avg / iterations)
b13avg = 0
for msd in bvalues13:
    b13avg += msd
print(b13avg / iterations)
b14avg = 0
for msd in bvalues14:
    b14avg += msd
print(b14avg / iterations)
b15avg = 0
for msd in bvalues15:
    b15avg += msd
print(b15avg / iterations)
b16avg = 0
for msd in bvalues16:
    b16avg += msd
print(b16avg / iterations)
b17avg = 0
for msd in bvalues17:
    b17avg += msd
print(b17avg / iterations)
b18avg = 0
for msd in bvalues18:
    b18avg += msd
print(b18avg / iterations)
b19avg = 0
for msd in bvalues19:
    b19avg += msd
print(b19avg / iterations)
b20avg = 0
for msd in bvalues20:
    b20avg += msd
print(b20avg)
print("\n")
t1avg = 0
for msd in tvalues1:
    t1avg += msd
print(t1avg / iterations)
t2avg = 0
for msd in tvalues2:
    t2avg += msd
print(t2avg / iterations)
t3avg = 0
for msd in tvalues3:
    t3avg += msd
print(t3avg / iterations)
t4avg = 0
for msd in tvalues4:
    t4avg += msd
print(t4avg / iterations)
t5avg = 0
for msd in tvalues5:
    t5avg += msd
print(t5avg / iterations)
t6avg = 0
for msd in tvalues6:
    t6avg += msd
print(t6avg / iterations)
t7avg = 0
for msd in tvalues7:
    t7avg += msd
print(t7avg / iterations)
t8avg = 0
for msd in tvalues8:
    t8avg += msd
print(t8avg / iterations)
t9avg = 0
for msd in tvalues9:
    t9avg += msd
print(t9avg / iterations)
t10avg = 0
for msd in tvalues10:
    t10avg += msd
print(t10avg / iterations)
t11avg = 0
for msd in tvalues11:
    t11avg += msd
print(t11avg / iterations)
t12avg = 0
for msd in tvalues12:
    t12avg += msd
print(t12avg / iterations)
t13avg = 0
for msd in tvalues13:
    t13avg += msd
print(t13avg / iterations)
t14avg = 0
for msd in tvalues14:
    t14avg += msd
print(t14avg / iterations)
t15avg = 0
for msd in tvalues15:
    t15avg += msd
print(t15avg / iterations)
t16avg = 0
for msd in tvalues16:
    t16avg += msd
print(t16avg / iterations)
t17avg = 0
for msd in tvalues17:
    t17avg += msd
print(t17avg / iterations)
t18avg = 0
for msd in tvalues18:
    t18avg += msd
print(t18avg / iterations)
t19avg = 0
for msd in tvalues19:
    t19avg += msd
print(t19avg / iterations)
t20avg = 0
for msd in tvalues20:
    t20avg += msd
print(t20avg / iterations)

