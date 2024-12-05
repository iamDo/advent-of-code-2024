#!/usr/bin/env python3
import argparse
from collections import Counter



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input file", default="input.txt")
    args = parser.parse_args()

    lines = []
    with open(args.input) as f:
        lines = f.readlines()

    split_lines = [line.split() for line in lines]

    left_column = [int(line[0]) for line in split_lines]
    right_column = [int(line[1]) for line in split_lines]

    number_count = Counter(right_column)

    similarity_score = 0
    for number in left_column:
        similarity_delta = number * number_count[number]
        similarity_score += similarity_delta

    print(similarity_score)



if __name__ == "__main__":
    main()
