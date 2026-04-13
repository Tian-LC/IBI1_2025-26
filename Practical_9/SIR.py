import numpy as np
import matplotlib.pyplot as plt
### init data ###
N = 10000
I = 1
S = N - 1
R = 0
beta = 0.3
gamma = 0.05
s_list = [S]
i_list = [I]
r_list = [R]

### time loop ###

# pseudocode
# for each loop:
#     p_infection = beta * (I/N)
#     new infectors =  random_infectors(p_infection)
#     p_recovery = gamma
#     new recoveries =  random_infectors(recovery)
#
#     add (Infectors + new infectors - new recoveries) into [I]
#     add (Recoveries + new recoveries) into [R]
#     add (Susceptible indiciduals - new infectors) into [S]
#     update the value of S I R

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
plt.figure(figsize=(6, 4), dpi=150)

plt.plot(s_list, label="susceptible")
plt.plot(i_list, label="infected")
plt.plot(r_list, label="recovered")

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()

plt.show()