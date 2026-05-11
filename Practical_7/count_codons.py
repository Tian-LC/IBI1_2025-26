import matplotlib.pyplot as plt

seqs = []
headers = []

# Read the FASTA file and combine sequence lines for each gene
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f:
    count = -1

    for line in f:
        line = line.strip()

        if line.startswith(">"):
            count += 1
            headers.append(line)
            seqs.append("")
        else:
            seqs[count] += line

# Ask the user to input one stop codon
target = input("Enter a stop codon (TAA, TAG, TGA): ")

# Check that the input is valid
if target not in ["TAA", "TAG", "TGA"]:
    print("Invalid stop codon. Please enter TAA, TAG, or TGA.")
    exit()

# Store the counts of codons upstream of the selected stop codon
codon_counts = {}

# Go through each gene sequence
for seq in seqs:
    longest_orf = ""

    # Check every possible ATG start codon
    for start in range(len(seq) - 2):
        if seq[start:start + 3] == "ATG":

            # From this ATG, check codons in steps of 3
            for pos in range(start + 3, len(seq) - 2, 3):
                codon = seq[pos:pos + 3]

                # Only consider the stop codon selected by the user
                if codon == target:
                    orf = seq[start:pos + 3]

                    # Keep the ORF that gives the longest sequence
                    if len(orf) > len(longest_orf):
                        longest_orf = orf

    # Count codons upstream of the selected stop codon
    # The stop codon itself is not counted
    if longest_orf != "":
        for i in range(0, len(longest_orf) - 3, 3):
            codon = longest_orf[i:i + 3]

            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1

# Print the codon counts
print("Codon counts upstream of", target)

for codon in codon_counts:
    print(codon, codon_counts[codon])

# Generate and save a pie chart
if len(codon_counts) > 0:
    labels = list(codon_counts.keys())
    sizes = list(codon_counts.values())

    plt.figure(figsize=(12, 12))
    plt.pie(
        sizes,
        labels=labels,
        autopct=lambda p: "%1.1f%%" % p if p >= 5 else "",
        startangle=90
    )

    plt.title("Codon distribution upstream of " + target)
    plt.axis("equal")
    plt.savefig(target + "_pie_chart.png", dpi=300)
    plt.close()

    print("Pie chart saved as " + target + "_pie_chart.png")

else:
    print("No genes containing this in-frame stop codon were found.")