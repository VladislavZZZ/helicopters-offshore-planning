from entities.additional.Place import Place
from entities.additional.dates.WeeklyTime import WeeklyTime


class Helicopter:
    def __init__(self, name, capacity, destination, availability, cost_per_week, currency) -> None:
        self.name = name
        self.capacity = capacity
        self.cost_per_week = cost_per_week
        self.currency = currency
        self.destination = Place(destination)
        self.availability = WeeklyTime(availability)
