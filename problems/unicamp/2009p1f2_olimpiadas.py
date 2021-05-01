#!/usr/bin/env python3
from typing import Tuple, List
from dataclasses import dataclass

@dataclass
class Country():
    id: int
    gold_medals: int = 0
    silver_medals: int = 0
    bronze_medals: int = 0

def read_medal_winners() -> Tuple[int, int, int]:
    g, s, b = [int(i) for i in input().split(' ')]
    return (g, s, b)

def read_countries_and_categories() -> Tuple[int, int]:
    m, n = [int(i) for i in input().split(' ')]
    return (m, n)

def sort_countries_by_medal_count(countries: List[Country]) -> List[Country]:
    sorted_countries = sorted(countries, key=lambda country: country.bronze_medals, reverse=True)
    sorted_countries = sorted(countries, key=lambda country: country.silver_medals, reverse=True)
    sorted_countries = sorted(countries, key=lambda country: country.gold_medals, reverse=True)
    return sorted_countries

if __name__ == "__main__":
    m, n = read_countries_and_categories()
    countries = [Country(id=id+1) for id in range(m)]

    for _ in range(n):
        gold_winner, silver_winner, bronze_winner = read_medal_winners()

        # Update medal counter
        countries[gold_winner-1].gold_medals += 1
        countries[silver_winner-1].silver_medals += 1
        countries[bronze_winner-1].bronze_medals += 1

    sorted_countries = sort_countries_by_medal_count(countries)
    result = ' '.join([str(country.id) for country in sorted_countries])

    print(result)
