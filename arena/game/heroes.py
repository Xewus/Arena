from .game_settings import (
    MAX_HERO_DEFENSE, MAX_HERO_ATTACK, MAX_HERO_HEALTH,)


class Hero():
    def __init__(self, name, defense, attack, health, sex):
        if not name.isalpha():
            raise ValueError('Invalid name of hero value')
        if defense > MAX_HERO_DEFENSE or defense < 0:
            raise ValueError('Invalid protection of hero value')
        if attack > MAX_HERO_ATTACK or attack < 1:
            raise ValueError('Invalid attack of hero value')
        if health > MAX_HERO_HEALTH or health < 1:
            raise ValueError('Invalid health of hero value')
        if sex not in 'wm':
            raise ValueError('Invalid sex of hero value')
        self.name = name
        self.defense = defense
        if self.defense >= 0.9:
            self.defense = 0.9
        self.attack = attack
        self.health = health
        self.sex = sex
        self.things = []

    def finalAttack(self):
        for thing in self.things:
            self.attack += thing.attack

    def finalDefense(self,):
        for thing in self.things:
            self.defense += thing.defense

    def finalHealth(self):
        for thing in self.things:
            self.health += thing.health

    def set_things(self, things):
        self.things.extend(things)
        self.finalAttack()
        self.finalDefense()
        self.finalHealth()

    def decrease_helth(self, attack_damage):
        damage = attack_damage - attack_damage * self.defense
        self.health -= damage
        print(f'{self.name} получил урон - {damage}')
        if self.health > 0:
            print(f'Осталось {self.health} HP')
        else:
            print(f'Боец {self.name} умер!', 'blue')


class Paladin(Hero):
    def finalDefense(self,):
        for thing in self.things:
            self.defense += thing.defense
        self.defense *= 2

    def finalHealth(self):
        for thing in self.things:
            self.health += thing.health
        self.health *= 2


class Warrior(Hero):
    def finalAttack(self):
        for thing in self.things:
            self.attack += thing.attack
        self.attack *= 2


class Child(Paladin, Warrior):
    def __init__(self, name, defense, attack, health, sex):
        self.name = name
        self.defense = defense
        if self.defense >= 0.9:
            self.defense = 0.9
        self.attack = attack
        self.health = health
        self.sex = sex
        self.things = []
