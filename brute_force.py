from itertools import permutations

from input_reader import InputReader


class BruteForce:
    input_filename = 'pub_in.txt'
    lines: list
    cities: []

    def __init__(self):
        input_reader = InputReader(filepath=self.input_filename)
        self.lines = input_reader.readlines()
        self.cities = input_reader.get_cities()

    def get_min_path(self):
        min_path = min(permutations(self.cities), key=lambda city: self.get_path_distance(city))
        return self.get_path_distance(min_path)

    @staticmethod
    def get_path_distance(path):
        distance_sum = [city.get_distance_from_city(path[index - 1]) for index, city in enumerate(path)]
        return sum(distance_sum)
