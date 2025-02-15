import random
import numpy as np
from pytictoc import TicToc

t = TicToc()

omega = 0.2
epsilon = 0.01
M_max = 100
alpha = 0.01
matrixSize = 1001
iterations = 1000

times = [
    0, 1, 2, 3, 4, 5, 6, 8, 10, 13, 16, 20, 25, 32, 40, 50, 63, 79, 100, 126, 158,
    200, 251, 316, 398, 501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012,
    6310, 7943, 10000, 12589, 15849, 19953, 25119, 31623, 39811, 50119, 63096, 79433,
    100000
]
values = {t: [] for t in times}

class App:
    @staticmethod
    def generateMatrix():
        mat = [0] * matrixSize
        # mat[math.floor(matrixSize / 2)] = 1
        return mat

    def memoryUpdate(mem, agentPosition):
        i = 0
        while i < len(mem):
            if i == agentPosition:
                delta = 1
            else:
                delta = 0
            mem[i] += (alpha / M_max) * (M_max - mem[i]) ** 2 * delta - epsilon * mem[i]
            i += 1
        return mem

    @staticmethod
    def getOrientation():
        return "L" if random.uniform(0, 1) <= 0.5 else "R"

    def moveAgent(mat, agentPosition, pL, pR, wL, wR):
        r = random.uniform(0, 1)
        if r < pL:
            if agentPosition != 0:
                mat[agentPosition - 1] = 1
                agentPosition = agentPosition - 1
                orientation = "L"
            else:
                print("oh no!")
                App.moveAgent(mat, agentPosition, 0, 1, wL, wR)
        elif pL < r <= pL + pR:
            if agentPosition != matrixSize - 1:
                mat[agentPosition + 1] = 1
                agentPosition = agentPosition + 1
                orientation = "R"
            else:
                print("oh no!")
                App.moveAgent(mat, agentPosition, 1, 0, wL, wR)
        return mat, agentPosition, orientation

    def print2D(mat):
        for row in mat:
            print(row)

    @staticmethod
    def main():
        for iteration in range(iterations):
            print(iteration)
            mat = App.generateMatrix()
            mem = App.generateMatrix()
            agentPosition = int(matrixSize / 2)
            mat[agentPosition] = 1
            for step in range(times[-1] + 1):
                try:
                    wL = np.exp(omega * mem[agentPosition - 1])
                except IndexError:
                    wL = 0
                try:
                    wR = np.exp(omega * mem[agentPosition + 1])
                except IndexError:
                    wR = 0
                mat[agentPosition] = 0
                mat, agentPosition, orientation = App.moveAgent(mat, agentPosition, wL / (wR + wL), wR / (wR + wL), wL, wR)
                mem = App.memoryUpdate(mem, agentPosition)
                if step in times:
                    values[step].append(agentPosition - matrixSize // 2)
        for time in times:
            msd = np.mean([x ** 2 for x in values[time]])
            mstd = np.mean([x ** 4 for x in values[time]])
            merr = np.sqrt((mstd - msd ** 2) / iterations)
            print(time, msd, merr)

if __name__ == "__main__":
    t.tic()
    App.main()
    t.toc()
