#!/usr/bin/env python3

class BilliardCue:
    def __init__(self, length):
        self.length = length
        self.stock_quantity = 0
        self.total = 0


def get_or_fabricate_cue(cue: BilliardCue):
    if cue.stock_quantity == 0:
        cue.stock_quantity += 1
        cue.total += 2
    else:
        cue.stock_quantity -= 1


if __name__ == "__main__":
    quantity = int(input())

    store = {}
    for billiard_length in input().split(' '):
        billiard_cue = store.setdefault(billiard_length, BilliardCue(billiard_length))
        get_or_fabricate_cue(billiard_cue)

    result = sum([cue.total for cue in store.values()])
    print(result)
