#!/usr/bin/env python3
from collections import deque
from typing import List, Dict, Set

Graph = Dict[int, Set[int]]


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


def breadth_first_search(graph: Graph, start: int, ttl: int) -> int:
    # reached nodes
    return 0


def solve_problem():
    number_of_nodes = int(input())
    case_counter = 1
    while number_of_nodes:
        # Initialize graph (incidence list representation)
        graph = dict()

        # Read input
        edges, vertex_ttl = read_test_case(number_of_nodes)

        # Populate graph
        for i in range(0, 2*number_of_nodes, 2):
            graph.setdefault(edges[i], set()).add(edges[i+1])
            graph.setdefault(edges[i+1], set()).add(edges[i])
        del edges, i

        # Solve test cases for this graph
        for i in range(0, len(vertex_ttl), 2):
            start, ttl = vertex_ttl[i:i+2]
            reached_count = breadth_first_search(graph, start, ttl)

            print(f'Case {case_counter}: '
                  f'{number_of_nodes-reached_count} nodes not reachable from node {start} with TTL = {ttl}.')

            case_counter += 1

        # Read empty line and next test case size
        input()
        number_of_nodes = int(input())


if __name__ == "__main__":
    solve_problem()
