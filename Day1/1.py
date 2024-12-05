#!/usr/bin/env python3
import argparse



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input file", default="input.txt")
    args = parser.parse_args()

    lines = []
    with open(args.input) as f:
        lines = f.readlines()

    split_lines = [line.split() for line in lines]

    left_column = [int(line[0]) for line in split_lines]
    left_column.sort()
    right_column = [int(line[1]) for line in split_lines]
    right_column.sort()

    combined = [(left_column[i], right_column[i]) for i in range(len(left_column))]
    differences = [max(row) - min(row) for row in combined]
    print(sum(differences))


if __name__ == "__main__":
    main()
