from Spieler import Spieler
from Pokémon_Pool import Pool
from Pokémon import Attacken_hinzufügen
from Spielregeln import Würfelwurf, Pokémon_auswählen

Spieler1 = Spieler("Sky")
Spieler2 = Spieler("Elias")
Alle_Pokémon = Pool()
Attacken = Attacken_hinzufügen()

#Würfeln um Pokémon auszuwählen
for i in range(3):
    Wurf = Würfelwurf(Spieler1, Spieler2)
    if Wurf:
        print(f"{Spieler1.name} hat gewonnen")
        Pokémon_auswählen(Alle_Pokémon, Spieler1, False)
        print(f"{Spieler2.name} hat verloren")
        Pokémon_auswählen(Alle_Pokémon, Spieler2, True)
    else:
        print(f"{Spieler2.name} hat gewonnen")
        Pokémon_auswählen(Alle_Pokémon, Spieler2, False)
        print(f"{Spieler1.name} hat verloren")
        Pokémon_auswählen(Alle_Pokémon, Spieler1, True)

