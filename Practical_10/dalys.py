import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/ASUS/Desktop/Bioinformatic_workspace/IBI1/IBI1_2025-26/Practical_10")

#try "pwd/ls" in python
#os.getcwd()
#os.listdir()

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")  #import dataset
#print(dalys_data.head(5))  #to see the first 5 rows
#dalys_data.info()  # to see basic informations
#print(dalys_data.describe())  #to see descriptive informations

#task1: show the max and min years and DALYs 
max_year = dalys_data["Year"].describe()["max"]
min_year = dalys_data["Year"].describe()["min"]
max_DALYs = dalys_data["DALYs"].describe()["max"]
min_DALYs = dalys_data["DALYs"].describe()["min"]
print("Task1:")
print("The maximum DALYs is", max_DALYs)
print("The minimum DALYs is", min_DALYs)
print("The first recorded year is", min_year)
print("The most recent year is", max_year)

#dalys_data.iloc[0,3]  #to se the element in the first row and the fourth column
#dalys_data.head(1)  #to check if the "iloc" command works

#Task2:show the first 10 rows and the third and fourth column
print("Task2:")
first_10_rows = dalys_data.iloc[0:10,2:4]  #the answer is Year 1998, which will be confirm in following commands
AFG_first_10 = dalys_data.loc[dalys_data["Entity"] == "Afghanistan", ["Year","DALYs"]].head(10)
AFG_max_row = AFG_first_10.loc[AFG_first_10["DALYs"].idxmax()]
print("The first 10 rows are:\n",first_10_rows.to_string(index = False))
print("Across the first 10 years for which DALYs were recorded in Afghanistan, Year", int(AFG_max_row["Year"]), "reported the maximum DALYs")

#Task3:find all rows whose "Entity" column is "Zimbabwe"
print("Task3:")
#create the bool list to mark which row is needed
Bool_list = []
for i in dalys_data["Entity"]:
    if i == "Zimbabwe":
        Bool_list.append(True)
    else:
        Bool_list.append(False)
Zimbabwe = dalys_data.loc[Bool_list,:]
print(Zimbabwe)
#This task can also be done like this: print(dalys_data.loc[dalys_data["Entity"] == "Zimbabwe"]) or we can delete ".loc" in this command

#Task4: compute the countries with the maximum and mimumum DALYs in 2019
print("Task4:")
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
max_country_2019 = recent_data.loc[recent_data["DALYs"].idxmax(),"Entity"] #the answer is Lesotho
min_country_2019 = recent_data.loc[recent_data["DALYs"].idxmin(),"Entity"] #the answer is Singapore
print("the country with the maximum DALYs in 2019 is", max_country_2019)
print("the country with the minimum DALYs in 2019 is", min_country_2019)

Max_x_axis = dalys_data.loc[dalys_data.Entity == max_country_2019, "Year"]
Max_y_axis = dalys_data.loc[dalys_data.Entity == max_country_2019, "DALYs"]
plt.plot(Max_x_axis, Max_y_axis, 'bo') #"b" means "Blue", and "o" refers to the shape of the data points
plt.xticks(dalys_data.loc[dalys_data.Entity == max_country_2019, "Year"],rotation=-90) #let the xticks rotate a such angle to avoid overlap
plt.title("The DALYs change with years of Lesotho")
plt.xlabel("Years")
plt.ylabel("DALYs")
plt.savefig("C:/Users/ASUS/Desktop/Bioinformatic_workspace/IBI1/IBI1_2025-26/Practical_10/The_DALYs_change_with_years_of_Lesotho.png")
plt.show()

Min_x_axis = dalys_data.loc[dalys_data.Entity == min_country_2019, "Year"]
Min_y_axis = dalys_data.loc[dalys_data.Entity == min_country_2019, "DALYs"]
plt.plot(Min_x_axis, Min_y_axis, 'bo') #"b" means "Blue", and "o" refers to the shape of the data points
plt.xticks(dalys_data.loc[dalys_data.Entity == min_country_2019, "Year"],rotation=-90) #let the xticks rotate a such angle to avoid overlap
plt.title("The DALYs change with years of Singapore")
plt.xlabel("Years")
plt.ylabel("DALYs")
plt.savefig("C:/Users/ASUS/Desktop/Bioinformatic_workspace/IBI1/IBI1_2025-26/Practical_10/The_DALYs_change_with_years_of_Singapore.png")
plt.show()

#Task5: Free Question: What was the distribution of DALYs across countries with top 20 DALYs  in 2019?
print("Task5:")
target_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity","DALYs"]]
target_data = target_data.sort_values("DALYs", ascending=False).head(20) #find the target top 20 data and create a dataset
print("The countries with top 20 DALYs:\n",target_data.to_string(index=False).center(25)) 
x_axis = target_data["Entity"] #set x axis data
y_axis = target_data["DALYs"] # set y axis data
plt.bar(x_axis,y_axis)
plt.xticks(rotation=75)
plt.ylabel("DALYs")
plt.xlabel("Country")
plt.title("the distribution of DALYs across countries with top 20 DALYs in 2019")
plt.savefig("C:/Users/ASUS/Desktop/Bioinformatic_workspace/IBI1/IBI1_2025-26/Practical_10/The_distribution_of_DALYs_across_countries_with_top_20_DALYs_in_2019.png")
plt.show()