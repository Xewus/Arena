from random import randint
from .game_settings import (
    MAX_THING_DEFENSE, MAX_THING_ATTACK, MAX_THING_HEALTH)


class Thing:
    def __init__(self, name, defense, attack, health):
        if defense > MAX_THING_DEFENSE or defense < 0:
            raise ValueError('Invalid protection of thing value')
        if attack > MAX_THING_ATTACK or attack < 0:
            raise ValueError('Invalid attack of thing value')
        if health > MAX_THING_HEALTH or health < 0:
            raise ValueError('Invalid health of thing value')
        self.name = str(name)
        self.defense = float(defense)
        self.attack = float(attack)
        self.health = float(health)


def sort_key_defense(thing):
    return thing.defense


THINGS = [
    Thing('Socks of Fortune', randint(0, 10) / 100,
          randint(0, 10), randint(0, 100)),
    Thing('Gods armor', 0.1, 0, 10),
    Thing('killing rage', 0, 10, 0),
    Thing('Ring of Health', 0, 0, 10),
    Thing('Ring of Power', 0.02, 5, 0),
    Thing('Casual hat', 0.1, 5, 5),
    Thing('Ferrobots', 0.1, 2, 3)
]
