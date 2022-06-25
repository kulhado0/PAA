from itertools import combinations

from brute_force import BruteForce
from input_reader import InputReader


class Dynamic:
    input_filename = 'pub_in.txt'
    lines: list
    cities: []

    def __init__(self):
        input_reader = InputReader(filepath=self.input_filename)
        self.lines = input_reader.readlines()
        self.cities = input_reader.get_cities()

    def get_min_path(self):
        min_path = [self.cities[index] for index in self.resolver()]
        return BruteForce.get_path_distance(min_path)

    def resolver(self):
        matrix_distance = [[city_.get_distance_from_city(city__) for city__ in self.cities] for city_ in self.cities]
        first_city = {(frozenset([0, idx + 1]), idx + 1): (dist, [0, idx + 1]) for idx, dist in
                      enumerate(matrix_distance[0][1:])}
        num_cities = len(self.cities)
        for m in range(2, num_cities):
            scnd_city = {}
            cities_combination = combinations(range(1, num_cities), m)
            for city_set in [frozenset(C) | {0} for C in cities_combination]:
                city_set_ = city_set - {0}
                for set in city_set_:
                    scnd_city[(city_set, set)] = min([(first_city[(city_set - {set}, k)][0] + matrix_distance[k][set],
                                                       first_city[(city_set - {set}, k)][1] + [set])
                                                      for k in city_set if k != 0 and k != set])
            first_city = scnd_city
        return min([(first_city[d_iter][0] + matrix_distance[0][d_iter[1]], first_city[d_iter][1]) for d_iter in
                    iter(first_city)])[1]
