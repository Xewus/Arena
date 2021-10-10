from random import randint

from .game_settings import (
    ATTRIBUTES_HERO,  MAX_DEFENSE, MAX_DODGE, MAX_HERO_ATTACK,
    MAX_HERO_DEFENSE, MAX_HERO_DODGE, MAX_HERO_HEALTH)


def check_param(param, max_param):
    return (param, max_param)[param > max_param]


class Hero():
    __slots__ = ATTRIBUTES_HERO
    _defense_multiplier = 1
    _attack_multiplier = 1
    _dodge_multiplier = 1
    _health_multiplier = 1

    def __init__(self, name='', surname='', sex='w',
                 defense=0, attack=0, dodge=0, health=0):
        if not name.isalpha():
            raise ValueError('Invalid name of hero value')
        if not surname.isalpha():
            raise ValueError('Invalid surname of hero value')
        if sex not in 'wm':
            raise ValueError('Invalid sex of hero value')
        if 0 > defense > MAX_HERO_DEFENSE:
            raise ValueError('Invalid protection of hero value')
        if 0 > attack > MAX_HERO_ATTACK:
            raise ValueError('Invalid attack of hero value')
        if 0 > dodge > MAX_HERO_DODGE:
            raise ValueError('Invalid dodge of hero value')
        if 0 > health > MAX_HERO_HEALTH:
            raise ValueError('Invalid health of hero value')
        self.name = name
        self.surname = surname
        self.sex = sex
        self.sex_dependence = (1.1, 0.9)[sex == 'w']
        self.defense = int(
            check_param(defense * self._defense_multiplier, MAX_DEFENSE))
        self.attack = int(
            attack * self.sex_dependence * self._attack_multiplier)
        self.dodge = int(
            check_param(dodge * self._dodge_multiplier, MAX_DODGE))
        self.health = int(
            health / self.sex_dependence * self._health_multiplier)
        self.things = []

    def finalDefense(self):
        for thing in self.things:
            self.defense += thing.defense * self._defense_multiplier
            self.defense = int(check_param(self.defense, MAX_HERO_DEFENSE))

    def finalAttack(self):
        for thing in self.things:
            self.attack += int(
                thing.attack * self._attack_multiplier * self.sex_dependence)

    def finalDodge(self):
        for thing in self.things:
            self.dodge += thing.dodge * self._dodge_multiplier
            self.dodge = int(check_param(self.dodge, MAX_DODGE))

    def finalHealth(self):
        for thing in self.things:
            self.health += int(
                thing.health * self._health_multiplier / self.sex_dependence)

    def set_things(self, things):
        self.things.extend(things)
        self.finalAttack()
        self.finalDefense()
        self.finalDodge()
        self.finalHealth()

    def decrease_params(self, attack_damage):
        dodge = randint(0, MAX_DODGE)
        self.dodge -= 1
        if dodge < self.dodge:
            print(f'{self.name} уклонился')
            return None
        damage = attack_damage - attack_damage * (self.defense / 100)
        self.health -= damage
        self.defense -= 1
        print(f'{self.name} получил урон - {damage}')
        if self.health > 0:
            print(f'Осталось {self.health} HP')
        else:
            print(f'Боец {self.name} умер!')


class Paladin(Hero):
    _defense_multiplier = 2
    _health_multiplier = 1.5


class Warrior(Hero):
    _attack_multiplier = 2


class Rogue(Hero):
    _attack_multiplier = 1.3
    _dodge_multiplier = 1.3


AVAILABLE_HEROES_CLASSES = {
    'p': Paladin,
    'w': Warrior,
    'r': Rogue,
}
