#!/usr/bin/env python3
import argparse
from operator import itemgetter
from copy import deepcopy


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
            rule = [int(r) for r in rule]
            rules.append(rule)
        else:
            order = line.split(",")
            order = [int(o) for o in order]
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


def is_valid(order, rules):
    for rule in rules:
        if not check_rule(order, rule):
            return False
    return True


def rules_for_page(page_number, rules):
    applicable_rules = [rule for rule in rules if rule[0] == page_number]
    return sorted(applicable_rules, key=itemgetter(1))


def fix_order(order, rules):
    fixed_order = deepcopy(order)
    for page in order:
        applicable_rules = rules_for_page(page, rules)
        if applicable_rules !=  []:
            indices = [fixed_order.index(rule[1]) for rule in applicable_rules]
            lowest_index = min(indices)
            value_index = fixed_order.index(page)
            if value_index > lowest_index:
                fixed_order = move_position(fixed_order, value_index, lowest_index)

    return fixed_order

def move_position(lst, origin, destination):
    lst = deepcopy(lst)
    value = lst.pop(origin)
    lst.insert(destination, value)
    return lst


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
    fixed_orders = []
    for order in orders:
        applicable_rules = [rule for rule in rules if rule_applies(order, rule)]
        if is_valid(order, applicable_rules):
            continue
        while not is_valid(order, applicable_rules):
            order = fix_order(order, applicable_rules)
        fixed_orders.append(order)

    middle_numbers = [middle_value(order) for order in fixed_orders]
    print(sum(middle_numbers))


if __name__ == "__main__":
    main()
