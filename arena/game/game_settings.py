from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# audiofiles
start_game = BASE_DIR / 'Audio/start_game.mp3'
burn_child = BASE_DIR / 'Audio/burn_child.mp3'
last_breath = BASE_DIR / 'Audio/last_breath.mp3'
death_half_population = BASE_DIR / 'Audio/death_half_population.mp3'
win = BASE_DIR / 'Audio/win.mp3'

# acceptable attributes of heroes
ATTRIBUTES_HERO = (
    'name', 'sex',  'defense', 'attack', 'defense', 'health')

#  things settings
MAX_THING_DEFENSE = 50
MAX_THING_ATTACK = 100
MAX_THING_DODGE = 50
MAX_THING_HEALTH = 100

#  heros settings
MAX_HERO_DEFENSE = 10
MAX_HERO_ATTACK = 20
MAX_HERO_DODGE = 10
MAX_HERO_HEALTH = 50

# game mode (restoring health)
MAX_DEFENSE = 90
MAX_DODGE = 90
MAX_POPULATION = 10
FERTILITY = 10
SURVIVAL = False
WITH_THINGS = True
CREATE_USERS_HERO = True

COUNT_THINGS_ON_HERO = 4

NAMES = [
    ('Cynthia', 'Brown', 'w'),
    ('Bob', 'Sullivan', 'm'),
    ('Jason', 'Lewis', 'm'),
    ('Ben', 'Little', 'm'),
    ('Jesse', 'Clayton', 'w'),
    ('Elizabeth', 'Ford', 'w'),
    ('Peggy', 'Jackson', 'w'),
    ('Josephine', 'Gilbert', 'w'),
    ('Victoria', 'Carroll', 'w'),
    ('Arthur', 'Strickland', 'm'),
    ('Randy', 'Adams', 'w'),
    ('Pamela', 'Harmon', 'w'),
    ('Joanne', 'Phillips', 'w'),
    ('Kenneth', 'Wilson', 'm'),
    ('Richard', 'Henry', 'm'),
    ('Rafael', 'Johnson', 'm'),
    ('Christopher', 'Harrison', 'm'),
    ('Terri', 'Williams', 'w'),
    ('Rufus', 'Carlson', 'm'),
    ('Kathleen', 'Shelton', 'w'),
    ('Vernon', 'Hanson', 'm'),
    ('James', 'Curry', 'm'),
    ('Louise', 'Sparks', 'm'),
    ('Peggy', 'Holmes', 'w'),
    ('Henry', 'Martin', 'm'),
    ('William', 'Smith', 'm'),
    ('Don', 'Kelley', 'm'),
    ('Thomas', 'McCarthy', 'm'),
    ('Corey', 'Dunn', 'w'),
    ('Rhonda', 'Ramirez', 'w'),
    ('Julie', 'Waters', 'w'),
    ('Tammy', 'Crawford', 'w'),
    ('Linda', 'Vasquez', 'w'),
    ('Curtis', 'Morgan', 'm'),
    ('James', 'Burns', 'm'),
    ('Ernest', 'Turner', 'm'),
    ('Cindy', 'Wolfe', 'w'),
    ('Theresa', 'Kelley', 'w'),
    ('Warren', 'McCoy', 'm'),
    ('Peter', 'Scott', 'm'),
    ('Lisa', 'Wagner', 'w'),
    ('Donna', 'Murphy', 'w'),
    ('Sherry', 'Guzman', 'w'),
    ('Leonard', 'Alvarez', 'm'),
    ('Teresa', 'Johnson', 'w'),
    ('Chris', 'Smith', 'm'),
    ('Barbara', 'Gordon', 'w'),
    ('Catherine', 'Miller', 'w'),
    ('Carrie', 'Wells', 'w'),
    ('Doris', 'Graham', 'w'),
    ('Edna', 'Ortega', 'w'),
    ('Nancy', 'Williams', 'w'),
    ('Bobby', 'Reeves', 'm'),
    ('Frank', 'Pearson', 'm'),
    ('Kevin', 'Scott', 'm'),
    ('Christine', 'Thomas', 'w'),
    ('Edward', 'Long', 'm'),
    ('Frank', 'Gardner', 'm'),
    ('Ruth', 'Perkins', 'm'),
    ('Rebecca', 'Johnson', 'w'),
    ('Sandra', 'Cannon', 'w'),
    ('John', 'Vasquez', 'm'),
    ('Cassandra', 'Clarke', 'w'),
    ('Ann', 'Williamson', 'w'),
    ('Joseph', 'Lee', 'm'),
    ('AnnMary', 'Farmer', 'w'),
    ('James', 'Jordan', 'm'),
    ('Sheila', 'Delgado', 'w'),
    ('Patricia', 'Payne', 'w'),
    ('Shirley', 'Morgan', 'w'),
    ('Eloise', 'Marsh', 'w'),
    ('Karen', 'Harris', 'm'),
    ('Bradley', 'Johnson', 'm'),
    ('Sarah', 'McCoy', 'w'),
    ('Karen', 'Smith', 'w'),
    ('David', 'Moore', 'm'),
    ('Pedro', 'Hawkins', 'm'),
    ('Sue', 'Carpenter', 'w'),
    ('Lucille', 'Padilla', 'w'),
    ('Anna', 'Bush', 'w'),
    ('Jerry', 'Edwards', 'w'),
    ('Rhonda', 'Burgess', 'w'),
    ('Ray', 'McGee', 'm'),
    ('Stanley', 'Baker', 'm'),
    ('Eleanor', 'Allen', 'w'),
    ('Peter', 'Gomez', 'm'),
    ('Amanda', 'Nelson', 'w'),
    ('Carol', 'Manning', 'w'),
    ('Warwara', 'Harris', 'w'),
    ('Nicole', 'Murphy', 'w'),
    ('Djohn', 'Lopez', 'm'),
    ('Karina', 'Brown', 'w'),
    ('Dorothy', 'Richardson', 'w'),
    ('Lorraine', 'Rodriguez', 'w'),
    ('Jimmy', 'Clark', 'm'),
    ('Carl', 'Garcia', 'm'),
    ('David', 'Castillo', 'm'),
    ('Dorris', 'Brown', 'm'),
    ('Thomas', 'Wilson', 'm'),
    ('Ryan', 'Washington', 'm'),
]

COUNT_BOTS = 50
if COUNT_BOTS > len(NAMES):
    COUNT_BOTS = len(NAMES)
if COUNT_BOTS > MAX_POPULATION:
    COUNT_BOTS = MAX_POPULATION
