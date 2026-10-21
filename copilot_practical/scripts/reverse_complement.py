# reverse_complement.py
# Reads a single-line DNA sequence from a FASTA file and prints its
# reverse complement.

COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}


def read_fasta_sequence(path):
    """Return the sequence (str) from a single-record FASTA file."""
    sequence = []
    found_header = False
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if found_header:
                    raise ValueError("Expected a single-record FASTA file")
                found_header = True
            elif not found_header:
                raise ValueError("FASTA sequence must follow a '>' header")
            else:
                sequence.append(line)

    if not found_header:
        raise ValueError("No FASTA record found")
    return "".join(sequence)


def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    seq = "".join(seq.split()).upper()
    invalid_bases = set(seq) - COMPLEMENT.keys()
    if invalid_bases:
        raise ValueError(f"Invalid DNA base(s): {''.join(sorted(invalid_bases))}")
    return "".join(COMPLEMENT[base] for base in reversed(seq))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Print the reverse complement of a single-record FASTA file."
    )
    parser.add_argument("path", help="path to the FASTA file")
    args = parser.parse_args()
    seq = read_fasta_sequence(args.path)
    print(reverse_complement(seq))