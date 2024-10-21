# Import necessary libraries
import os

def read_utr_file(file_path):
    """Reads the 5' UTR sequences from a given file."""
    try:
        with open(file_path, 'r') as file:
            utr_sequences = file.readlines()
        return [seq.strip() for seq in utr_sequences if seq.strip()]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []

def process_utr_sequences(utr_sequences):
    """Processes the UTR sequences to extract relevant information."""
    processed_sequences = []
    for seq in utr_sequences:
        # Example processing: Convert to uppercase
        processed_sequences.append(seq.upper())
    return processed_sequences

def write_processed_sequences(output_path, processed_sequences):
    """Writes the processed UTR sequences to a new file."""
    with open(output_path, 'w') as file:
        for seq in processed_sequences:
            file.write(f"{seq}\n")
    print(f"Processed sequences written to {output_path}")

def main():
    input_file = '5_UTR_sequences.txt'  # Input file containing UTR sequences
    output_file = 'processed_5_UTR_sequences.txt'  # Output file for processed sequences

    # Read UTR sequences from the input file
    utr_sequences = read_utr_file(input_file)

    # Process the UTR sequences
    processed_sequences = process_utr_sequences(utr_sequences)

    # Write the processed sequences to the output file
    write_processed_sequences(output_file, processed_sequences)

if __name__ == "__main__":
    main()


