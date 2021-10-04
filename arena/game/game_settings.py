MAX_DEFENSE = 90

#  things settings
MAX_THING_DEFENSE = 0.1
MAX_THING_ATTACK = 100
MAX_THING_HEALTH = 100

#  heros settings
MAX_HERO_DEFENSE = 10
MAX_HERO_ATTACK = 20
MAX_HERO_HEALTH = 50

# game mode (restoring health)
SURVIVAL = False

COUNT_THINGS_ON_PERS = 4

COUNT_PERSES = 20

NAMES = [
    ('Keowe', 'w'),
    ('Gary', 'm'),
    ('Lucille', 'w'),
    ('Joanne', 'w'),
    ('Ruby', 'm'),
    ('Douglas', 'm'),
    ('Marjorie', 'w'),
    ('Ashley', 'w'),
    ('Sarah', 'w'),
    ('Jennifer', 'w'),
    ('Eric', 'm'),
    ('Ivan', 'm'),
    ('Jesse', 'w'),
    ('Stephen', 'm'),
    ('Leonard', 'm'),
    ('Cathy', 'w'),
    ('Cathy', 'm'),
    ('Brenda', 'w'),
    ('Thomas', 'm'),
    ('Henry', 'm'),
]

if COUNT_PERSES > len(NAMES):
    COUNT_PERSES = len(NAMES)
