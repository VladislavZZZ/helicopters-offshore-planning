import json

from entities.Helicopter import Helicopter
from entities.Installation import Installation


def init_installations(raw_installations):
    installations=[]
    for raw_installation in raw_installations:
        installations.append(Installation(
                name=raw_installation["name"],
                destination=raw_installation["destination"],
                availability=raw_installation["availability"],
                distribution=raw_installation["demand_distribution"]
            ))
    return installations


def load_res(filepath: str):
    f = open("./"+filepath, "r").read()
    t = json.loads(f)
    return t

def init_helicopters(raw_helicopters):
    helicopters = []
    for raw_helicopter in raw_helicopters:
        helicopters.append(Helicopter(
            name=raw_helicopter["name"],
            capacity=raw_helicopter["capacity"],
            destination=raw_helicopter["base_destination"],
            availability=raw_helicopter["availability"],
            cost_per_week=raw_helicopter["cost_per_week"],
            currency=raw_helicopter["currency"]
        ))
    return helicopters