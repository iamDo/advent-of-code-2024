#!/usr/bin/env python3
import argparse
from copy import deepcopy
from collections import Counter


def apply_dampener(report):
    dampened_reports = []
    for i in range(len(report)):
        dampened_report = deepcopy(report)
        dampened_report.pop(i)
        dampened_reports.append(dampened_report)
    return dampened_reports


def test_increasing(report):
    for i in range(1, len(report)):
        if report[i] < report[i - 1]:
            return False
    return True


def test_decreasing(report):
    return test_increasing(list(reversed(report)))


def test_delta(report):
    for i in range(1, len(report)):
        delta = abs(report[i - 1] - report[i])
        if delta > 3 or delta == 0:
            return False
    return True


def safe_report_p(report):
    safe_fluctuation = test_decreasing(report) or test_increasing(report)
    safe_deltas = test_delta(report)
    return safe_deltas and safe_fluctuation


def test_report(report):
    safe_report = safe_report_p(report)
    if not safe_report:
        for dampened_report in apply_dampener(report):
            if safe_report_p(dampened_report):
                return True
    return safe_report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input file", default="input.txt")
    args = parser.parse_args()

    lines = []
    with open(args.input) as f:
        lines = f.readlines()

    reports = [[int(level) for level in line.split()] for line in lines]
    safety_counter = Counter([test_report(report) for report in reports])
    print(safety_counter[True])


if __name__ == "__main__":
    main()
