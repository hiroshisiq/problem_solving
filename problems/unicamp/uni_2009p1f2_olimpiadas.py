#!/usr/bin/env python3
from typing import Tuple, List


class Country:
    def __init__(self, country_id: int):
        self.id = country_id
        self.gold_medals = 0
        self.silver_medals = 0
        self.bronze_medals = 0


def read_medal_winners() -> Tuple[int, int, int]:
    g, s, b = [int(i) for i in input().split(' ')]
    return g, s, b


def read_countries_and_categories() -> Tuple[int, int]:
    m, n = [int(i) for i in input().split(' ')]
    return m, n


def sort_countries_by_medal_count(countries: List[Country]) -> List[Country]:
    s_countries = sorted(countries, key=lambda country: country.bronze_medals, reverse=True)
    s_countries = sorted(s_countries, key=lambda country: country.silver_medals, reverse=True)
    s_countries = sorted(s_countries, key=lambda country: country.gold_medals, reverse=True)
    return s_countries


if __name__ == "__main__":
    number_of_countries, number_of_sports = read_countries_and_categories()
    country_list = [Country(country_id=country_id + 1)
                    for country_id in range(number_of_countries)]

    for _ in range(number_of_sports):
        gold_winner, silver_winner, bronze_winner = read_medal_winners()

        # Update medal counter
        country_list[gold_winner - 1].gold_medals += 1
        country_list[silver_winner - 1].silver_medals += 1
        country_list[bronze_winner - 1].bronze_medals += 1

    sorted_countries = sort_countries_by_medal_count(country_list)
    result = ' '.join([str(country.id) for country in sorted_countries])

    print(result)
