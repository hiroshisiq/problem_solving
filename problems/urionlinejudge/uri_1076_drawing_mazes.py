#!/usr/bin/env python3
from typing import Dict, Set

Graph = Dict[str, Set[str]]


# Does a DFS and returns the number "movements" necessary to complete the search
def depth_first_search(graph: Graph, initial_vertex: str, visited: Graph, counter: int = 0) -> int:
    visited.add(initial_vertex)

    for next_vertex in graph[initial_vertex] - visited:
        counter = depth_first_search(graph, next_vertex, visited, counter)
        counter += 2

    return counter


def solve_problem():
    number_of_cases = int(input())

    for _ in range(number_of_cases):
        initial_vertex = int(input())
        number_of_vertices, number_of_edges = [int(i) for i in input().split()]

        # Initialize graph (incidence list representation)
        graph = dict((vertex, set()) for vertex in range(number_of_vertices))

        # Populate graph
        for entry in range(number_of_edges):
            vertex_a, vertex_b = [int(i) for i in input().split()]
            graph[vertex_a].add(vertex_b)
            graph[vertex_b].add(vertex_a)

        counter = depth_first_search(graph, initial_vertex, set())
        print(counter)


if __name__ == "__main__":
    solve_problem()
