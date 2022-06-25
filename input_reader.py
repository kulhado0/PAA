from city import City
from position import Position


class InputReader:
    filepath: str
    num_cities: int

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_num_cities(self):
        file = open(self.filepath, 'r')
        with file as file:
            self.num_cities = int(file.readline())

    def readlines(self):
        file = open(self.filepath, 'r')
        with file as file:
            file.readline()
            return file.readlines()

    def get_cities(self):
        cities = []
        for line in self.readlines():
            city = self.get_city_from_line(line)
            cities.append(city)
        return cities

    def get_city_from_line(self, line: str):
        city_pos = Position(line)
        city = City(city_pos)
        return city
