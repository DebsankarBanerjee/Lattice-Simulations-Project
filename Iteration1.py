import random

matrixSize = 10  # gets you a 5x5 matrix
iterations = 100
pU = 0.25
pD = 0.25
pL = 0.25
pR = 0.25


class App:
    @staticmethod
    def generateMatrix():
        mat = [[0] * matrixSize for _ in range(matrixSize)]
        # mat[random.randint(1, matrixSize - 1)][random.randint(1, matrixSize - 1)] = 1
        mat[0][0] = 1
        return mat

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

    def moveAgent(mat, agentPosition):
        r = random.uniform(0, 1)
        if r < pU:
            if agentPosition[0] != 0:
                mat[agentPosition[0] - 1][agentPosition[1]] = 1
            else:
                mat = App.moveAgent(mat, agentPosition)
        elif pU < r <= pU + pD:
            if agentPosition[0] != matrixSize - 1:
                mat[agentPosition[0] + 1][agentPosition[1]] = 1
            else:
                mat = App.moveAgent(mat, agentPosition)
        elif pU + pD < r <= pU + pD + pL:
            if agentPosition[1] != 0:
                mat[agentPosition[0]][agentPosition[1] - 1] = 1
            else:
                mat = App.moveAgent(mat, agentPosition)
        elif pU + pD + pL < r <= pU + pD + pL + pR:
            if agentPosition[1] != matrixSize - 1:
                mat[agentPosition[0]][agentPosition[1] + 1] = 1
            else:
                mat = App.moveAgent(mat, agentPosition)
        return mat

    def print2D(mat):
        for row in mat:
            print(row)

    @staticmethod
    def main():
        mat = App.generateMatrix()
        # trajectory = [[0] * (3) for _ in range(6)]
        App.print2D(mat)
        print("")
        for x in range(iterations):
            agentPosition = App.getAgentPosition(mat)
            # print("[" + str((x + 1)) + ", " + str(agentPosition[0]) + ", " + str(agentPosition[1]) + "]")
            # trajectory[x][0] = x + 1
            # trajectory[x][1] = agentPosition[0]
            # trajectory[x][2] = agentPosition[1]
            mat[agentPosition[0]][agentPosition[1]] = 0
            mat = App.moveAgent(mat, agentPosition)
        print("")
        App.print2D(mat)


if __name__ == "__main__":
    App.main()
