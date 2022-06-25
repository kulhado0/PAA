from brute_force import BruteForce
from input_reader import InputReader


class Guloso:
    input_filename = 'pub_in.txt'
    lines: list
    cities: []

    def __init__(self):
        input_reader = InputReader(filepath=self.input_filename)
        self.lines = input_reader.readlines()
        self.cities = input_reader.get_cities()
        self.not_visited = self.cities[1:]
        self.path = [self.cities[0]]

    def get_min_path(self):
        while len(self.not_visited):
            index, closer_city = self.get_distance()
            self.path.append(closer_city)
            del self.not_visited[index]
        self.path.append(self.path[0])
        self.path.pop()
        return BruteForce.get_path_distance(self.path)

    def get_distance(self):
        return min(enumerate(self.not_visited),
                   key=lambda city: city[1].get_distance_from_city(self.path[-1]))
