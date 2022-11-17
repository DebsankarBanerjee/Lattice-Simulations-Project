import random


def  generateMatrix() :
    mat = [[0] * (5) for _ in range(5)]
    mat[random.randint(1, 4)][random.randint(1, 4)] = 1
    return mat

def  getAgentPosition( mat) :
    agentPosition = [0] * (2)
    i = 0
    while (i < len(mat)) :
        j = 0
        while (j < len(mat[i])) :
            if (mat[i][j] == 1) :
                agentPosition[0] = i
                agentPosition[1] = j
            j += 1
        i += 1
    return agentPosition

def  moveAgent( mat,  agentPosition) :
    pU = 0.25
    pD = 0.25
    pL = 0.25
    pR = 0.25
    r = random.uniform(0, 1)
    if (r < pU) :
        if (agentPosition[0] != 0) :
            mat[agentPosition[0] - 1][agentPosition[1]] = 1
   print(“Up”)
        else :
            mat = App.moveAgent(mat, agentPosition)
    elif(pU < r and r <= pU + pD) :
        if (agentPosition[0] != 4) :
            mat[agentPosition[0] + 1][agentPosition[1]] = 1
   print(“Down”)
        else :
            mat = App.moveAgent(mat, agentPosition)
    elif(pU + pD < r and r <= pU + pD + pL) :
        if (agentPosition[1] != 0) :
            mat[agentPosition[0]][agentPosition[1] - 1] = 1
   print(“Left”)
        else :
            mat = App.moveAgent(mat, agentPosition)
    elif(pU + pD + pL < r and r <= pU + pD + pL + pR) :
        if (agentPosition[1] != 4) :
            mat[agentPosition[0]][agentPosition[1] + 1] = 1
  print(“Right”)
        else :
            mat = App.moveAgent(mat, agentPosition)
    return mat

def print2D( mat) :
    for row in mat :
        print(row)
@staticmethod
def main( args) :
    mat = App.generateMatrix()
    # trajectory = [[0] * (3) for _ in range(6)]
    App.print2D(mat)
    print("")
    time = 0
    while (time < 5) :
        agentPosition = App.getAgentPosition(mat)
        # print("[" + str((time + 1)) + ", " + str(agentPosition[0]) + ", " + str(agentPosition[1]) + "]")
        # trajectory[time][0] = time + 1
        # trajectory[time][1] = agentPosition[0]
        # trajectory[time][2] = agentPosition[1]
        mat[agentPosition[0]][agentPosition[1]] = 0
        mat = App.moveAgent(mat, agentPosition)
        time += 1
    print("")
    App.print2D(mat)



if __name__=="__main__":
App.main([])
