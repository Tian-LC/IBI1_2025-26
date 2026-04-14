import numpy as np
import matplotlib.pyplot as plt

beta = 0.3
gamma = 0.05
population = np.zeros((100, 100), dtype=int)
x_vacc = np.random.choice(range(100), 1000)
y_vacc = np.random.choice(range(100), 1000)

for j in range(1000):
    population[x_vacc[j], y_vacc[j]] = 2

while True:
    outbreak = np.random.choice(range(100), 2)
    if population[outbreak[0], outbreak[1]] == 0:
        population[outbreak[0], outbreak[1]] = 1
        break

for t in range(101):
    
    # recovery 先复制一份
    new_population = population.copy()

    #  infection snippet
    infectedIndex = np.where(population == 1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]

        for xNeighbour in range(x - 1, x + 2):
            for yNeighbour in range(y - 1, y + 2):
                if (xNeighbour, yNeighbour) != (x, y):
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        if population[xNeighbour, yNeighbour] == 0:
                            new_population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]

        # recovery
        if population[x,y] == 1:
            new_population[x,y]=np.random.choice([1,2],1,p=[1-gamma,gamma])[0]
        #update the population
        population = new_population
    # 画图
    if t in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"time = {t}")
        plt.colorbar()
        plt.show()

