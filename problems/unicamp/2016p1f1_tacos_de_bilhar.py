from collections import namedtuple

class BilliardCue():
    def __init__(self, lenght):
        self.length = lenght
        self.stock_quantity = 0
        self.total = 0

def getOrFabricateCue(cue: BilliardCue):
    if cue.stock_quantity == 0:
        cue.stock_quantity += 1
        cue.total += 2
    else:
        cue.stock_quantity -= 1

if __name__ == "__main__":
    quantity = int(input())

    store = {}
    for lenght in input().split(' '):
        cue = store.setdefault(lenght, BilliardCue(lenght))
        getOrFabricateCue(cue)

    result = sum([cue.total for cue in store.values()])
    print(result)
