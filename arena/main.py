import random
from time import sleep

from game import game_settings
from game.game_settings import (
    CREATE_USERS_HERO, MAX_HERO_DEFENSE, MAX_HERO_ATTACK, MAX_HERO_DODGE,
    MAX_HERO_HEALTH, WITH_THINGS)
from game.heroes import Child, AVAILABLE_HEROES_CLASSES
from game.things import THINGS


COUNT_BOTS = game_settings.COUNT_BOTS
COUNT_THINGS_ON_HERO = game_settings.COUNT_THINGS_ON_HERO
MAX_POPULATION = game_settings.MAX_POPULATION
SURVIVAL = game_settings.SURVIVAL


def user_settings():
    if input('Изменить настройки игры? Y/N:  ').lower() != 'y':
        return None
    global COUNT_BOTS
    global COUNT_THINGS_ON_HERO
    global MAX_POPULATION
    global SURVIVAL

    count_bots = False
    while count_bots is False:
        count_bots = check_input_numeric_value(
            atr='количество ботов',
            max_value=game_settings.COUNT_BOTS)
    COUNT_BOTS = count_bots

    count_things_on_hero = False
    while count_things_on_hero is False:
        count_things_on_hero = check_input_numeric_value(
            atr='Количество вещей у героя',
            max_value=game_settings.COUNT_THINGS_ON_HERO)
    COUNT_THINGS_ON_HERO = count_things_on_hero

    max_population = False
    while max_population is False:
        max_population = check_input_numeric_value(
            atr='Максимально количество героев',
            min_value=COUNT_BOTS, max_value=game_settings.MAX_POPULATION)
    MAX_POPULATION = max_population

    SURVIVAL = input(
        'Установить режим игры "на выживание"?'
        'HP не будет восстанавлиываться после боя. Y/N  :').lower() == 'y'


def check_input_numeric_value(atr, min_value=0, max_value=1):
    '''Checking user input for numeric attributes.'''

    value = input(
            f'Установите {atr} от {min_value} до {max_value}:  ')
    if not value.isdigit():
        print('Введены неверные данные.')
        return False
    value = int(value)
    return (value, max_value)[value > max_value]


def auto_create_hero(names):
    '''Creates bots when the program starts.'''

    klasses = list(AVAILABLE_HEROES_CLASSES.values())
    klasse = random.choice(klasses)
    name, sex = names.pop(random.randint(0, len(names) - 1))
    defense = random.randint(0, MAX_HERO_DEFENSE)
    attack = random.randint(1, MAX_HERO_ATTACK)
    dodge = random.randint(0, MAX_HERO_DODGE)
    helth = random.randint(1, MAX_HERO_HEALTH)
    hero = klasse(name, sex, defense, attack, dodge, helth)
    print(f'Create {type(hero).__name__} "{hero.name}" {hero.sex}\n'
          f'def={hero.defense}, attack={hero.attack}, '
          f'dodge={hero.dodge}, HP={hero.health}\n\n')
    return hero


def create_hero():
    '''Creating a custom hero.'''

    klasse = False
    while not klasse:
        print('На данный момент в игре доступны следующие классы:')
        [print(
            AVAILABLE_HEROES_CLASSES[klass].__name__
            ) for klass in AVAILABLE_HEROES_CLASSES]
        klasse = input(
            'Выберите класс введя первую букву класса: ').lower()
        if klasse not in AVAILABLE_HEROES_CLASSES:
            klasse = False
            print('Не правильно выбран класс.')
            continue
        klasse = AVAILABLE_HEROES_CLASSES[klasse]
        print(f'Выбран {klasse.__name__}')

    name = False
    while not name:
        name = (input('Введите имя только из букв: ') + 'son').capitalize()
        if not name.isalpha():
            name = False
            print('Не правильное имя.')
            continue
        print(f'Выбрано {name}')

    sex = False
    while not sex:
        sex = input('Выберите пол персонажа W/M:  ').lower()
        if sex not in 'mw':
            sex = False
            print('Неправильно указан пол.')
            continue

    defense = False
    while defense is False:
        defense = check_input_numeric_value(
            atr='защита', max_value=MAX_HERO_DEFENSE)

    attack = False
    while attack is False:
        attack = check_input_numeric_value(
            atr='атака', max_value=MAX_HERO_ATTACK)

    dodge = False
    while dodge is False:
        dodge = check_input_numeric_value(
            atr='уклонение', max_value=MAX_HERO_DODGE)

    health = False
    while health is False:
        health = check_input_numeric_value(
            atr='здоровье', max_value=MAX_HERO_HEALTH)

    hero = klasse(name, sex, defense, attack, dodge, health)
    return hero


def user_create_hero(HEROES):
    '''Allows the user to set game settings and create custom heroes.'''

    create_heroes = CREATE_USERS_HERO
    while create_heroes:
        available_count_create = MAX_POPULATION - len(HEROES)
        if not available_count_create:
            break
        print(f'Доступно создание {available_count_create} героев')
        create = input('Желаете создать нового героя? Y/N: ').lower()
        if create != 'y':
            break
        hero = create_hero()
        print(f'Create {type(hero).__name__} "{hero.name}" {hero.sex}\n'
              f'def={hero.defense}, attack={hero.attack}, '
              f'dodge={hero.dodge} HP={hero.health}\n')
        HEROES.append(hero)


def get_things(heroes, things):
    '''Distribution of things to heroes.'''

    if not WITH_THINGS or COUNT_THINGS_ON_HERO == 0:
        return None
    for hero in heroes:
        limit = random.randint(0, COUNT_THINGS_ON_HERO)
        choised_things = random.sample(things, limit)
        if choised_things:
            hero.set_things(choised_things)
            print(f'\n{hero.name} получил предметы:')
            for thing in choised_things:
                print(f'"{thing.name}"')
        else:
            print(f'\n"{hero.name}" не повезло, ему не выпало ничего!')
        print(
            f'def={hero.defense}, attack={hero.attack}, '
            f'dodge={hero.dodge}, HP={hero.health}\n\n')


def burn_child(heroes, fighter_1, fighter_2):
    '''Creating a new hero if two opposite-sex heroes meet.'''

    name = (fighter_1.name + fighter_2.name)[:13]
    sex = fighter_1.sex
    defense = (fighter_1.defense + fighter_2.defense) // 2
    attack = (fighter_1.attack + fighter_2.attack) // 2
    dodge = (fighter_1.dodge + fighter_2.dodge) // 2
    health = (fighter_1.health + fighter_2.health) // 2
    child = Child(name, sex, defense, attack, dodge, health)
    heroes.append(child)
    if len(heroes) > MAX_POPULATION:
        random.shuffle(heroes)
        del heroes[:(MAX_POPULATION // 2)]
        print('Половина населения погибли от голода!')
        sleep(2)
    return child


def two_heroes_fight(HEROES, fighter_1, fighter_2):
    '''The battle of two heroes.
    A new bot may appear if two heroes of the opposite sex meet.'''

    freeze_health_1 = fighter_1.health
    freeze_health_2 = fighter_2.health
    if fighter_1.sex != fighter_2.sex and random.randint(0, 2):
        return burn_child(HEROES, fighter_1, fighter_2)

    while True:
        fighter_2.decrease_helth(fighter_1.attack)
        if fighter_2.health <= 0:
            HEROES.remove(fighter_2)
            if not SURVIVAL:
                fighter_1.health = freeze_health_1
            return fighter_1
        fighter_1.decrease_helth(fighter_2.attack)
        if fighter_1.health <= 0:
            HEROES.remove(fighter_1)
            if not SURVIVAL:
                fighter_2.health = freeze_health_2
            return fighter_2


def main():
    user_settings()
    names = game_settings.NAMES.copy()
    HEROES = [auto_create_hero(names) for _ in range(COUNT_BOTS)]
    count_battle = 0
    user_create_hero(HEROES)
    if not HEROES:
        print('Желающих сражаться - нет.')
        return None
    get_things(HEROES, THINGS)
    print('\n---------  FIGHT!  --------\n')

    while len(HEROES) > 1:
        fighter_1, fighter_2 = random.sample(HEROES, 2)
        count_battle += 1
        print(f'Бой №{count_battle} начался! \n'
              f'Участники: {type(fighter_1).__name__} {fighter_1.name} и'
              f' {type(fighter_2).__name__} {fighter_2.name}.\n')
        winner = two_heroes_fight(HEROES, fighter_1, fighter_2)
        if winner not in (fighter_1, fighter_2):
            print(f'В этой встрече родился {winner.name}!\n')
        else:
            print(f'В этом бою победил {winner.name}!!!\n')

    winner = HEROES[0]
    print(f'    Поздравляем чемпиона {count_battle} боёв:\n'
          f'    {type(winner).__name__} {winner.name} ({winner.sex})!!!\n'
          f'def={winner.defense}, attack={winner.attack}, '
          f'dodge={winner.dodge}, HP={winner.health}')
    print('\n---------  GAME OVER  --------\n')


if __name__ == '__main__':
    running = True
    while running:
        main()
        running = input('Сыграем ещё? Y/N:  \n\n').lower()
        running = running == 'y'
