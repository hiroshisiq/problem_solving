#!/usr/bin/env python3
# TIME EXCEEDED AT URI JUDGE ONLINE BUT WORKS FOR TEST CASE
import sys
from typing import Set, Dict

Graph = Dict[str, Set[str]]


def prim(graph: Graph) -> int:
    selected = [0]
    cost = 0

    while len(selected) < len(graph):
        nearest_distance = sys.maxsize
        nearest_vertex = sys.maxsize

        for vertex in selected:
            for neighbor, distance in graph[vertex]:
                if neighbor in selected:
                    continue

                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_vertex = neighbor

        cost += nearest_distance
        selected.append(nearest_vertex)

    return cost


def solve_problem():
    number_of_junctions, number_of_roads = [int(i) for i in input().split(' ')]
    while number_of_junctions or number_of_roads:
        # Initialize graph (incidence list representation)
        graph = dict((vertex, set()) for vertex in range(number_of_junctions))
        total = 0

        # Populate graph with road toll fee (cost)
        for _ in range(number_of_roads):
            city_a, city_b, distance = [int(i) for i in input().split(' ')]
            graph[city_a].add((city_b, distance))
            graph[city_b].add((city_a, distance))
            total += distance

        # Get MST cost
        cost = prim(graph)

        # Result
        print(total-cost)

        # Get new test case
        number_of_junctions, number_of_roads = [int(i) for i in input().split(' ')]


if __name__ == "__main__":
    solve_problem()
