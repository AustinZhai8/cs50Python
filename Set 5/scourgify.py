import sys
import csv

# Check if exactly two command-line arguments are provided
if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

# Get the input and output filenames
input_file = sys.argv[1]
output_file = sys.argv[2]

# Try to read the input file
try:
    with open(input_file, 'r') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")

# Write to the output file
with open(output_file, 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['first', 'last', 'house'])
    writer.writeheader()
    
    for row in rows:
        # Split the name into last and first
        name = row['name']
        last, first = name.split(', ')
        writer.writerow({'first': first, 'last': last, 'house': row['house']})
