#!/usr/bin/env python3

PORTUGAL = "A"
CHINA = "B"
ENGLAND = "C"


def ports_of_hanoi(number_of_boats: int, source: str, destination: str, auxiliary: str):
    if number_of_boats == 1:
        print(f'{source} {destination}')
        return

    ports_of_hanoi(number_of_boats - 1, source, auxiliary, destination)
    print(f'{source} {destination}')
    ports_of_hanoi(number_of_boats - 1, auxiliary, destination, source)


def solve_problem():
    number_of_boats, number_of_trips = list(map(int, input().split(' ')))

    # The problem is a tower of hanoi puzzle, in which is solvable in 2^n-1 where n is the number of pieces (boats)
    # If the remainder is not zero, it is not solvable. And the div is the number of times it has to be solved.
    div, mod = divmod(number_of_trips, pow(2, number_of_boats)-1)

    if mod == 0:
        print('Y')

        # Initial solution if odd
        if div % 2 == 1:
            ports_of_hanoi(number_of_boats, PORTUGAL, ENGLAND, CHINA)
            div -= 1
        # Initial solution if even
        else:
            ports_of_hanoi(number_of_boats, PORTUGAL, CHINA, ENGLAND)
            ports_of_hanoi(number_of_boats, CHINA, ENGLAND, PORTUGAL)
            div -= 2

        # Cycle between england and portugal until satisfied number of trips
        for _ in range(div):
            ports_of_hanoi(number_of_boats, ENGLAND, PORTUGAL, CHINA)
            ports_of_hanoi(number_of_boats, PORTUGAL, ENGLAND, CHINA)
    else:
        print('N')


if __name__ == "__main__":
    solve_problem()
