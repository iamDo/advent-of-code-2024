#!/usr/bin/env python3
import argparse
import re


def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def rotate(matrix):
    transposed = transpose(matrix)
    return [list(reversed(row)) for row in transposed]


def sub_matrix(matrix, x, y):
    row_1 = matrix[y][x:x+3]
    row_2 = matrix[y+1][x:x+3]
    row_3 = matrix[y+2][x:x+3]
    return [row_1, row_2, row_3]


def is_x_mas(matrix):
    if not    matrix[0][0] == 'M' \
       or not matrix[0][2] == 'S' \
       or not matrix[1][1] == 'A' \
       or not matrix[2][0] == 'M' \
       or not matrix[2][2] == 'S':
        return False
    return True


def count_x_masses(matrix):
    width, height = dimensions(matrix)
    xmas_count = 0
    for x in range(width - 3):
        for y in range(height - 3):
            if is_x_mas(sub_matrix(matrix, x, y)):
                xmas_count += 1
    return xmas_count


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
