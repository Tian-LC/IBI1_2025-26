import random
import requests


BLOSUM62_TEXT = """
   A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V
A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0
R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3
N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3
D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3
C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1
Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2
E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2
G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3
H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3
I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3
L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1
K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2
M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1
F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1
P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2
S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2
T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0
W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3
Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1
V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4
"""


def parse_blosum62(matrix_text):
    lines = [line.strip() for line in matrix_text.strip().splitlines()]
    amino_acids = lines[0].split()

    matrix = {}

    for line in lines[1:]:
        parts = line.split()
        row_aa = parts[0]
        scores = parts[1:]

        matrix[row_aa] = {}

        for col_aa, score in zip(amino_acids, scores):
            matrix[row_aa][col_aa] = int(score)

    return matrix


def fetch_fasta_from_uniprot(accession):
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    return response.text


def parse_fasta(fasta_text):
    lines = fasta_text.strip().splitlines()
    header = lines[0].replace(">", "")
    sequence = "".join(lines[1:])
    return header, sequence


def generate_random_protein(length):
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    return "".join(random.choice(amino_acids) for _ in range(length))


def save_fasta(filename, name, sequence):
    with open(filename, "w") as file:
        file.write(f">{name}\n")

        for i in range(0, len(sequence), 60):
            file.write(sequence[i:i + 60] + "\n")


def compare_sequences(seq1_name, seq1, seq2_name, seq2, blosum62):
    if len(seq1) != len(seq2):
        raise ValueError("The two sequences must have the same length.")

    total_score = 0
    identical_count = 0

    for aa1, aa2 in zip(seq1, seq2):
        total_score += blosum62[aa1][aa2]

        if aa1 == aa2:
            identical_count += 1

    percentage_identity = identical_count / len(seq1) * 100
    normalised_score = total_score / len(seq1)

    print("=" * 70)
    print(f"Comparison: {seq1_name} vs {seq2_name}")
    print(f"Sequence length: {len(seq1)} amino acids")
    print(f"Identical amino acids: {identical_count}")
    print(f"Percentage identity: {percentage_identity:.2f}%")
    print(f"Raw BLOSUM62 score: {total_score}")
    print(f"Normalised score per residue: {normalised_score:.2f}")

    return {
        "comparison": f"{seq1_name} vs {seq2_name}",
        "length": len(seq1),
        "identical_count": identical_count,
        "percentage_identity": percentage_identity,
        "raw_score": total_score,
        "normalised_score": normalised_score,
    }


def main():
    random.seed(13)

    blosum62 = parse_blosum62(BLOSUM62_TEXT)

    human_fasta = fetch_fasta_from_uniprot("P56178")
    mouse_fasta = fetch_fasta_from_uniprot("P70396")

    human_name, human_seq = parse_fasta(human_fasta)
    mouse_name, mouse_seq = parse_fasta(mouse_fasta)

    random_seq = generate_random_protein(len(human_seq))

    save_fasta("human_DLX5_P56178.fasta", human_name, human_seq)
    save_fasta("mouse_DLX5_P70396.fasta", mouse_name, mouse_seq)
    save_fasta("random_protein.fasta", "Random_protein_sequence", random_seq)

    results = []

    results.append(
        compare_sequences(
            "Human DLX5",
            human_seq,
            "Mouse DLX5",
            mouse_seq,
            blosum62
        )
    )

    results.append(
        compare_sequences(
            "Human DLX5",
            human_seq,
            "Random sequence",
            random_seq,
            blosum62
        )
    )

    results.append(
        compare_sequences(
            "Mouse DLX5",
            mouse_seq,
            "Random sequence",
            random_seq,
            blosum62
        )
    )

    print("=" * 70)
    print("Summary table")
    print("=" * 70)

    for result in results:
        print(
            f"{result['comparison']}: "
            f"identity = {result['percentage_identity']:.2f}%, "
            f"raw score = {result['raw_score']}, "
            f"normalised score = {result['normalised_score']:.2f}"
        )


if __name__ == "__main__":
    main()