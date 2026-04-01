import re
seq = 'AUGAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
result = re.findall(r'(?=(AUG(?:...)*?(?:UAA|UAG|UGA)))', seq)
largest = ''
same_tmp = []
for i in result:
    if len(largest) < len(i):
        largest = i
        same_tmp = [i]
    if len(largest) == i:
         same_tmp.append(i)  
print('the largest orf(s):', same_tmp, "\n its(their) lenth:", len(largest) )