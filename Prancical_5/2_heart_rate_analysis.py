#the total number of patients and the mean value of their heart rate
heart_rates_list = [72,60,126,85,90,59,76,131,88,121,64]
num = len(heart_rates_list)
sum = 0.0
for i in heart_rates_list:
    sum+=i
average = sum/float(num)
print(' total number of patients is', num,'\n','the mean value of their heart rate is', average)

#the number of each category and which category is the largest
low = []
normal = []
high = []
for i in heart_rates_list:
    if i >= 60 and i <= 120:
        normal.append(i)
    else:
        if i < 60:
            low.append(i)
        else:
            high.append(i)
nlow = len(low)
nnormal = len(normal)
nhigh = len(high)
category_num = {nlow: 'low', nnormal: 'normal', nhigh: 'high'}
largest_num = max(nlow,nnormal,nhigh)
largest_cat = category_num[largest_num]
print(' low:',nlow,'\n','normal:',nnormal,'\n','high:',nhigh)
print('the largest category is:', largest_cat)

#draw a pie plot
import matplotlib.pyplot as plt
labels = 'low','normal','high'
size = [nlow,nnormal,nhigh]
explode = (0,0,0)
plt.rcParams['font.size'] = 14
plt.pie(size, explode = explode, labels=labels, autopct='%1.1f%%' ,shadow = False, startangle= 90)
plt.axis('equal')
plt.title('The proportion of each heart rate type', fontsize = 18)
plt.show()