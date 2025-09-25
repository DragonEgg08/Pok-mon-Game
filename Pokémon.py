import random


class Pokémon:
    def __init__(self, name:str, typ:str, attacken:str, hp:int):
        self.name = name
        self.typ = typ
        self.attacken = attacken
        self.hp = hp

class Typen:
    def __init__(self):
        self.name
    def Schwächen_Stärken(self, typ, typ_gegner) -> float | None:
        if typ == "Wasser" or typ == "Feuer" and typ_gegner == "Wasser" or typ_gegner == "Feuer":
            if typ == "Wasser":
                return 0.2
            else:
                return -0.2
        elif typ == "Wasser" or typ == "Pflanze" and typ_gegner == "Wasser" or typ_gegner == "Pflanze":
            if typ == "Pflanze":
                return 0.2
            else:
                return -0.2
        elif typ == "Pflanze" or typ == "Feuer" and typ_gegner == "Pflanze" or typ_gegner == "Feuer":
            if typ == "Feuer":
                return 0.2
            else:
                return -0.2
        return None

def Typen_hinzufügen():
    return "Wasser", "Feuer", "Pflanze"

class Attacken():
    def __init__(self, name, schaden, nutzungslimit, typ):
        self.name = name
        self.schaden = schaden
        self.nutzungslimit = nutzungslimit
        self.typ = typ

def Attacken_hinzufügen(Pokémon:Pokémon):
    Attacken_list_Normal = []
    Attacken_list_Feuer = []
    Attacken_list_Wasser = []
    Attacken_list_Pflanze = []
    ###Immer gleiche Anzahl von Attacken!!!
    #Normal
    Attacken_list_Normal.append(Attacken("Tackle", 70, 15, "Normal"))
    Attacken_list_Normal.append(Attacken("Bodyslam", 125, 5, "Normal"))
    #Feuer
    Attacken_list_Feuer.append(Attacken("Glut", 70, 15, "Feuer"))
    Attacken_list_Feuer.append(Attacken("Flammenwurf", 125, 5, "Feuer"))
    #Wasser
    Attacken_list_Wasser.append(Attacken("Blubber", 70, 15, "Wasser"))
    Attacken_list_Wasser.append(Attacken("Hydropumpe", 125, 5, "Wasser"))
    #Pflanze
    Attacken_list_Pflanze.append(Attacken("Rankenhieb", 70, 15, "Pflanze"))
    Attacken_list_Pflanze.append(Attacken("Energieball", 125, 5, "Pflanze"))

    Pokémon.attacken.append(Attacken_list_Normal[0])
    Pokémon.attacken.append(Attacken_list_Normal[1])

    if Pokémon.typ == "Feuer":
        Pokémon.attacken.append(Attacken_list_Feuer[0])
        Pokémon.attacken.append(Attacken_list_Feuer[1])
    elif Pokémon.typ == "Wasser":
        Pokémon.attacken.append(Attacken_list_Wasser[0])
        Pokémon.attacken.append(Attacken_list_Wasser[1])
    elif Pokémon.typ == "Pflanze":
        Pokémon.attacken.append(Attacken_list_Pflanze[0])
        Pokémon.attacken.append(Attacken_list_Pflanze[1])