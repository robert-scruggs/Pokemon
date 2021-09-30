import math
import time, sys, random

from classes import Pokemon

pokemon_list = {
    'Pikachu': Pokemon(math.floor(random.random() * 10),math.floor(random.random() * 10),'Pikachu'),
    'Ghastly': Pokemon(math.floor(random.random() * 10),math.floor(random.random() * 10),'Ghastly'),
    'Haunter': Pokemon(math.floor(random.random() * 10),math.floor(random.random() * 10),'Haunter'),
    'Lotad': Pokemon(math.floor(random.random() * 10),math.floor(random.random() * 10),'Lotad'),
    'Miltank': Pokemon(math.floor(random.random() * 10),math.floor(random.random() * 10),'Miltank')
}
for pokemon in pokemon_list.items():
    print(pokemon)


pikachu = Pokemon(math.floor(random.random() * 10),math.floor(random.random() * 10),'Pikachu')
ghastly = Pokemon(math.floor(random.random() * 10),math.floor(random.random() * 10),'Ghastly')
haunter = Pokemon(math.floor(random.random() * 10),math.floor(random.random() * 10),'Haunter')
lotad = Pokemon(math.floor(random.random() * 10),math.floor(random.random() * 10),'Lotad')
miltank = Pokemon(math.floor(random.random() * 10),math.floor(random.random() * 10),'Miltank')

pikachu_attack = pikachu.attack
ghastly_attack = ghastly.attack
haunter_attack = haunter.attack
lotad_attack = lotad.attack
miltank_attack = miltank.attack


def pokemon_battle(p1,p2):
    if p1 > p2:
        return (f'Great job {pikachu.name}! You defeated {ghastly.name}!')
    elif p2 > p1:
        return (f'Great job {ghastly.name}! You defeated {pikachu.name}!')
    else:
        return 'Draw!'
print(pokemon_battle(pikachu.attack,ghastly.attack))
print(pokemon_battle(haunter.attack,lotad.attack))
print(pokemon_battle(pikachu.attack,miltank.attack))
print(pokemon_battle(ghastly.attack,lotad.attack))