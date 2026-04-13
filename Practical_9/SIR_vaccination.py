import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
vaccination_rates = np.arange(0, 1.01, 0.1)
plt.figure(figsize=(6, 4), dpi=150)
colors = [
    "#440154",  
    "#482878",
    "#3E4989",  
    "#31688E",  
    "#26828E",  
    "#1F9E89",  
    "#35B779",  
    "#6DCD59",  
    "#B4DE2C",  
    "#DCE319",
    "#FDE725",  
]
for color_id,t in enumerate(vaccination_rates):
    N = 10000
    I = 1
    S =int( N - 1 - (N*t) )
    R = 0
    beta = 0.3
    gamma = 0.05
    s_list = [S]
    i_list = [I]
    r_list = [R]
    if t == 1.0:
        I = 0
        S = 0
### time loop ###
    for i in range(1000):
        p_infection = beta * (I/N)
        new_infectors = np.random.choice([0,1], size = S, p = [1-p_infection, p_infection]).sum()
        p_recovery = gamma
        new_recoveries = np.random.choice([0,1], size = I, p = [1-p_recovery, p_recovery]).sum()   
        I += (new_infectors-new_recoveries)
        R += new_recoveries
        S -= new_infectors
        s_list.append(S)
        i_list.append(I)
        r_list.append(R)
    ### drawing a plot ###
    plt.plot(i_list, label=f"{int(t * 100)}%", color=colors[color_id])

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()
plt.show()
