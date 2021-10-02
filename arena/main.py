import random

from game.game_settings import (
    NAMES, COUNT_PERSES, COUNT_THINGS_ON_PERS,
    MAX_HERO_DEFENSE, MAX_HERO_ATTACK, MAX_HERO_HEALTH, SURVIVAL)
from game.heroes import Child, Paladin, Warrior
from game.things import THINGS


def auto_create_hero():
    klasse = Warrior if random.randint(0, 1) else Paladin
    name, sex = NAMES.pop(random.randint(0, len(NAMES) - 1))
    defense = random.randint(1, 10) / 100
    attack = random.randint(1, 20)
    helth = random.randint(1, 20)
    return klasse(name, defense, attack, helth, sex)


FIGHTERS = [auto_create_hero() for _ in range(COUNT_PERSES)]


def create_person(klasse):
    gamer = klasse(
        name=input('Введите имя: '),
        defense=float(input(
            f'Установите защиту от 0 до {MAX_HERO_DEFENSE}:  ')),
        attack=float(input(
            f'Установите атаку от 1 до {MAX_HERO_ATTACK}:  ')),
        health=float(input(
            f'Установите злоровье от 1 до {MAX_HERO_HEALTH}:  ')),
        sex=(input(
            'Выберите пол персонажа W/M:  ').lower()), )
    FIGHTERS.append(gamer)


def user_input():
    global SURVIVAL
    gamer = input('Желаете создать нового персонажа? Y/N: ').lower()
    if gamer == 'y':
        gamer = input('Выберите класс Warrior или Paladin - W/P: ').lower()
        if gamer == 'w':
            create_person(Warrior)
        elif gamer == 'p':
            create_person(Paladin)
        else:
            print('Вы не выбрали нужный класс, продолжим без Вас.')
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
            if not SURVIVAL:
                fighter_1.health = freeze_health_1
            return fighter_1
        fighter_1.decrease_helth(fighter_2.attack)
        if fighter_1.health <= 0:
            if not SURVIVAL:
                fighter_2.health = freeze_health_2
            return fighter_2


def main():
    count_battle = 0
    user_input()
    get_things(FIGHTERS, THINGS)
    print('\n---------  FIGHT!  --------\n')

    while True:
        len_fighters = len(FIGHTERS) - 2
        if len_fighters == -1:
            break
        limit = len(FIGHTERS) - 1
        fighter_1 = FIGHTERS.pop(random.randint(0, limit))
        fighter_2 = FIGHTERS.pop(random.randint(0, limit - 1))
        count_battle += 1
        print(f'Бой №{count_battle} начался! '
              f'Участники: {fighter_1.name} и {fighter_2.name}.\n')
        winner = battle(fighter_1, fighter_2)
        if len_fighters < len(FIGHTERS):
            print(f'В этом бою родился {winner.name}!\n')
            FIGHTERS.append(fighter_1)
            FIGHTERS.append(fighter_2)
        else:
            print(f'В этом бою победил {winner.name}!!!\n')
            FIGHTERS.append(winner)
    print(
        f'    Поздравляем победителя {FIGHTERS[0].name}!!!')


if __name__ == '__main__':
    main()
