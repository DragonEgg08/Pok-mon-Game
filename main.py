from Spieler import Spieler
from Pokémon import Pokémon, Typen
from Pokémon_Pool import Pool
from Spielregeln import Würfelwurf, Pokémon_auswählen

Spieler1 = Spieler("Rot")
Spieler2 = Spieler("Blau")
Alle_Pokémon = Pool()

for i in range(3):
    Wurf = Würfelwurf(Spieler1, Spieler2)
    if Wurf:
        print(f"{Spieler1.name} hat gewonnen, er würfelt:")
        Pokémon_auswählen(Alle_Pokémon, Spieler1)
        print(f"{Spieler2.name} hat verloren, er würfelt:")
        Pokémon_auswählen(Alle_Pokémon, Spieler2)
    else:
        print(f"{Spieler2.name} hat gewonnen, er würfelt:")
        Pokémon_auswählen(Alle_Pokémon, Spieler2)
        print(f"{Spieler1.name} hat verloren, er würfelt:")
        Pokémon_auswählen(Alle_Pokémon, Spieler1)

