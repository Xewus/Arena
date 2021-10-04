from .game_settings import (
    MAX_HERO_DEFENSE, MAX_HERO_ATTACK, MAX_HERO_HEALTH, MAX_DEFENSE)


def check_defense(defense):
    return (defense, MAX_DEFENSE)[defense > MAX_DEFENSE]


class Hero():
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
        self.defense = check_defense(defense)
        self.attack = attack * self.sex_dependence
        self.health = health / self.sex_dependence
        self.things = []

    def finalAttack(self):
        for thing in self.things:
            self.attack += thing.attack
            self.attack *= self.sex_dependence

    def finalDefense(self):
        for thing in self.things:
            self.defense += thing.defense
            self.defense = check_defense(self.defense)

    def finalHealth(self):
        for thing in self.things:
            self.health += thing.health
            self.health /= self.sex_dependence

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
    def finalDefense(self):
        for thing in self.things:
            self.defense += thing.defense
        self.defense *= 2
        self.defense = check_defense(self.defense)

    def finalHealth(self):
        for thing in self.things:
            self.health += thing.health
        self.health = self.health * 2 / self.sex_dependence


class Warrior(Hero):
    def finalAttack(self):
        for thing in self.things:
            self.attack += thing.attack
        self.attack = self.attack * 2 * self.sex_dependence


class Child(Paladin, Warrior):
    def __init__(self, sex, name, defense, attack, health):
        self.name = name
        self.defense = check_defense(defense)
        self.attack = attack
        self.health = health
        self.sex = sex
        self.things = []


AVAILABLE_HEROES_CLASSES = {
    'p': Paladin,
    'w': Warrior,
}
