# GC Content Script

`scripts/gc_content.py` reads a FASTA file and prints the GC percentage for each non-empty record. It counts `G` and `C` in either case and reports each result with the record header and a percentage to two decimal places.

Run it from this folder with:

```bash
python scripts/gc_content.py path/to/sequences.fasta
```

The script currently does **not** define a `--min-gc` option, so it does not filter records by GC percentage.

Records with empty sequences are skipped, and a warning naming the record is written to standard error.
