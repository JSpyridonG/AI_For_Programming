"""Calculate GC content for each record in a FASTA file."""

import argparse
import sys


def read_fasta_records(path):
    """Yield (header, sequence) pairs from a FASTA file."""
    header = None
    sequence = []
    with open(path, encoding="utf-8") as fasta_file:
        for line in fasta_file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    yield header, "".join(sequence)
                header = line[1:]
                sequence = []
            elif header is None:
                raise ValueError("FASTA sequence must follow a '>' header")
            else:
                sequence.append(line)

    if header is not None:
        yield header, "".join(sequence)


def main():
    parser = argparse.ArgumentParser(
        description="Print GC content for each record in a FASTA file."
    )
    parser.add_argument("path", help="path to the FASTA file")
    args = parser.parse_args()

    for header, sequence in read_fasta_records(args.path):
        if not sequence:
            print(f"Warning: skipping empty sequence for '{header}'", file=sys.stderr)
            continue
        gc_percentage = sum(base in "GCgc" for base in sequence) / len(sequence) * 100
        print(f">{header}\t{gc_percentage:.3f}%")


if __name__ == "__main__":
    main()
