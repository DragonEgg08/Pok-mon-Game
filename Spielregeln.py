import random
from Spieler import Spieler
from Pokémon import Typenabfrage

#Würfeln für Vorspiel
def würfeln() -> int:
    return random.randint(1,6)

def Würfelwurf(Spieler1: Spieler, Spieler2: Spieler) -> bool:
    while True:
        Spieler1_Ergebnis = würfeln()
        Spieler2_Ergebnis = würfeln()
        Spieler1_gewonnen = False

        print(f"{Spieler1.name} würfelt und hat eine {Spieler1_Ergebnis}")
        print(f"{Spieler2.name} würfelt und hat eine {Spieler2_Ergebnis}")

        if Spieler1_Ergebnis > Spieler2_Ergebnis:
            Spieler1_gewonnen = True
            break
        elif Spieler1_Ergebnis == Spieler2_Ergebnis:
            print("Beide Spieler haben die gleiche Augenzahl, es wird nochmal gewürfelt\n\n\n")
        else:
            break
    return Spieler1_gewonnen

def Pokémon_auswählen(Alle_Pokémon, Spieler:Spieler):
    Typen_Reihenfolge = Typenabfrage()
    Typen_Menge = len(Typen_Reihenfolge)
    Typen_Print_Zähler = 0
    print(f"{Spieler.name} würfelt\n")
    print(f"\n{Typen_Reihenfolge[0]}")
    for i in range(len(Alle_Pokémon)):
        print(f"{i+1}. {Alle_Pokémon[i].name}")
        #Berechnung unten noch falsch
        if i != 0 and Typen_Menge / i == int(Typen_Menge / i):
            print({Typen_Reihenfolge[Typen_Print_Zähler] + "\n"})
            Typen_Print_Zähler += 1


    Auswahl = int(input("Gib eine Zahl für das Pokémon ein: "))
    Spieler.pokémon.append(Alle_Pokémon[Auswahl-1])
    Alle_Pokémon.pop(Auswahl-1)