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

    data = ' '.join(lines)
    valid_instructions =  re.findall(r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)', data)
    mul_enabled = True
    multiplications = []
    for instruction in valid_instructions:
        if instruction == "do()":
            mul_enabled = True
        elif instruction == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                operands = [int(op) for op in re.findall(r'\d{1,3}', instruction)]
                value = operands[0] * operands[1]
                multiplications.append(value)
    print(sum(multiplications))



if __name__ == "__main__":
    main()
