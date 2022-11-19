This iteration simulates the random walk of an agent populated in a matrix. 

The user can vary the size of the matrix and the number of times that the agent is allowed to move. The probability of the agent moving in a certain direction can be changed, but it is imperative that the sum of the probabilities remains 1. 

The program first builds the matrix using the matrixSize number desired by the user. It then places an agent at a random location within the matrix and then returns the matrix. This is completed in the generateMatrix() function.

To be able to move the agent, the program must know the location of the agent within the matrix. Since this is randomized, it is not known from the beginning, and thus a function is needed to locate the agent within the matrix. The function getAgentPosition(mat) searches the matrix for the agent and then returns its position (i, j) in the array agentPosition. 

The program moves the agent in the moveAgent(mat, agentPosition) function. A random number between 0 and 1 'r' is generated. It is then compared to the probabilities of movement to see in which direction it will move. The agent's current position is returned to its original state and its new location is populated. 

To print the initial and final arrays for reference to confirm the agent's movement, the function print2D(mat) is included. Furthermore, every time the agent moves its direction of movement is printed to the console. The user can map out the agent's movement and confirm. The array 'trajectory' is included for plotting purposes. It stores the time and position (i, j) of the agent in each iteration. 
