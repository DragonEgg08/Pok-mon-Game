import Pokémon
import Spielregeln
from Spieler import Spieler
from Pokémon_Pool import Pool
from Pokémon import Attacken_hinzufügen
from Spielregeln import Würfelwurf, Pokémon_auswählen

Spieler1 = Spieler("Sky")
Spieler2 = Spieler("Elias")
Alle_Pokémon = Pool()

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

#Pokémon Kampf
S1_Kampf_Pokémon = ""
S2_Kampf_Pokémon = ""
while True:
    #Spieler Pokémon auswahl
    if S1_Kampf_Pokémon == "":
        for i in range(len(Spieler1.pokémon)):
            print(f"{i+1} {Spieler1.pokémon[i].name}")
        S1_Kampf_Pokémon = Spieler1.pokémon[int(input(f"{Spieler1.name}, Kampfpokémon auswählen: "))-1]

    if S2_Kampf_Pokémon == "":
        for i in range(len(Spieler2.pokémon)):
            print(f"{i + 1} {Spieler2.pokémon[i].name}")
        S2_Kampf_Pokémon = Spieler2.pokémon[int(input(f"{Spieler2.name}, Kampfpokémon auswählen: ")) - 1]
    if len(S1_Kampf_Pokémon.attacken) == 0:
        Pokémon.Attacken_hinzufügen(S1_Kampf_Pokémon)
        Pokémon.Attacken_hinzufügen(S2_Kampf_Pokémon)

    Spielregeln.Kampf(S1_Kampf_Pokémon, S2_Kampf_Pokémon)
    Spielregeln.Kampf(S2_Kampf_Pokémon, S1_Kampf_Pokémon)