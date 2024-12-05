#!/usr/bin/env python3
import argparse
import re



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input file", default="input.txt")
    args = parser.parse_args()

    lines = []
    with open(args.input) as f:
        lines = f.readlines()

    data = ''.join(lines)
    valid_instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
    operands = [[int(op) for op in re.findall(r'\d{1,3}', instruction)] for instruction in valid_instructions]
    print(sum([op[0] * op[1] for op in operands]))


if __name__ == "__main__":
    main()
