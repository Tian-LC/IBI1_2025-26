import re
import matplotlib.pyplot as plt
f = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
count = -1
seq = []
header = []
orfs = []
for line in f:
    line = line.strip()
    if line.startswith('>'):
        count += 1
        header.append(line.split(" ")[0])
        seq.append("")
    else:
        seq[count] += line.strip()

end_codon = [None] * (count+1)
for i in range(count+1):
     m = re.search(r'^(ATG(?:...)*)(TAA|TAG|TGA)', seq[i])
     header[i] = header[i] + (";" + m.group(2) if m else "000")
     end_codon[i] = m.group(1) + m.group(2) if m else "000"


for i in range(count, -1, -1):
    if "000" in header[i]:
        del header[i]
        del end_codon[i]

TAA = []
TAG = []
TGA = []
codon_counts = {}
codon_list = []

for i in end_codon:
    if re.search('TAA$', i):
        TAA.append(i)
    else:
        if re.search('TAG$', i):
            TAG.append(i)
        else:
            TGA.append(i)

target = input() 
if target == 'TAA':
    for gene in TAA:
        for i in range(0,len(gene)-3,3):
            codon = gene[i:i+3]
            if codon not in codon_list:
                codon_list.append(codon)
            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1

if target == 'TAG':
    for gene in TAG:
        for i in range(0,len(gene)-3,3):
            codon = gene[i:i+3]
            if codon not in codon_list:
                codon_list.append(codon)
            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1

if target == 'TGA':
    for gene in TGA:
        for i in range(0,len(gene)-3,3):
            codon = gene[i:i+3]
            if codon not in codon_list:
                codon_list.append(codon)
            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1

labels = list(codon_counts.keys())
sizes = list(codon_counts.values())

plt.figure(figsize=(12, 12))
plt.pie(sizes, labels=labels, autopct=lambda P:"%1.1f%%" if P>= 5 else "", startangle=90)
plt.title("Codon distribution upstream of "+ target+"\n")
plt.axis("equal")
plt.savefig(target+"_pie_chart.png", dpi=300)
plt.close()