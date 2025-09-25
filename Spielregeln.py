import random
from Spieler import Spieler
from Pokémon import Typen_hinzufügen, Pokémon, Attacken, Schwächen_Stärken

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

def Pokémon_auswählen(Alle_Pokémon, Spieler:Spieler, Random):
    if Random:
        Zahl = random.randint(0, len(Alle_Pokémon))
        print(Zahl)
        Spieler.pokémon.append(Alle_Pokémon[Zahl])
        print(f"{Spieler.name} bekommt als random Pokémon {Spieler.pokémon[-1].name}")
        Alle_Pokémon.pop(Zahl)
    else:
        Typen_Reihenfolge = Typen_hinzufügen()
        Pokémon_print_Zähler = 1
        print(f"{Spieler.name} wählt ein Pokémon\n")
        print(Typen_Reihenfolge[0])
        for i in Typen_Reihenfolge:
            print("\n" + i)
            for a in Alle_Pokémon:
                if a.typ == i:
                    print(f"{Pokémon_print_Zähler}. {a.name}")
                    Pokémon_print_Zähler += 1

        Auswahl = int(input("Gib eine Zahl für das Pokémon ein: "))
        Spieler.pokémon.append(Alle_Pokémon[Auswahl-1])
        Alle_Pokémon.pop(Auswahl-1)

def Kampf(Pokémon, Pokémon_Gegner:Pokémon):
    for i in range(len(Pokémon.attacken)):
        print(f"{i+1}. {Pokémon.attacken[i].name}")
    Attacke:Attacken = Pokémon.attacken[int(input("Wähle eine Attacke aus: "))-1]
    Resistenz = int(Schwächen_Stärken(Pokémon.typ, Pokémon_Gegner.typ))
    print(Resistenz)

    if Resistenz != 0:
        Pokémon_Gegner.hp -= (Attacke.schaden-Attacke.schaden*Resistenz)
    else:
        Pokémon_Gegner.hp -= Attacke.schaden
