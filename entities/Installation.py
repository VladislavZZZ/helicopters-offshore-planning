from entities.additional.Place import Place
from entities.additional.dates.WeeklyTime import WeeklyTime
from entities.additional.DemandDistribution import DemandDistribution


class Installation:
    def __init__(self, name, destination, availability, distribution ) -> None:
        self.name = name
        self.destination = Place(destination)
        self.availability = WeeklyTime(availability)
        self.demand_distrib = DemandDistribution(distribution)
