from array import ArrayType

from Pokémon import Pokémon
import random
pkm_pool = [
    #Wasser-Pokémon
    Pokémon("Aquana", "Wasser", "", 300),
    Pokémon("Garados", "Wasser", "", 300),
    Pokémon("Turtok", "Wasser", "", 300),

    #Feuer-Pokémon
    Pokémon("Glurak", "Feuer", "", 300),
    Pokémon("Miezunder", "Feuer", "", 300),
    Pokémon("Azugladis", "Feuer", "", 300),

    #Pflanzen-Pokémon
    Pokémon("Silvaro", "Pflanze", "", 300),
    Pokémon("Maskagato", "Pflanze", "", 300),
    Pokémon("Serpiroyal", "Pflanze", "", 300),

    #Psycho-Pokémon
    Pokémon("Guardevoir", "Pflanze", "", 400)
    ]
#Guardevoir
#Kapu-Fala

def Pool():
    """Random_Nummer = random.randint(0, len(pkm_pool))
    Ausgewähltes_Pokémon = pkm_pool[Random_Nummer]
    pkm_pool.pop(Random_Nummer)
    return Ausgewähltes_Pokémon"""
    return pkm_pool
