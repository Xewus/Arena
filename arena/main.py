import random

from game.game_settings import (
    NAMES, COUNT_PERSES, COUNT_THINGS_ON_PERS,
    MAX_HERO_DEFENSE, MAX_HERO_ATTACK, MAX_HERO_HEALTH, SURVIVAL)
from game.heroes import Child, Paladin, Warrior, AVAILABLE_HEROES_CLASSES
from game.things import THINGS


def auto_create_hero():
    klasse = Warrior if random.randint(0, 1) else Paladin
    name, sex = NAMES.pop(random.randint(0, len(NAMES) - 1))
    defense = random.uniform(0, MAX_HERO_DEFENSE)
    attack = random.randint(1, MAX_HERO_ATTACK)
    helth = random.randint(1, MAX_HERO_HEALTH)
    return klasse(name, defense, attack, helth, sex)


FIGHTERS = [auto_create_hero() for _ in range(COUNT_PERSES)]


def test_input_value(atr, max_value):
    value = input(
            f'Установите {atr} от 0 до {max_value}:  ')
    if value.isdigit():
        value = float(value)
    else:
        print('Введены неверные данные.')
        return False
    return (value, max_value)[value > max_value]


def create_hero():
    klasse = False
    while not klasse:
        klasse = input(
            'Выберите класс Warrior или Paladin - W/P: ').lower()
        if klasse not in AVAILABLE_HEROES_CLASSES:
            klasse = False
            print('Не правильно выбран класс.')
            continue
        klasse = AVAILABLE_HEROES_CLASSES[klasse]

    name = False
    while not name:
        name = input('Введите имя только из букв: ') + 'son'
        if not name.isalpha():
            name = False
            print('Не правильное имя.')

    defense = False
    while not defense:
        defense = test_input_value('защита', MAX_HERO_DEFENSE)

    attack = False
    while not attack:
        attack = test_input_value('атака', MAX_HERO_ATTACK)

    health = False
    while not health:
        health = test_input_value('здоровье', MAX_HERO_HEALTH)

    sex = input(
        'Выберите пол персонажа W/M:  ').lower()
    if sex not in 'wm':
        sex = 'm'

    gamer = klasse(name, defense, attack, health, sex)
    FIGHTERS.append(gamer)


def user_input():
    global SURVIVAL
    create_your_hero = input('Желаете создать нового персонажа? Y/N: ').lower()
    if create_your_hero == 'y':
        create_hero()
    survival = input('Хотите установить режим "На выживание"?'
                     ' Тогда бойцы не восстановят здоровье после боя: Y/N: '
                     ).lower()
    SURVIVAL = survival == 'y'


def get_things(fighters, things):
    for fighter in fighters:
        limit = random.randint(0, COUNT_THINGS_ON_PERS)
        choised_things = random.sample(things, limit)
        if choised_things:
            fighter.set_things(choised_things)
            print(f'\n"{fighter.name}" получил предметы:')
            for thing in choised_things:
                print(f'"{thing.name}"')
        else:
            print(f'\n"{fighter.name}" не повезло, ему не выпало ничего!')


def burn_child(fighter_1, fighter_2):
    name = (fighter_1.name + fighter_2.name)[:10]
    defense = (fighter_1.defense + fighter_2.defense) / 2
    attack = (fighter_1.attack + fighter_2.attack) / 2
    health = (fighter_1.health + fighter_2.health) / 2
    sex = fighter_1.sex
    child = Child(name, defense, attack, health, sex)
    FIGHTERS.append(child)
    return child


def battle(fighter_1, fighter_2):
    freeze_health_1 = fighter_1.health
    freeze_health_2 = fighter_2.health
    if fighter_1.sex != fighter_2.sex and random.randint(0, 2):
        return burn_child(fighter_1, fighter_2)

    while True:
        fighter_2.decrease_helth(fighter_1.attack)
        if fighter_2.health <= 0:
            FIGHTERS.remove(fighter_2)
            if not SURVIVAL:
                fighter_1.health = freeze_health_1
            return fighter_1
        fighter_1.decrease_helth(fighter_2.attack)
        if fighter_1.health <= 0:
            FIGHTERS.remove(fighter_1)
            if not SURVIVAL:
                fighter_2.health = freeze_health_2
            return fighter_2


def main():
    count_battle = 0
    user_input()
    get_things(FIGHTERS, THINGS)
    print('\n---------  FIGHT!  --------\n')

    while len(FIGHTERS) > 1:
        fighter_1, fighter_2 = random.sample(FIGHTERS, 2)
        count_battle += 1
        print(f'Бой №{count_battle} начался! '
              f'Участники: {fighter_1.name} и {fighter_2.name}.\n')
        winner = battle(fighter_1, fighter_2)
        if winner not in (fighter_1, fighter_2):
            print(f'В этой встрече родился {winner.name}!\n')
        else:
            print(f'В этом бою победил {winner.name}!!!\n')

    winner = FIGHTERS[0]
    print(f'    Поздравляем чемпиона {count_battle} боёв:'
          f'    {type(winner).__name__} {winner.name}!!!')
    print('     ______GAME OVER______')


if __name__ == '__main__':
    main()
