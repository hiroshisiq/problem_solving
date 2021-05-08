#!/usr/bin/env python3
from typing import Dict


def calculate_total_distance(houses: Dict[str, int], packages: str, number_of_packages: int) -> int:
    # Calculate the distance between each delivery
    distance = 0
    for i in range(number_of_packages - 1):
        distance += abs(houses[packages[i]] - houses[packages[i + 1]])

    # Add distance to the first house
    return distance + houses[packages[0]]


def solve_problem():
    _, number_of_packages = map(int, input().split(' '))

    houses = dict((house, i) for i, house in enumerate(input().split(' ')))
    packages = input().split(' ')

    result = calculate_total_distance(houses, packages, number_of_packages)
    print(result)


if __name__ == "__main__":
    solve_problem()
