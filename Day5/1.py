#!/usr/bin/env python3
import argparse


def separate_orders_and_rules(lines):
    rules = []
    orders = []
    add_to_rules = True
    for line in lines:
        if line == '':
            add_to_rules = False
            continue
        if add_to_rules:
            rule = line.split("|")
            rules.append(rule)
        else:
            order = line.split(",")
            orders.append(order)

    return orders, rules


# Rule only applies if both elements of rule are present in the order
def rule_applies(order, rule):
    return len(set(order) & set(rule)) == 2


def check_rule(order, rule):
    if rule_applies(order, rule):
        first_index = order.index(rule[0])
        second_index = order.index(rule[1])
        return first_index < second_index
    return True


def middle_value(lst):
    middle_index = int(len(lst)/2)
    return lst[middle_index]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input file", default="input.txt")
    args = parser.parse_args()

    lines = []
    with open(args.input) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    orders, rules = separate_orders_and_rules(lines)
    valid_orders = []
    for order in orders:
        applicable_rules = [rule for rule in rules if rule_applies(order, rule)]
        valid_order = True
        for rule in applicable_rules:
            if not check_rule(order, rule):
                valid_order = False
        if valid_order:
            valid_orders.append(order)

    middle_numbers = [int(middle_value(order)) for order in valid_orders]
    print(sum(middle_numbers))


if __name__ == "__main__":
    main()
