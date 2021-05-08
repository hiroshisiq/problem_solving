#!/usr/bin/env python3
from typing import Tuple


def read_case() -> Tuple[int, str, str]:
    s, p, i = [i for i in input().split(' ')]
    return int(s), p, i


def get_postorder(size: int, preorder: str, inorder: str) -> str:
    root = inorder.index(preorder[0])

    left = get_postorder(root, preorder[1:], inorder) if root != 0 else ''

    right = get_postorder(size-root-1, preorder[root+1:size], inorder[root+1:size]) if root != size-1 else ''

    return left + right + inorder[root]


if __name__ == "__main__":
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        s, p, i = read_case()
        result = get_postorder(size=s, preorder=p, inorder=i)
        print(result)
