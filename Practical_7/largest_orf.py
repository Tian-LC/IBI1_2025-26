import re
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
# Find all possible ORFs that start with AUG and end with one of the stop codons: UAA, UAG, or UGA.
result = re.findall(r'(?=(AUG(?:...)*?(?:UAA|UAG|UGA)))', seq)
# to store the longest ORF found 
largest = ''
# Store all ORFs that have the same longest length
same_tmp = []
# Check each ORF found by the regular expression
for i in result:
    # If the current ORF is longer than the previous longest ORF,
    # update the longest ORF and reset the list
    if len(largest) < len(i):
        largest = i
        same_tmp = [i]
    # If the current ORF has the same length as the longest ORF,
    # add it to the list
    elif len(largest) == len(i):
         same_tmp.append(i)  
print('the largest orf(s):', same_tmp, "\n its(their) length:", len(largest) )