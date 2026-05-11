import re

seq = []
header = []

with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f:
    count = -1

    for line in f:
        line = line.strip()

        if line.startswith(">"):
            count += 1
            header.append(line)
            seq.append("")
        else:
            seq[count] += line


with open("stop_genes.fa", "w") as out:
    for i in range(len(header)):
        current_seq = seq[i]

        # Store all stop codons found in this gene
        found_stops = []

        # Check every possible ATG start codon
        for start in range(len(current_seq) - 2):
            if current_seq[start:start + 3] == "ATG":

                # From this ATG, check codons in steps of 3
                for pos in range(start + 3, len(current_seq) - 2, 3):
                    codon = current_seq[pos:pos + 3]

                    if codon in ["TAA", "TAG", "TGA"]:
                        if codon not in found_stops:
                            found_stops.append(codon)

        # Only output genes that contain at least one in-frame stop codon
        if len(found_stops) > 0:

            # Extract the gene name from the header
            gene_match = re.search(r"gene:([^\s]+)", header[i])

            if gene_match:
                gene_name = gene_match.group(1)
            else:
                gene_name = header[i].split()[0].replace(">", "")

            out.write(">" + gene_name + ";" + ",".join(found_stops) + "\n")
            out.write(current_seq + "\n")