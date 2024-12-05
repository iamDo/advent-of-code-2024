#!/usr/bin/env python3
import argparse
import re


def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def rotate(matrix):
    transposed = transpose(matrix)
    return [list(reversed(row)) for row in transposed]


def count_x_masses(matrix):
    width, height = dimensions(matrix)
    xmas_count = 0
    for x in range(width - 2):
        for y in range(height - 2):
            if matrix[y][x] == 'M' \
               and matrix[y+2][x] == 'M' \
               and matrix[y][x+2] == 'S' \
               and matrix[y+2][x+2] == 'S' \
               and matrix[y+1][x+1] == 'A':
                xmas_count += 1
    return xmas_count


def dimensions(matrix):
    return (len(matrix[0]), len(matrix))


def display(matrix):
    for row in matrix:
        print(''.join(row))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input file", default="input.txt")
    args = parser.parse_args()

    lines = []
    with open(args.input) as f:
        lines = f.readlines()
    matrix = [line.strip() for line in lines]
    matrix90 = rotate(matrix)
    matrix180 = rotate(matrix90)
    matrix270 = rotate(matrix180)

    count = count_x_masses(matrix)
    count90 = count_x_masses(matrix90)
    count180 = count_x_masses(matrix180)
    count270 = count_x_masses(matrix270)

    print(count + count90 + count180 + count270)


if __name__ == "__main__":
    main()
