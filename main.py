import numpy as np
import matplotlib.pylab as plt
import time

def count(grid, x, y):
    sum = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            col = i % len(grid)
            row = j % len(grid)
            sum += grid[col][row]

    sum -= grid[x][y]
    return sum

length = 10
N = 10
#initGrid = np.array([[np.abs(int(np.random.normal(0,0.7))) for i in range(N)] for j in range(N)])
initGrid = np.random.randint(0,2, size=(length,length))
#initGrid = np.random.normal(0, 0.2, size=(length, length))

while True:
    plt.cla()
    newGrid = initGrid
    for i in range(length):
        for j in range(length):
            state = initGrid[i][j]
            neighbor = count(initGrid, i, j)
            if ( state == 0 and neighbor == 3):
                newGrid[i][j] = 1
            elif(state == 1 and (neighbor <2 or neighbor > 3)):
                newGrid[i][j] = 0
            else:
                newGrid[i][j] = state
    initGrid = newGrid
    plt.imshow(initGrid, cmap='gray_r');
    #plt.draw()
    plt.pause(.001)
