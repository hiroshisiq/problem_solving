#!/usr/bin/env python3
from typing import Tuple, List


def read_test_case() -> Tuple[str, List[str]]:
    array_size = input()
    test_array = input().split(' ')
    return array_size, test_array


def array_to_depth(array: List[str], size: int, depth: int) -> str:
    index = array.index(max(array))

    left = array_to_depth(array[:index], index, depth+1) if index != 0 else ''
    right = array_to_depth(array[index+1:], size-index-1, depth+1) if index != size-1 else ''

    return f'{left} {depth} {right}'.strip()


if __name__ == "__main__":
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        size, array = read_test_case()
        result = array_to_depth(array, int(size), 0)
        print(result)
