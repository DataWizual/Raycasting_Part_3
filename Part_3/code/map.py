from settings import *

text_map = [    
    'WWWWWWWWWWWW',
    'W....W.....W',
    'W..W...W...W',
    'W....W..WW.W',
    'W.WW....W..W',
    'W.W..W.WWW.W',
    'W....W.....W',
    'WWWWWWWWWWWW'
    ]

world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == '1': world_map[(i * TILE, j * TILE)] = '1'
            elif char == '2': world_map[(i * TILE, j * TILE)] = '2'        