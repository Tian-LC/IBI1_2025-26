#Calculate the percentage change 
UK = [66.7, 69.2, 'UK']
China = [1426.0, 1410.0, 'China']
Italy = [59.4, 58.9, 'Italy']
Brazil = [208.6, 212.0, 'Brazil']
USA = [331.6, 340.1, 'USA']
Countries = [UK,China,Italy,Brazil,USA]
for i in Countries:
    pop_change = ( i[1] - i[0] ) / i[0] * 100
    i.append(pop_change)
    print('the percentage population change of', i[2],'between 2020 and 2024 is', i[3],'%')
Countries_sorted = sorted(Countries, key=lambda x:x[3], reverse= True)
print('countries\tpercentage_change')
for i in range(5):
    print(Countries_sorted[i][2],'\t\t',Countries_sorted[i][3],'%')
print('the country with largest percentage_population_change is', Countries_sorted[0][2])
print('the country with lowest percentage_population_change is', Countries_sorted[4][2])
#draw a plot
percentage = []
Countries_name = []
for i in range(5): 
    percentage.append(Countries_sorted[i][3])
    Countries_name.append(Countries_sorted[i][2])
width = 0.35
import matplotlib.pyplot as plt
plot = plt.bar(Countries_name, percentage, width)
plt.xlabel = 'Countries'
plt.ylabel = 'Percentage population change(%)'
plt.ylim(-2, 5)
plt.axhline(y=0, color = 'black', linewidth = 0.5)
plt.show()