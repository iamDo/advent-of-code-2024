#!/usr/bin/env python3
import argparse
import re


def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def rotate(matrix):
    transposed = transpose(matrix)
    return [list(reversed(row)) for row in transposed]


def scan_line(line):
    xmasses = re.findall(r'XMAS', line)
    xmasses += re.findall(r'SAMX', line)
    return xmasses


def diagonal(matrix, start_row, start_col):
    diagonal = []
    width, height = dimensions(matrix)
    longest_side = max(width, height)
    shortest_side = min(width, height)
    x = start_col
    y = start_row

    while x < width and y < height:
        diagonal.append(matrix[y][x])
        x = x + 1
        y = y + 1
    return diagonal


def diagonals(matrix):
    def _diagonals(matrix):
        diagonals = []
        width, height = dimensions(matrix)

        for i in range(width):
            diagonals.append(diagonal(matrix, 0, i))

        for i in range(1, height):
            diagonals.append(diagonal(matrix, i, 0))

        return diagonals

    return _diagonals(matrix) + _diagonals(rotate(matrix))


def dimensions(matrix):
    return (len(matrix[0]), len(matrix))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input file", default="input.txt")
    args = parser.parse_args()

    lines = []
    with open(args.input) as f:
        lines = f.readlines()
    matrix = [line.strip() for line in lines]

    horizontal_lines = [''.join(line) for line in matrix]
    vertical_lines = [''.join(line) for line in transpose(matrix)]
    diagonal_lines = [''.join(diag) for diag in diagonals(matrix)]
    lines = horizontal_lines + vertical_lines + diagonal_lines

    xmasses = sum([len(scan_line(line)) for line in lines])
    print(xmasses)



if __name__ == "__main__":
    main()
