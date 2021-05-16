#!/usr/bin/env python3
from typing import List


def read_line() -> List[int]:
    # This function goes throw the following steps:
    # 1. Read line and split by space
    # 2. Filter out empty entries (the spacing in the input can be irregular)
    # 3. Map all entries to int
    return list(map(int, filter(None, input().split(' '))))


def read_test_case(number_of_nodes: int):
    line = read_line()

    # Test case ends when we read 0 0
    while line[-1] or line[-2]:
        line.extend(read_line())

    # Remove end of test case
    del line[-2:]

    # Return vertex/vertex pairs and vertex/ttl pairs
    return line[:2*number_of_nodes], line[2*number_of_nodes:]


def solve_problem():
    number_of_nodes = int(input())
    while number_of_nodes:
        edges, vertex_ttl = read_test_case(number_of_nodes)

        # Read empty line and next test case size
        input()
        number_of_nodes = int(input())


if __name__ == "__main__":
    solve_problem()
