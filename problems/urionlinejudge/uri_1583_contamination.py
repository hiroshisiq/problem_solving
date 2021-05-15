#!/usr/bin/env python3
from typing import Set, Dict, List

Graph = Dict[int, Set[int]]


def row_col_to_index(row: int, col: int, number_of_cols: int) -> int:
    return row*number_of_cols + col


def depth_first_search(graph: Graph, initial_vertex: int, visited: Set[int], vertices: List[str]):
    visited.add(initial_vertex)
    vertices[initial_vertex] = 'T'

    # Contaminate adjacent vertices
    for next_vertex in graph[initial_vertex] - visited:
        depth_first_search(graph, next_vertex, visited, vertices)


def solve_problem():
    rows, columns = [int(i) for i in input().split(' ')]
    while rows and columns:
        # Read map
        vertices = list(''.join([input() for _ in range(rows)]))

        # Initialize graph (incidence list representation) and contaminated vertices
        graph = dict((i, set()) for i in range(rows*columns))
        contaminated_vertices = set()

        # Populate graph and contaminated vertices from map
        for row in range(rows):
            for col in range(columns):
                index = row_col_to_index(row, col, columns)

                if vertices[index] == 'X':
                    continue

                if vertices[index] == 'T':
                    contaminated_vertices.add(index)

                front = row_col_to_index(row, col+1, columns)
                if col+1 < columns and vertices[front] != 'X':
                    graph[index].add(front)
                    graph[front].add(index)

                below = row_col_to_index(row+1, col, columns)
                if row+1 < rows and vertices[below] != 'X':
                    graph[index].add(below)
                    graph[below].add(index)

        # Run contamination from each contaminated spot
        for vertex in contaminated_vertices:
            depth_first_search(graph, vertex, set(), vertices)

        # Print solution
        for i in range(0, rows*columns, columns):
            print(''.join(vertices[i:i + columns]))
        print('')

        # Read next test case
        rows, columns = [int(i) for i in input().split(' ')]


if __name__ == "__main__":
    solve_problem()
