import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument('--reference', '-r', type=str, required=True, help="Reference genome file")
parser.add_argument('--input', '-i', type=str, required=True, help="Input fastq file")

args = parser.parse_args()

if not os.path.exists(args.input):
    print("Input file does not exist.")
    exit()

if not os.path.exists(args.reference):
    print("Reference file does not exist.")
    exit()

with open(args.input) as f:
    i = 1
    j = 1
    for line in f:
        if i % 4 == 2:
            print("Aligned sequence ", j, ": ", line.strip())
            j += 1
        i += 1

