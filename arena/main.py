import random
from time import sleep

from game.game_settings import (
    COUNT_BOTS, COUNT_THINGS_ON_PERS, CREATE_USERS_HERO, MAX_HERO_DEFENSE,
    MAX_HERO_ATTACK, MAX_HERO_HEALTH, NAMES, SURVIVAL, WITH_THINGS)
from game.heroes import Child, Paladin, Warrior, AVAILABLE_HEROES_CLASSES
from game.things import THINGS


def auto_create_hero():
    klasse = Warrior if random.randint(0, 1) else Paladin
    name, sex = NAMES.pop(random.randint(0, len(NAMES) - 1))
    defense = random.randint(0, MAX_HERO_DEFENSE)
    attack = random.randint(1, MAX_HERO_ATTACK)
    helth = random.randint(1, MAX_HERO_HEALTH)
    hero = klasse(name, sex, defense, attack, helth)
    print(f'Create {type(hero).__name__} "{hero.name}" {hero.sex}\n'
          f'def={hero.defense}, attack={hero.attack}, HP={hero.health}\n\n')
    return hero


FIGHTERS = [auto_create_hero() for _ in range(COUNT_BOTS)]


def check_input_digit_value(atr, max_value):
    '''Checking user input for numeric attributes.'''
    value = input(
            f'Установите {atr} от 1 до {max_value}:  ')
    if value.isdigit():
        value = float(value)
    else:
        print('Введены неверные данные.')
        return False
    return (value, max_value)[value > max_value]


def create_hero():
    '''Creating a custom hero.'''
    klasse = False
    while not klasse:
        print('На данный момент в игре доступны следующие классы:')
        [print(
            AVAILABLE_HEROES_CLASSES[i].__name__
            ) for i in AVAILABLE_HEROES_CLASSES]
        klasse = input(
            'Выберите класс введя первую букву класса: ').lower()
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

    sex = ('m', 'w')[input('Выберите пол персонажа W/M:  ').lower() == 'w']

    defense = False
    while not defense:
        defense = check_input_digit_value('защита', MAX_HERO_DEFENSE)

    attack = False
    while not attack:
        attack = check_input_digit_value('атака', MAX_HERO_ATTACK)

    health = False
    while not health:
        health = check_input_digit_value('здоровье', MAX_HERO_HEALTH)

    hero = klasse(name, sex, defense, attack, health)
    print(f'Create {type(hero).__name__} "{hero.name}" {hero.sex}\n'
          f'def={hero.defense}, attack={hero.attack}, HP={hero.health}\n\n')
    FIGHTERS.append(hero)


def user_input():
    global CREATE_USERS_HERO, SURVIVAL
    while CREATE_USERS_HERO:
        if input('Желаете создать нового персонажа? Y/N: ').lower() == 'y':
            create_hero()
        else:
            CREATE_USERS_HERO = False
    survival = input('Хотите установить режим "На выживание"?'
                     ' Тогда бойцы не восстановят здоровье после боя: Y/N: '
                     ).lower()
    SURVIVAL = survival == 'y'


def get_things(fighters, things):
    '''Distribution of things to heroes.'''
    if not WITH_THINGS:
        return None
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
        sleep(0.1)


def burn_child(fighter_1, fighter_2):
    '''Creating a new hero if two opposite-sex heroes meet.'''
    name = (fighter_1.name + fighter_2.name)[:13]
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
        print(f'Бой №{count_battle} начался! \n'
              f'Участники: {type(fighter_1).__name__} {fighter_1.name} и'
              f' {type(fighter_2).__name__} {fighter_2.name}.\n')
        winner = battle(fighter_1, fighter_2)
        if winner not in (fighter_1, fighter_2):
            print(f'В этой встрече родился {winner.name}!\n')
        else:
            print(f'В этом бою победил {winner.name}!!!\n')

    winner = FIGHTERS[0]
    print(f'    Поздравляем чемпиона {count_battle} боёв:'
          f'    {type(winner).__name__} {winner.name} ({winner.sex})!!!')
    print('     ______GAME OVER______')


if __name__ == '__main__':
    main()
