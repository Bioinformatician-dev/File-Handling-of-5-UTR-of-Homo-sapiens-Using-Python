
# Sequence Translator using Python
The objective of this task is to create a Python function that translates a given DNA sequence into its corresponding protein sequence. This involves mapping codons (three-nucleotide sequences) to their respective amino acids using a predefined codon table.


## Authors

- [@Salma](https://www.github.com/Bioinformatician-dev)


## Description

The provided code defines a function translate_dna_to_protein that takes a DNA sequence as input and returns the corresponding protein sequence. Here’s a breakdown of how it works:

Codon Table Definition: A dictionary named codon_table is created, mapping each possible three-nucleotide codon to its respective amino acid. This is crucial for the translation process.

Protein Sequence Initialization: An empty string protein_sequence is initialized to store the resulting protein sequence as it is built.

Iterating Through the DNA Sequence: The function uses a for loop to iterate through the DNA sequence in steps of three nucleotides (codons). The loop runs from 0 to the length of the DNA sequence, incrementing by 3 each time.

Codon Translation: For each codon extracted from the DNA sequence, the function checks if it exists in the codon_table. If it does, the corresponding amino acid is appended to protein_sequence. If the codon is not found, a '?' is added to indicate an unknown codon.

Return Statement: Finally, the function returns the complete protein sequence.

Example Usage: The code includes a main block that demonstrates how to use the function. It defines a sample DNA sequence, calls the translation function, and prints both the original DNA sequence and the resulting protein sequence.

This code serves as a fundamental tool for bioinformatics applications, allowing researchers to translate genetic information into functional proteins efficiently.

