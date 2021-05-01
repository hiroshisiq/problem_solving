from typing import Tuple, List

class Number():
    def __init__(self, value: int, div: int):
        self.value = str(value)                                 # true value
        self.rem = value % div if value > 0 else -(value % div) # mod by div
        self.remBy2 = value % 2                                 # is even
        self.secondaryValue = -value if self.remBy2 else value  # last untie

def read_configuration() -> Tuple[int, int]:
    m, n = [int(i) for i in input().split(' ')]
    return (m, n)

def read_list(size: int, div: int) -> List[Number]:
    return [Number(int(input()), div) for _ in range(size)]

def sort_numbers(numbers: List[Number]) -> List[Number]:
    return sorted(numbers, key=lambda n: (n.rem, -n.remBy2, n.secondaryValue))

if __name__ == "__main__":
    size, div = read_configuration()

    while size != 0 and div != 0:
        numbers = read_list(size, div)
        result = [number.value for number in sort_numbers(numbers)]

        # Output result
        print(f'{size} {div}')
        print('\n'.join(result))

        # Get next round (end if size and mod is equal to zero)
        size, mod = read_configuration()

    print('0 0')
