from position import Position


class City:
    pos: Position

    def __init__(self, pos: Position):
        self.pos = pos

    def get_distance_from_city(self, city):
        return self.pos.distance_from(pos=city.pos)
