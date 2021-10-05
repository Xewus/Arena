from .game_settings import (
    ATTRIBUTES_HERO,
    MAX_HERO_DEFENSE, MAX_HERO_ATTACK, MAX_HERO_HEALTH, MAX_DEFENSE)


def check_defense(defense):
    return (defense, MAX_DEFENSE)[defense > MAX_DEFENSE]


class Hero():
    __slots__ = ATTRIBUTES_HERO
    _defense_multiplier = 1
    _attack_multiplier = 1
    _health_multiplier = 1
    _dodge_multiplier = 1

    def __init__(self, name, sex, defense, attack, health):
        if not name.isalpha():
            raise ValueError('Invalid name of hero value')
        if sex not in 'wm':
            raise ValueError('Invalid sex of hero value')
        if 0 > defense > MAX_HERO_DEFENSE:
            raise ValueError('Invalid protection of hero value')
        if 0 > attack > MAX_HERO_ATTACK:
            raise ValueError('Invalid attack of hero value')
        if 0 > health > MAX_HERO_HEALTH:
            raise ValueError('Invalid health of hero value')
        self.name = name
        self.sex = sex
        self.sex_dependence = (1.1, 0.9)[sex == 'w']
        self.defense = int(
            check_defense(defense * self._defense_multiplier))
        self.attack = int(
            attack * self.sex_dependence * self._attack_multiplier)
        self.health = int(
            health / self.sex_dependence * self._health_multiplier)
        self.things = []

    def finalDefense(self):
        for thing in self.things:
            self.defense += thing.defense * self._defense_multiplier
            self.defense = int(check_defense(self.defense))

    def finalAttack(self):
        for thing in self.things:
            self.attack += int(
                thing.attack * self._attack_multiplier * self.sex_dependence)

    def finalHealth(self):
        for thing in self.things:
            self.health += int(
                thing.health * self._health_multiplier / self.sex_dependence)

    def set_things(self, things):
        self.things.extend(things)
        self.finalAttack()
        self.finalDefense()
        self.finalHealth()

    def decrease_helth(self, attack_damage):
        damage = attack_damage - attack_damage * (self.defense / 100)
        self.health -= damage
        print(f'{self.name} получил урон - {damage}')
        if self.health > 0:
            print(f'Осталось {self.health} HP')
        else:
            print(f'Боец {self.name} умер!')


class Paladin(Hero):
    _defense_multiplier = 2
    _health_multiplier = 2


class Warrior(Hero):
    _attack_multiplier = 2


class Child(Paladin, Warrior):
    _defense_multiplier = 1
    _attack_multiplier = 1
    _health_multiplier = 1
    _dodge_multiplier = 1


AVAILABLE_HEROES_CLASSES = {
    'p': Paladin,
    'w': Warrior,
}
