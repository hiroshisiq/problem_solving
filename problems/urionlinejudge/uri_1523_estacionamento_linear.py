#!/usr/bin/env python3
from typing import List, Tuple

# Car is a tuple with arrival and departure time
Car = Tuple[int, int]


def read_line() -> Tuple[int, int]:
    x, y = [int(i) for i in input().split(' ')]
    return x, y


def read_all() -> List[Tuple[int, int]]:
    line = read_line()
    lines = []

    while line[0] and line[1]:
        lines.append(line)
        for _ in range(line[0]):
            lines.append(read_line())
        line = read_line()

    return lines


def run_test_case(
    number_of_cars: int,
    parking_lot_size: int,
    cars: List[Car]
) -> bool:
    # Initialize parking_lot
    parking_lot: List[Car] = []

    # Run test
    for _ in range(number_of_cars):
        car = cars.pop(0)

        # Remove cars while last car left before car arrival
        while parking_lot and parking_lot[-1][1] <= car[0]:
            parking_lot.pop()

        # Check if car departure is before last car departure
        if parking_lot and parking_lot[-1][1] < car[1]:
            return False

        # Park new car
        parking_lot.append(car)

        # Check size
        if len(parking_lot) > parking_lot_size:
            return False

    # All cars were parked successfully
    return True


def solve_problem():
    info = read_all()

    while info:
        n, k = info.pop(0)
        cars = info[:n]
        del info[:n]

        if run_test_case(number_of_cars=n, parking_lot_size=k, cars=cars):
            print('Sim')
        else:
            print('Nao')


if __name__ == "__main__":
    solve_problem()
