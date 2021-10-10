from random import randint
from .game_settings import (
    COUNT_THINGS_ON_HERO, MAX_THING_ATTACK,
    MAX_THING_DEFENSE,  MAX_THING_DODGE, MAX_THING_HEALTH)


class Thing:
    def __init__(self, name, defense, attack, dodge, health):
        if 0 > defense > MAX_THING_DEFENSE:
            raise ValueError('Invalid protection of thing value')
        if 0 > attack > MAX_THING_ATTACK:
            raise ValueError('Invalid attack of thing value')
        if 0 > dodge > MAX_THING_DODGE:
            raise ValueError('Invalid dodge of thing value')
        if 0 > health > MAX_THING_HEALTH:
            raise ValueError('Invalid health of thing value')
        self.name = str(name)
        self.defense = defense
        self.attack = attack
        self.dodge = dodge
        self.health = health


def sort_key_defense(thing):
    return thing.defense


THINGS = [
    Thing('Socks of Fortune', randint(0, MAX_THING_DEFENSE),
          randint(0, MAX_THING_ATTACK), randint(0, MAX_THING_DODGE),
          randint(0, MAX_THING_HEALTH)),
    Thing('Gods armor', 20, 0, 5, 20),
    Thing('killing rage', 0, 100, 0, 0),
    Thing('Ring of Health', 1, 0, 5, 100),
    Thing('Ring of Power', 1, 50, 0, 0),
    Thing('Casual hat', 1, 5, 5, 5),
    Thing('Ferrobots', 10, 2, 10, 20),
    Thing('Snake pants', 5, 10, 20, 20)
]

if COUNT_THINGS_ON_HERO > len(THINGS):
    COUNT_THINGS_ON_HERO = len(THINGS)
