#!/usr/bin/env python3
import sys
from collections import namedtuple
from typing import List

TestCase = namedtuple('TestCase', ['number_of_cities', 'number_of_roads', 'route_size', 'repair_city'])
Graph = List[List[int]]


def read_case() -> TestCase:
    n, m, c, k = [int(i) for i in input().split(' ')]
    return TestCase(number_of_cities=n, number_of_roads=m, route_size=c, repair_city=k)


def is_valid_test_case(test_case: TestCase) -> bool:
    return any(list(test_case))


def dijkstra(graph: Graph, start: int, end: int) -> List[int]:
    # Create arrays
    dist = [sys.maxsize] * len(graph)
    prev = [None] * len(graph)
    queue = list(range(len(graph)))

    # Initialize initial distance
    dist[start] = 0

    # Search
    while queue:
        vertex = dist.index(min([dist[i] for i in queue]))
        queue.remove(vertex)

        for neighbor, toll_fee in enumerate(graph[vertex]):
            if toll_fee is None or neighbor not in queue:
                continue

            alternative_dist = dist[vertex] + graph[vertex][neighbor]
            if alternative_dist < dist[neighbor]:
                dist[neighbor] = alternative_dist
                prev[neighbor] = vertex

    return dist, prev


def solve_problem():
    test_case = read_case()
    while is_valid_test_case(test_case):
        # Initialize graph (adjacency matrix representation)
        graph = [[None]*test_case.number_of_cities for _ in range(test_case.number_of_cities)]

        # Populate graph with road toll fee (cost)
        for _ in range(test_case.number_of_roads):
            city_a, city_b, toll_fee = [int(i) for i in input().split(' ')]
            graph[city_a][city_b] = toll_fee
            graph[city_b][city_a] = toll_fee

        # Get distances
        distances, _ = dijkstra(graph, test_case.repair_city, test_case.route_size-1)

        # Result
        print(distances[test_case.route_size-1])

        # Cleanup and get new test case
        del graph, test_case
        test_case = read_case()


if __name__ == "__main__":
    solve_problem()
