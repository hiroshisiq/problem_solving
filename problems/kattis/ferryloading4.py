#!/usr/bin/env python3
from collections import namedtuple, deque
from typing import Tuple, List

Car = namedtuple('Car', ['length_in_cm', 'side'])


def read_configuration() -> Tuple[int, int]:
    l, m = [int(i) for i in input().split(' ')]
    return l, m


def build_car(entry: str) -> Car:
    length, side = entry.split(' ')
    return Car(length_in_cm=int(length), side=side)


def read_car_list(size: int) -> List[Car]:
    return [build_car(input()) for _ in range(size)]


def load_ferry(queue: deque, ferry_length):
    load = 0
    while queue:
        # Try to load next car in ferry
        load += queue[0].length_in_cm

        # If not exceeded limit load, else, break
        if load <= ferry_length:
            queue.popleft()
        else:
            break


def get_number_of_crosses(ferry_length_in_cm: int, car_list: List[Car], number_of_cars: int) -> int:
    queues = {'left': deque(), 'right': deque()}
    [queues[car.side].append(car) for car in car_list]

    counter = 0
    while any(queues.values()):
        load_ferry(queues['left'], ferry_length_in_cm)
        counter += 1

        if not any(queues.values()):
            break

        load_ferry(queues['right'], ferry_length_in_cm)
        counter += 1

    return counter


def solve_problem():
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        ferry_length_in_m, number_of_cars = read_configuration()
        car_list = read_car_list(number_of_cars)
        result = get_number_of_crosses(ferry_length_in_m*100, car_list, number_of_cars)
        print(result)


if __name__ == "__main__":
    solve_problem()
