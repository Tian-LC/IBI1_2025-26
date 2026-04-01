import re
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
     m = re.search(r'^(ATG(?:...)*?)(TAA|TAG|TGA)', seq[i])
     header[i] = header[i] + (";" + m.group(2) if m else "000")
     end_codon[i] = m.group(1) + m.group(2) if m else "000"


for i in range(count, -1, -1):
    if "000" in header[i]:
        del header[i]
        del end_codon[i]
        del seq[i]
with open("stop_genes.fa", "w") as out:
    for i in range(len(header)):
        out.write(header[i] + "\n")
        out.write(seq[i] + "\n")
    