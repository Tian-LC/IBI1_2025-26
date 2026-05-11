import numpy as np
import matplotlib.pyplot as plt

beta = 0.3
gamma = 0.05
population = np.zeros((100, 100), dtype=int)
 ### TRY: considering vaccination ###

# Select vaccinated individuals without replacement.
# The 100 x 100 grid contains 10000 positions, so each position is first
# represented by a unique number from 0 to 9999.
# Using replace=False prevents the same individual from being selected twice,
# so the actual number of vaccinated individuals is exactly 1000.
# Each selected number is then converted back to x and y coordinates.
vaccinated = np.random.choice(range(10000), 1000, replace=False)

for v in vaccinated:
    x = v // 100
    y = v % 100
    population[x, y] = 2

while True:
    outbreak = np.random.choice(range(100), 2)
    if population[outbreak[0], outbreak[1]] == 0:
        population[outbreak[0], outbreak[1]] = 1
        break

# plot time = 0 before the loop
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap="viridis", interpolation="nearest")
plt.title("time = 0")
plt.colorbar()
plt.show()
for t in range(101): #100 time loops
    
    # copy, to make the recovery and infection process happen at the same time
    new_population = population.copy()

    #  infection snippet
    infectedIndex = np.where(population == 1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]

        for xNeighbour in range(x - 1, x + 2):
            for yNeighbour in range(y - 1, y + 2):
                # infect each neighbour with probability beta
                if (xNeighbour, yNeighbour) != (x, y):
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100: # make sure I don't fall off an edge
                        if population[xNeighbour, yNeighbour] == 0:  # only infect neighbours that are not already infected!
                            new_population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]

        # recovery
        if population[x,y] == 1:
            new_population[x,y]=np.random.choice([1,2],1,p=[1-gamma,gamma])[0]
    #update the population (to make the recovery process and infection process at the same time)
    population = new_population
    # plot
    if t in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"time = {t}")
        plt.colorbar()
        plt.show()

