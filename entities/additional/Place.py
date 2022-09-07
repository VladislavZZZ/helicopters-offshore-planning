import numpy as np


class Place:
    def __init__(self, destination) -> None:
        self.x = destination["x"]
        self.y = destination["y"]

    def count_distance(self, p2):
        return np.linalg.norm((self.x-p2.x, self.y - p2.y))