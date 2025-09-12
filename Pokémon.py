class Pokémon:
    def __init__(self, name, typ, attacken, hp):
        self.name = name
        self.typ = typ
        self.attacken = attacken
        self.hp = hp

class Typen:
    def __init__(self):
        pass
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

    def Typendatenbank(self):
        pass
        #Wasser
        #Feuer
        #Pflanze