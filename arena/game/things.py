from random import randint, uniform
from .game_settings import (
    MAX_THING_DEFENSE, MAX_THING_ATTACK, MAX_THING_HEALTH)


class Thing:
    def __init__(self, name, defense, attack, health):
        if 0 > defense > MAX_THING_DEFENSE:
            raise ValueError('Invalid protection of thing value')
        if 0 > attack > MAX_THING_ATTACK:
            raise ValueError('Invalid attack of thing value')
        if 0 > health > MAX_THING_HEALTH:
            raise ValueError('Invalid health of thing value')
        self.name = str(name)
        self.defense = defense
        self.attack = attack
        self.health = health


def sort_key_defense(thing):
    return thing.defense


THINGS = [
    Thing('Socks of Fortune', uniform(0, MAX_THING_DEFENSE),
          randint(0, MAX_THING_ATTACK), randint(0, MAX_THING_HEALTH)),
    Thing('Gods armor', 0.1, 0, 10),
    Thing('killing rage', 0, 10, 0),
    Thing('Ring of Health', 0, 0, 10),
    Thing('Ring of Power', 0.02, 5, 0),
    Thing('Casual hat', 0.1, 5, 5),
    Thing('Ferrobots', 0.1, 2, 3)
]
