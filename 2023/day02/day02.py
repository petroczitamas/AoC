import os
import re

with open(os.path.join(os.path.dirname(__file__), "day02.txt"), "r") as f:
    data: list[str] = [re.sub(r'Game \d+: ', '', game, count=1) for game in f.read().splitlines()]

cubes_in_bag: dict = {
    'red'   : 12,
    'green' : 13,
    'blue'  : 14
}

possible_games: int = 0

power_games = 0

games: list[list[dict[str, int]]] = [[{cube.split(' ')[1]: int(cube.split(' ')[0]) for cube in draw.split(', ')} for draw in game.split('; ')] for game in data]

for i, game in enumerate(games):
    good_draws: dict = {
        'count' : 0,
        'red'   : 0,
        'green' : 0,
        'blue'  : 0
    }

    for j, draw in enumerate(game):
        if all([cubes_in_bag[key] >= draw[key] for key in draw.keys()]):
            good_draws['count'] += 1
        for key in draw.keys():
            if good_draws[key] < draw[key]:
                good_draws[key] = draw[key]
    
    if good_draws['count'] == len(game):
        possible_games += (i + 1)
    
    power_games += (good_draws['red'] * good_draws['green'] * good_draws['blue'])

print(possible_games)

print(power_games)

# Part 1 result: 2416
# Part 2 result: 63307